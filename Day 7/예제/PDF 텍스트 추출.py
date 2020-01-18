import PyPDF2
import sys

# PDF파일을 바이너리 읽기모드로 열어 pdfFileObj에 저장
pdfFileObj = open(r'Day 7\예제\PDF examples\meetingminutes.pdf', 'rb')
input_file = open(sys.argv[1], 'rb')

# PdfFileReader 객체를 pdfReader에 저장
#pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader = PyPDF2.PdfFileReader(input_file)


# 문서에 있는 총 페이지 수는 pdfReader 객체의 numPages 속성에 저장되어 있음
print(pdfReader.numPages)

# PDF 파일의 페이지 중 첫번째 페이지를 얻는다
pageObj = pdfReader.getPage(0)

# page 객체에서 텍스트를 추출한다
print(pageObj.extractText())
