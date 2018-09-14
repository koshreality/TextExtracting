from pdfparser import PDFParser

if __name__ == '__main__':
    pdf_parser = PDFParser()
    pdf_parser.parse(r'D:\Test.pdf')
    print(pdf_parser.get_processed_stems())
