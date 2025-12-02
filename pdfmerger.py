import os
import sys
from PyPDF2 import PdfMerger

def merge_numbered_pdfs(input_dir):
    # Collect only PDF files
    pdf_files = [f for f in os.listdir(input_dir) if f.lower().endswith(".pdf")]

    # Extract numeric prefix for ordering
    def extract_num(filename):
        stem = os.path.splitext(filename)[0]
        try:
            return int(stem)
        except ValueError:
            return float('inf')

    pdf_files.sort(key=extract_num)

    if not pdf_files:
        raise ValueError("No PDF files found in the directory.")

    output_path = os.path.join(input_dir, "merged.pdf")
    merger = PdfMerger()

    for pdf in pdf_files:
        merger.append(os.path.join(input_dir, pdf))

    merger.write(output_path)
    merger.close()

    print(f"Merged {len(pdf_files)} PDFs into: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python merge_pdfs.py /path/to/directory")
        sys.exit(1)

    merge_numbered_pdfs(sys.argv[1])
