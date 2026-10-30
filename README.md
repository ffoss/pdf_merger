# PDF Merger

Utilities for merging PDFs and converting/compressing images into PDFs.

## Environment Setup

This repository is managed by [uv](https://docs.astral.sh/uv/). uv should be installed beforehand.

Install dependencies and create the virtual environment: ```uv sync```

Add a new dependency: ```uv add <package>```

## Usage

### Merge PDFs

Merges a set of numbered PDF files located in a single directory. Filenames must begin with numeric names such as 1.pdf, 2.pdf, 3.pdf, etc. The script sorts them by their numeric value and produces a single file named merged.pdf inside the same directory.

```uv run python pdfmerger.py /path/to/your/pdf_directory```

### Compress an image into a PDF

Compresses an image (downsamples and re-encodes it) and saves the result as a PDF.

```uv run python image_to_pdf.py /path/to/image.jpg /path/to/output.pdf [quality]```

`quality` is optional (1-95, default 50); lower values produce smaller files.

### Extract text from a PDF

Extracts the text content of a PDF and writes it to a text file.

```uv run python pdf_to_text.py /path/to/input.pdf /path/to/output.txt```
