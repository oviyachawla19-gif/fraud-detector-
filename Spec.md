# PII Scanner CLI

## What this project is

This is a Python command line app that looks through text files and finds personal information.
It checks for things like names, emails, phone numbers, and addresses.

## What it does

- You give it a file or a folder.
- It reads the text.
- It looks for PII using Presidio.
- It saves a simple CSV report when it finds anything.

## How to use it

Run one of these commands:

```bash
python main.py --path /path/to/file.txt
python main.py --path /path/to/folder
python main.py --path /path/to/folder --output report.csv
```

## Input

- A single file to scan.
- A folder to scan all text files inside.
- Works with plain text files like `.txt`, `.csv`, or `.json`.

## Output

- Shows a short summary in the terminal.
- Creates a CSV report with these columns:
  - file path
  - entity type
  - text found
  - start position
  - end position
  - score

## How it works

- `main.py` reads the command line options.
- The scanner reads text from files.
- Presidio checks the text for PII.
- The app writes the results into a CSV file.

## What you need

- Python 3.10 or newer.
- `presidio-analyzer` - learn more at https://microsoft.github.io/presidio/
- `argparse`, `pathlib`, `json`, `csv` (built into Python)

## Library links

- Presidio docs: https://microsoft.github.io/presidio/
- Presidio analyzer package: https://pypi.org/project/presidio-analyzer/
- Presidio anonymizer package: https://pypi.org/project/presidio-anonymizer/
- Python `argparse`: https://docs.python.org/3/library/argparse.html
- Python `pathlib`: https://docs.python.org/3/library/pathlib.html
- Python `json`: https://docs.python.org/3/library/json.html
- Python `csv`: https://docs.python.org/3/library/csv.html

## Next steps

1. Add `requirements.txt`.
2. Make `main.py` read `--path` and `--output`.
3. Scan files and detect PII.
4. Save the results to CSV.
