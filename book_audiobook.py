import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ""
        for page_num in range(reader.numPages):
            text += reader.getPage(page_num).extractText()
    return text

book_text = extract_text_from_pdf('aesops_fables.pdf')
print(book_text[:1000])  # print the first 1000 characters for a quick check
