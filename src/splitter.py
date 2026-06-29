import re
from typing import Dict, List


def _normalize_whitespace(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("\u00a0", " ")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def _collapse_line_breaks(text: str) -> str:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(lines)


def _extract_fields(text: str) -> Dict[str, str]:
    normalized = _normalize_whitespace(text)
    lines = [line.strip() for line in normalized.splitlines() if line.strip()]

    fields: Dict[str, str] = {}
    current_key = None
    current_values: List[str] = []

    def flush():
        nonlocal current_key, current_values
        if current_key:
            fields[current_key] = " ".join(part.strip() for part in current_values if part.strip())
        current_key = None
        current_values = []

    for line in lines:
        if re.fullmatch(r"[A-Za-z][A-Za-z /?()]+:", line):
            flush()
            current_key = line[:-1]
            current_values = []
            continue

        if line in {"Fixture Details", "Match Official Details", "Report Details"}:
            if current_key:
                flush()
            current_key = line
            current_values = []
            continue

        if current_key is not None:
            current_values.append(line)

    flush()

    if "Fixture" in fields:
        fields["Fixture"] = fields["Fixture"].strip()
    if "Competition" in fields:
        fields["Competition"] = fields["Competition"].strip()
    if "Club" in fields:
        fields["Club"] = fields["Club"].strip()
    if "Referee Name" in fields:
        fields["Referee Name"] = fields["Referee Name"].strip()
    if "Report Submitted By" in fields:
        fields["Report Submitted By"] = fields["Report Submitted By"].strip()
    if "Report Details" in fields:
        fields["Report Details"] = re.sub(r"\s+", " ", fields["Report Details"]).strip()

    return fields


def _build_structured_text(fields: Dict[str, str]) -> str:
    lines = ["Document Type: Extraordinary Incident Report", ""]

    field_order = [
        ("Fixture", "Fixture"),
        ("Competition", "Competition"),
        ("Match Date", "Match Date"),
        ("Is Match Abandoned", "Is Match Abandoned"),
        ("Club", "Club"),
        ("Referee Name", "Referee Name"),
        ("Is Referee U18?", "Is Referee U18?"),
        ("Submission Date", "Submission Date"),
        ("Report Submitted By", "Report Submitted By"),
    ]

    for label, key in field_order:
        value = fields.get(key, "")
        if value:
            lines.append(f"{label}: {value}")

    report_details = fields.get("Report Details", "")
    if report_details:
        lines.extend(["", "Report Details:", report_details])

    return "\n".join(lines).strip()


def parse_report_text(raw_text: str) -> Dict[str, object]:
    normalized = _normalize_whitespace(raw_text)
    fields = _extract_fields(normalized)
    structured_text = _build_structured_text(fields)
    return {
        "text": structured_text,
        "fields": fields,
    }
