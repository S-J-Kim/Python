# 암호걸린 PDF 파일 불러오기
import PyPDF2

pdfFile = open(r'Day 7\예제\PDF examples\encrypted.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFile)

pdfWriter = PyPDF2.PdfFileWriter()

# 암호를 입력하지 않으면 에러가 발생합니다.(암호:rosebud)
pdfReader.decrypt('rosebud')

pdfReader.numPages

print(pdfReader.numPages,"페이지")

print("=======================================================")

pageObj = pdfReader.getPage(0)

pageObj.extractText()

print(pageObj.extractText())
