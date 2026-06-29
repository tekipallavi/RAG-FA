from src.loader import load_pdfs


docpaths = ['./output/fa_reports/EI_Report_01.pdf', './output/fa_reports/EI_Report_02.pdf']


def main():
    loaded_docs = load_pdfs(docpaths)
    print(loaded_docs)
    return loaded_docs


if __name__ == "__main__":
    main()