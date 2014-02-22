import collections
class_count=["" for i in range(100)]
fc=collections.defaultdict(dict)
counter=1
f=open("/Users/alekhyagumidelli/Documents/csci_544/Homework2/train.pos",'r')
for line in f:
    word=line.split()
    for i in range(0,len(word)):
        sub=word[i].split('/')
        if(sub[1] not in fc):
            fc[1]=sub[1]
            counter+=1
print(fc[1])
