import collections
class_count=["" for i in range(100)]
fc=collections.defaultdict(dict)
counter=1
max_class=""
f=open("/Users/alekhyagumidelli/Documents/csci_544/Homework2/train.pos",'r')
for line in f:
    word=line.split()
    for i in range(0,len(word)):
        sub=word[i].split('/')
        if(sub[1] not in class_count):
            class_count[counter]=sub[1]
            counter+=1
for iter in range(0,5):
    f=open("/Users/alekhyagumidelli/Documents/csci_544/Homework2/train.pos",'r')
    for line in f:
        word=line.split()
        for i in range(0,len(word)):
            sub=word[i].split('/')
            if(sub[0] not in fc):
                for i in range(0,counter):
                    fc[sub[0]][class_count[i]]=0
                fc[sub[0]][sub[1]]=1
            else:
                max=0
                for i in range(0,counter-1):
                    if(fc[sub[0]][class_count[i]]>max):
                        max_class=class_count[i]
                        max=fc[sub[0]][class_count[i]]
                if(max_class is not sub[1]):
                    fc[sub[0]][max_class]-=1
                    fc[sub[0]][sub[1]]+=1
    f.close()

