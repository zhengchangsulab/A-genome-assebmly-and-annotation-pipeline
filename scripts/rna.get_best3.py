#!/usr/bin/env python
import re
first={}
fp=open("diamond.first",'r')
for i in fp:
    i=re.sub('\n','',i)
    j=i.split()
    a=re.search('-',j[0])
    a1=a.end()
    a2=a.start()
    name=j[0][:a2]
    length=int(j[0][a1:])
    l=[length,j[0],j[1]]
    if name not in first.keys():
        first[name]=l
    else:
        if length>first[name][0]:
            first[name]=l
fp.close()
fp=open("new_old.name",'w')
for i in first.keys():
    fp.write(i+'\t'+first[i][1]+'\t'+first[i][2]+'\n')
fp.close()
anno={}
fp=open("rna_uniq1.gff3",'r')
for i in fp:
    i=re.sub('\n','',i)
    j=i.split()
    if j[2]=="gene":
        name=i
        l=[]
    else:
        l.append(i)
        anno[name]=l
fp.close()
for i in first.keys():
    for x in anno.keys():
        y=x.split()
        if y[8]==i:
            new="ID="+first[i][2]+";type=nr_support"
            print(y[0]+'\t'+y[1]+'\t'+y[2]+'\t'+y[3]+'\t'+y[4]+'\t'+y[5]+'\t'+y[6]+'\t'+y[7]+'\t'+new)
            for a in anno[x]:
                b=a.replace(i[3:],first[i][2])
                print(b)
