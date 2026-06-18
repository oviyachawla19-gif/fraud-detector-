import csv
from pathlib import Path
from scanner import PIIEntity

def write_csv_report(output_path: Path, rows):
    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "file_path",
            "entity_type",
            "text_found",
            "start_position",
            "end_position",
            "score",
            "redacted_text"
        ])

        for file_path, entity, redacted_text in rows:
            writer.writerow([
                file_path,
                entity.entity_type,
                entity.text,
                entity.start,
                entity.end,
                entity.score,
                redacted_text
            ])


def write_summary_report(output_path: Path, rows):
    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "file_path",
            "entity_count",
            "entity_types",
            "decision",
            "has_pii",
            "redacted_text"
        ])

        for file_path, entity_count, entity_types, decision, has_pii, redacted_text in rows:
            writer.writerow([
                file_path,
                entity_count,
                entity_types,
                decision,
                has_pii,
                redacted_text
            ])
