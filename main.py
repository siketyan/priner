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

# Project ID is determined by the GCLOUD_PROJECT environment variable
db = firestore.Client()

def scape():
    for d in ['m','i']:
        res = requests.get(f'http://math.dge.toyota-ct.ac.jp/katsutani/lssn/2020/ba2/wkprntans/index-f2{d}.html')
        soup = BeautifulSoup(res.text, 'html.parser')
        source = soup.find_all('a',text=f'{month}/{date}')
        links = [url.get('href') for url in source]
        if d=='m':
            m=links
        else:
            i=links
    return m,i

def correct(d):
    for n in d:
        num=n[4:8]
        url = f'http://math.dge.toyota-ct.ac.jp/katsutani/lssn/2020/ba2/wkprntans/'+n
        savename = "/tmp/print.pdf"
        urllib.request.urlretrieve(url, savename)

        with open(savename, "rb") as f:
            reader = PyPDF2.PdfFileReader(f)
            page = reader.getPage(0)
            text = page.extractText()
            line = text.splitlines()
            result = line[7]
        print(result)
        DB(num,result)
        os.remove('/tmp/print.pdf')
    return 0

def DB(num,result):
    d=num[1:2]
    setData = db.collection(d).document(num)
    # Set the capital field
    setData.set({
        f'{year}/{month}/{date}': result
    }, merge=True)
    return 0

def main():
    m,i=scape()
    correct(m)
    correct(i)
    return 0