docpaths = ['./data/FTO0000377 - Pending Charge Letter.pdf', './data/FTO0000843 - Pending Charge Letter.pdf']
from src.loader import load_pdfs

def main():
    loaded_docs = load_pdfs(docpaths)
    #print(loaded_docs)

if __name__ == "__main__":
    main()