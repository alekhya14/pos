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
for iter in range(0,1):
    f=open("/Users/alekhyagumidelli/Documents/csci_544/Homework2/train.pos",'r')
    for line in f:
        word=line.split()
        for i in range(0,len(word)):
            sub=word[i].split('/')
            if(sub[0] not in fc):
                for i in range(0,counter):
                    fc[sub[0]][class_count[i]]=0
                fc[sub[0]][sub[1]]=1
                index+=1
            else:
                maxi=0
                for i in range(0,counter):
                    #temp=ind[sub[0]]
                    if(fc[sub[0]][class_count[i]]>maxi):
                        max_class=class_count[i]
                        maxi=fc[sub[0]][class_count[i]]
                if(max_class is not sub[1]):
                    fc[sub[0]][max_class]-=1
                    fc[sub[0]][sub[1]]+=1
    f.close()
print(index)
w=csv.writer(open("/Users/alekhyagumidelli/Documents/csci_544/Homework2/pos/model.csv","w"))
for i in fc:
    maxi=0
    for j in range(1,counter):
        if(fc[i][class_count[j]]>maxi):
            maxi=fc[i][class_count[j]]
            max_class=class_count[j]          
    w.writerow([i,max_class])