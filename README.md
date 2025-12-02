# PDF Merger

This script merges a set of numbered PDF files located in a single directory. Filenames must begin with numeric names such as 1.pdf, 2.pdf, 3.pdf, etc. The script sorts them by their numeric value and produces a single file named merged.pdf inside the same directory.

## Environment Setup

This repository is managed by conda. Conda should be installed before hand.

Create the environment: ```conda env create -f environment.yaml```

Activate: environment: ```conda activate pdfmerger```

### Dependency Management

Dependencies are maintained with `pip`.

Install: ```pip install -r requirements.txt```

Add a new dependency by editing requirements.in and running: ```pip-compile requirements.in```

## Usage

Provide the directory containing the numbered PDFs:
```python merge_pdfs.py /path/to/your/pdf_directory```
