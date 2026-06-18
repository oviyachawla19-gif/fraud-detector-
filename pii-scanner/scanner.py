from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer.anonymizer_engine import AnonymizerEngine
from dataclasses import dataclass
from typing import List, Optional

analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

@dataclass(frozen=True)
class PIIEntity:
    entity_type: str
    text: str
    start: int
    end: int
    score: float

@dataclass(frozen=True)
class ScanResult:
    has_pii: bool
    entities: List[PIIEntity]
    redacted_text: Optional[str]

def scan_text(text: str, redact: bool = True) -> ScanResult:
    results = analyzer.analyze(text=text, language="en")

    entities = [
        PIIEntity(
            entity_type=r.entity_type,
            text=text[r.start:r.end],
            start=r.start,
            end=r.end,
            score=r.score
        )
        for r in results
    ]

    redacted_text = None
    if redact and entities:
        anonymized = anonymizer.anonymize(text=text, analyzer_results=results)
        redacted_text = anonymized.text

    return ScanResult(
        has_pii=len(entities) > 0,
        entities=entities,
        redacted_text=redacted_text
    )
