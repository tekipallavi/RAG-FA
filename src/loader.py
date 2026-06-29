from pathlib import Path

import fitz


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
        docs[str(resolved_path)] = pages
    return docs