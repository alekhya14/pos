import collections
import csv
import json
import operator
count=0
correct=0
fc=collections.defaultdict(dict)
for key,val in csv.reader(open("/Users/alekhyagumidelli/Documents/csci_544/Homework2/pos/model.csv","r")):
    fc[key]=val
for x in fc:
    print(x)
    print fc[x]
f=open("/Users/alekhyagumidelli/Documents/csci_544/Homework2/train.pos",'r')
for line in f:
    word=line.split()
    for i in range(0,len(word)):
        sub=word[i].split('/')
        result=fc[sub[0]]
        if(result!=sub[1]):
            print result
            print sub[1]
            count+=1
        else:
            correct+=1
print count
print fc["then-dress"]
print fc["Improving"]
print correct