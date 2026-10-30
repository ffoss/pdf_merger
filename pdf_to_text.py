
import sys

import PyPDF2


def pdf_to_text(input_pdf, output_txt):
    with open(input_pdf, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""

    with open(output_txt, "w", encoding="utf-8") as txt_file:
        txt_file.write(text)

    print(f"Saved extracted text to: {output_txt}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python pdf_to_text.py /path/to/input.pdf /path/to/output.txt")
        sys.exit(1)

    pdf_to_text(sys.argv[1], sys.argv[2])
