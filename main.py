import PyPDF2
import linecache

FILE_PATH = 'http://math.dge.toyota-ct.ac.jp/katsutani/lssn/2020/ba2/wkprntans/f2i/2i30ans18.pdf'

with open(FILE_PATH, "rb") as f:
    reader = PyPDF2.PdfFileReader(f)
    page = reader.getPage(0)
    text = page.extractText()

line = text.splitlines()
print(text)
print("あなたの18回目時点での正答数は"+line[7]+"問です。")
