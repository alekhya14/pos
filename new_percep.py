import collections
import csv
import json
import operator

class_count=["" for i in range(100)]
fc=collections.defaultdict(dict)
sorted_fc=collections.defaultdict(dict)
fin=collections.defaultdict(dict)
trin=collections.defaultdict(dict)
sum_class=[0 for i in range(50)]
counter=1
index=1
correct=0
wrong=0
temp=0
max_class=""
f=open("/Users/alekhyagumidelli/Documents/csci_544/Homework2/train.pos",'r')
for line in f:
    word=line.split()
    for i in range(1,len(word)):
        sub=word[i].split('/')
        if(sub[1] not in class_count):
            class_count[counter]=sub[1]
            counter+=1
f.close()
for fi in range(0,15):
    print "iter:%d" %(fi)
    f=open("/Users/alekhyagumidelli/Documents/csci_544/Homework2/pos/train",'r')
    for line in f:
        sum_class=[0 for i in range(50)]
        word=line.split()
        tag=word[0]
        maxi=-1
        for j in range(0,counter):
            for i in range(1,len(word)):    
                if(word[i] not in fin):
                    for x in range(0,counter):
                        fin[word[i]][class_count[x]]=0
                    sum_class[j]+=0
                else:
                    sum_class[j]+=fin[word[i]][class_count[j]]
            if(sum_class[j]>maxi):
                maxi=sum_class[j]
                result=class_count[j]
        if(result!=tag):
            for i in range(1,len(word)):
                fin[word[i]][tag]+=1
                fin[word[i]][result]-=1
    f.close()
f=open("/Users/alekhyagumidelli/Documents/csci_544/Homework2/pos/tt",'r')
for line in f:
    sum_class=[0 for i in range(50)]
    word=line.split()
    maxi=-1
    for j in range(0,counter):
        for i in range(1,len(word)):
            if(word[i] not in fin):
                    for x in range(0,counter):
                        fin[word[i]][class_count[x]]=0
                    sum_class[j]+=0
                    if(word[i][0].isupper()):
                        if(word[i][-1:0]=='s'):
                            fin[word[i]]['NNS']=1
                        else:
                            fin[word[i]]['NN']=1
                    elif(word[i][:2]=="un"):
                        fin[word[i]]['JJ']=1
                    elif((word[i][-4:]=="ing.") or (word[i][-3:]=="ing")):
                        fin[word[i]]['VBG']=1
            else:
                sum_class[j]+=fin[word[i]][class_count[j]]
        if(sum_class[j]>maxi):
            maxi=sum_class[j]
            result=class_count[j]
    if(result==word[0]):
        correct+=1
    else:
        wrong+=1
print correct
print wrong