from PyPDF2 import PdfFileReader, PdfFileWriter

pdf =  PdfFileReader("a7541en.pdf")

pdfwriter = PdfFileWriter()

for page_num in range(pdf.numPages):
    pdfwriter.addPage(pdf.getPage(page_num))
    password = "2022"
    pdfwriter.encrypt(password)
with open("newFile.pdf", 'wb') as f:
    pdfwriter.write(f)
    f.close()