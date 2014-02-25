import collections
import csv
import json
import operator

class_count=["" for i in range(100)]
fc=collections.defaultdict(dict)
fin=collections.defaultdict(dict)
trin=collections.defaultdict(dict)
counter=1
index=1
temp=0
max_class=""
f=open("/Users/alekhyagumidelli/Documents/csci_544/Homework2/train.pos",'r')
for line in f:
    word=line.split()
    for i in range(0,len(word)):
        sub=word[i].split('/')
        if(sub[1] not in class_count):
            class_count[counter]=sub[1]
            counter+=1
f.close()
f=open("/Users/alekhyagumidelli/Documents/csci_544/Homework2/train.pos",'r')
for line in f:
    word=line.split()
    for i in range(0,len(word)):
        sub=word[i].split('/')
        if(i!=0):
            sub2=word[i-1].split('/')
        if(sub[1] not in fin):
            for j in range(0,counter):
                fin[sub[1]][class_count[j]]=0
            if(i!=0):
                fin[sub[1]][sub2[1]]=1
        else:
            fin[sub[1]][sub2[1]]+=1
w2=csv.writer(open("/Users/alekhyagumidelli/Documents/csci_544/Homework2/pos/model_tag.csv","w"))
for i in fin:
    for class_c,freq in fin[i].items():
        w2.writerow([i,class_c,freq])
            
