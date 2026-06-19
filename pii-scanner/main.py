import argparse
from pathlib import Path
import csv

from scanner import scan_text
from report import write_csv_report, write_summary_report
from gate import evaluate, GateDecision

TEXT_EXTENSIONS = {".txt", ".csv", ".json"}

def read_text_from_file(path: Path) -> str:
    if path.suffix.lower() == ".csv":
        lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
        return "\n".join(lines)
    else:
        return path.read_text(encoding="utf-8", errors="ignore")

def iter_files(path: Path):
    if path.is_file():
        yield path
    else:
        for p in path.rglob("*"):
            if p.is_file() and p.suffix.lower() in TEXT_EXTENSIONS:
                yield p

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True)
    parser.add_argument("--output", default="pii_report.csv")
    args = parser.parse_args()

    target_path = Path(args.path)
    output_path = Path(args.output)

    report_rows = []
    summary_rows = []
    total_files = 0
    files_with_pii = 0

    for file_path in iter_files(target_path):
        total_files += 1
        text = read_text_from_file(file_path)

        scan = scan_text(text)
        decision, clean_text = evaluate(scan)

        entity_types = sorted({entity.entity_type for entity in scan.entities})
        if scan.has_pii:
            files_with_pii += 1
            for entity in scan.entities:
                report_rows.append((str(file_path), entity, clean_text))

        summary_rows.append(
            (
                str(file_path),
                len(scan.entities),
                ";".join(entity_types),
                decision.value,
                scan.has_pii,
                clean_text if decision == GateDecision.REDACT else ""
            )
        )

        print(f"{decision.value.upper()} → {file_path}")

    if report_rows:
        write_csv_report(output_path, report_rows)
        print(f"\nReport saved to {output_path}")

    summary_path = output_path.with_name(f"{output_path.stem}_summary{output_path.suffix}")
    write_summary_report(summary_path, summary_rows)
    print(f"Summary saved to {summary_path}")

    print(f"\nFiles scanned: {total_files}")
    print(f"Files with PII: {files_with_pii}")

if __name__ == "__main__":
    main()

