# coding: utf-8
import nltk
import os
import csv

from nltk.corpus import stopwords
stopWords = set(stopwords.words('french'))

from bs4 import BeautifulSoup
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '../data/data_janvier_fevrier_2017.html')


dataRaw = open(filename, encoding="utf8")

soup = BeautifulSoup(dataRaw, 'html.parser')

dataArray = soup.findAll('tr')
reportArray = []

for k in dataArray:
    temp = k.find_all("td")
    if len(temp) >= 7:
        reportArray.append(temp[6].string)

tokenizer = nltk.RegexpTokenizer(r'\w+')

reports = ""
for report in reportArray:
    reports += report

tokens = []
words = tokenizer.tokenize(reports)
for w in words:
    if w not in stopWords:
        tokens.append(w)


freq = nltk.FreqDist(tokens)
 


fname =  os.path.join(dirname, '../data/tokens.csv')
file = open(fname, "w")

try:
    writer = csv.writer(file, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Mots", "Occurences"])
    for key,val in freq.items():
        writer.writerow((str(key),val))

finally:
    file.close()
