import flask
import PyPDF2
import linecache
import urllib.request
import os

def correct(request):
    url = 'http://math.dge.toyota-ct.ac.jp/katsutani/lssn/2020/ba2/wkprntans/f2i/2i30ans18.pdf'
    savename = "/tmp/print.pdf"
    urllib.request.urlretrieve(url, savename)

    with open(savename, "rb") as f:
        reader = PyPDF2.PdfFileReader(f)
        page = reader.getPage(0)
        text = page.extractText()
    line = text.splitlines()
    result = line[7]
    os.remove('/tmp/print.pdf')
    return flask.make_response(flask.jsonify(result))