# Invoke_QRCodeNode

# QR Code Node

Welcome to the QR Code Node collection for InvokeAI.

With this node, you can encode a simple QR code easily within a single node.

## Installation

Drag the qrcode.py into your InvokeAI invocations folder (Currently located in your `/.venv/Lib/site-packages/invokeai/app/invocations` folder)

Open the developer console menu on launching Invoke's script, and run `pip install qrcode` to get dependencies installed.

## Generate QR Code

Inputs

    Data: The text or URL you want to encode into a QR code.

    Error Correction: The level of error correction ("L", "M", "Q", "H").

    Box Size: The size of each box in the QR code grid.

    Border: The thickness of the border.

    Fill Color: The color of the QR code itself.

    Background Color: The background color of the QR code.

How It Works

Simply input the URL or Data you want to convert into a QR code, tweak the settings as you like, and let the node generate a high-quality QR code for you. Once created, the QR code can be integrated into your graph and processed further or saved directly to your gallery.

You will probably want to use this with a ControlNet that can ingest a QR code, like `DionTimmer/controlnet_qrcode` 

Notes

    The Fill Color and Background Color fields accept RGB tuples for customization.

Special Thanks

    The Open-Source Community (especially lincolnloop/python-qrcode) for providing the QR code library this node relies upon.

Recommended Palette

For best results, high-contrast palettes are recommended. For example, black on white, white on black, etc.
