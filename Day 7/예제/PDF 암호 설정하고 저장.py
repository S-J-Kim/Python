# PDF 파일 불러와서 비밀번호 설정 후 저장
import PyPDF2

pdfFile = open(r'Day 7\예제\PDF examples\encrypted.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFile)

pdfWriter = PyPDF2.PdfFileWriter()

# 암호를 입력하지 않으면 에러가 발생합니다.(암호:rosebud)
pdfReader.decrypt('rosebud')

# 새로운 PDF를 만들어 그대로 복사
for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))

# 새로운 암호를 적어줌
pdfWriter.encrypt('hongik')

resultPDF = open('encrypted2.pdf', 'wb')
pdfWriter.write(resultPDF)
resultPDF.close()
