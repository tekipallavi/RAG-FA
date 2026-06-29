from pathlib import Path

import fitz

from src.splitter import parse_report_text


def _resolve_docpath(docpath):
    path = Path(docpath)
    candidates = []

    if path.is_absolute():
        candidates.append(path)
    else:
        candidates.extend([
            Path.cwd() / path,
            Path(__file__).resolve().parents[1] / path,
        ])

    if not path.is_absolute() and "fa-reports" in path.as_posix():
        corrected = Path(path.as_posix().replace("fa-reports", "fa_reports"))
        candidates.extend([
            Path.cwd() / corrected,
            Path(__file__).resolve().parents[1] / corrected,
        ])

    for candidate in candidates:
        if candidate.exists():
            return candidate

    return path


def load_pdfs(docpaths):
    docs = {}
    for docpath in docpaths:
        resolved_path = _resolve_docpath(docpath)
        if not resolved_path.exists():
            raise FileNotFoundError(f"no such file: '{docpath}'")

        doc = fitz.open(str(resolved_path))
        pages = [doc.load_page(i).get_text() for i in range(doc.page_count)]
        raw_text = "\n\n".join(pages)
        parsed = parse_report_text(raw_text)
        ## doc is a disctionary where the key is the file path and the value is the string extracted from the PDF file and parsed into structured text
        """
            Document Type: Extraordinary Incident Report

            Fixture: Thornton Rangers FC vs Millbrook United FC
            Competition: FA Vase
            Match Date: 2026-04-05
            Is Match Abandoned: No
            Club: Home Team
            Referee Name: Sarah Jennings
            Is Referee U18?: No
            Submission Date: 2026-04-06
            Report Submitted By: Sarah Jennings

            Report Details: Report details

        """
        docs[str(resolved_path)] = parsed["text"]
    return docs