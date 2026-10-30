import sys

from PIL import Image


def compress_image_to_pdf(input_image_path, output_pdf_path, quality=50, max_dimension=2000):
    image = Image.open(input_image_path).convert("RGB")

    width, height = image.size
    scale = min(1.0, max_dimension / max(width, height))
    if scale < 1.0:
        image = image.resize((int(width * scale), int(height * scale)), Image.LANCZOS)

    image.save(output_pdf_path, "PDF", quality=quality, optimize=True)

    print(f"Saved compressed PDF to: {output_pdf_path}")


if __name__ == "__main__":
    if len(sys.argv) not in (3, 4):
        print("Usage: python image_to_pdf.py /path/to/image.jpg /path/to/output.pdf [quality]")
        sys.exit(1)

    input_image_path = sys.argv[1]
    output_pdf_path = sys.argv[2]
    quality = int(sys.argv[3]) if len(sys.argv) == 4 else 50

    compress_image_to_pdf(input_image_path, output_pdf_path, quality=quality)
