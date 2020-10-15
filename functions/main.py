import flask
import requests
from bs4 import BeautifulSoup
import datetime
import PyPDF2
import linecache
import urllib.request
import os
from google.cloud import firestore

year = datetime.date.today().year
month = datetime.date.today().month
date = datetime.date.today().day

print(f'{year}/{month}/{date}')

root = os.environ['root']
print(root)

# Project ID is determined by the GCLOUD_PROJECT environment variable
db = firestore.Client()

def scape():
    for d in ['m','i']:
        res = requests.get(f'{root}wkprntans/index-l2{d}.html')
        soup = BeautifulSoup(res.text, 'html.parser')
        source = soup.find_all('a',text=f'{month}/{date}')
        links = [url.get('href') for url in source]
        if d=='m':
            m=links
        else:
            i=links
    print(m,i)
    return m,i

def correct(d):
    for n in d:
        num=n[4:8]
        no=int(n[11:13])
        url = f'{root}wkprntans/'+n
        savename = "/tmp/print.pdf"
        urllib.request.urlretrieve(url, savename)

        with open(savename, "rb") as f:
            reader = PyPDF2.PdfFileReader(f)
            page = reader.getPage(0)
            text = page.extractText()
            line = text.splitlines()
            try:
                result = int(line[9])
            except ValueError:
                print("First")
                result = None
        print(result)
        DB(num,result,no)
        os.remove('/tmp/print.pdf')
    return 0

def DB(num,result,no):
    setData = db.collection(num).document(str(no))
    last = no-1
    print(last)
    if last==0:
        pass
    else:
        db.collection(num).document(str(last)).update({u'score': result})
    setData.set({
        u'date': f'{year}/{month}/{date}',
        u'score': None
    }, merge=True)
    return 0

def main(request):
    m,i=scape()
    correct(m)
    correct(i)
    return flask.make_response('finish')