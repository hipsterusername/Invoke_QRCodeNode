from typing import Literal
import qrcode

from invokeai.app.invocations.primitives import ColorField, ImageField, ImageOutput
from .baseinvocation import BaseInvocation, InputField, InvocationContext, invocation
from ..models.image import ImageCategory, ResourceOrigin

@invocation("generate_qr_code", title="Generate QR Code", tags=["qr", "image"], category="image")
class GenerateQRCodeInvocation(BaseInvocation):
    """Generates a QR code with various options and forwards it to the pipeline"""

    Data: str = InputField(default="", description="The data (e.g., a URL) to encode into the QR code")
    error_correction: Literal["L", "M", "Q", "H"] = InputField(default="H", description="The error correction level")
    box_size: int = InputField(default=10, description="Size of each box in the QR code grid")
    border: int = InputField(default=4, description="Thickness of the border")
    fill_color: ColorField = InputField(default=ColorField(r=0, g=0, b=0, a=255), description="Color of the QR code")
    back_color: ColorField = InputField(default=ColorField(r=255, g=255, b=255, a=255), description="Background color")
    
    def invoke(self, context: InvocationContext) -> ImageOutput:
        qr = qrcode.QRCode(
            version=None,
            error_correction=getattr(qrcode.constants, f"ERROR_CORRECT_{self.error_correction}"),
            box_size=self.box_size,
            border=self.border,
        )
        
        qr.add_data(self.Data)
        qr.make(fit=True)
        
        img: PILImage = qr.make_image(
            fill_color=self.fill_color.tuple(),  # Using RGB tuple
            back_color=self.back_color.tuple()  # Using RGB tuple
        )

        # Presumed existing service for image creation in your system
        image_dto = context.services.images.create(
            image=img,
            image_origin=ResourceOrigin.INTERNAL,
            image_category=ImageCategory.GENERAL,
            node_id=self.id,
            session_id=context.graph_execution_state_id,
            is_intermediate=self.is_intermediate,
            workflow=self.workflow,
        )
        
        return ImageOutput(
            image=ImageField(image_name=image_dto.image_name),
            width=image_dto.width,
            height=image_dto.height,
        )