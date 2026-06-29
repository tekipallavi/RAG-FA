import fitz

def load_pdfs(docpaths):
    docs = {}
    for docpath in docpaths:
        doc = fitz.open(docpath)
        pages = []
        pages = [doc.load_page(i).get_text() for i in range(doc.page_count)]
        docs[docpath] = pages
    return docs