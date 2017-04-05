import csv
import os
import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
import nltk, sys

Path='C:\\Users\\Anamika\\Desktop\\test.csv'
message=[]
with open(Path,'r') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        message.append(row['message'].lower())
    print(message)
    print(len(message))
df = pd.read_csv(Path, encoding='latin-1')
df.head()
Path1='C:\\Users\\Anamika\\Desktop\\spam list.csv'
keywords=[]
with open(Path1,'r') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        keywords.append(row['keywords'])
    print(keywords)
    print(len(keywords))
df = pd.read_csv(Path1, encoding='latin-1')
df.head()
for i in range(0,len(message)):
    a=message[i]
    if set(keywords).intersection(a.split()):
        print('spam')
    else:
        print('ham')
