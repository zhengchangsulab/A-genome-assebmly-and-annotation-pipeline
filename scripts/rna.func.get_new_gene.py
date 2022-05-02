#!/usr/bin/env python
import re
bacteria=[]
fp=open("nr_support.genefunction",'r')
for i in fp:
    i=re.sub('\n','',i)
    j=i.split()
    if j[-1]=="bacteria":
        bacteria.append(j[0][1:])
fp.close()
remove=[]
nr={}
fp=open("first.txt",'r')
for i in fp:
    i=re.sub('\n','',i)
    j=i.split()
    if j[1] in bacteria:
        remove.append(j[0][:-5])
    else:
        nr[j[0][:-5]]=j[1]
fp.close()
h={}
fp=open("rna_support5.gff3",'r')
for i in fp:
    i=re.sub('\n','',i)
    j=i.split()
    if j[2]=="gene":
        name=i
        l=[]
    else:
        l.append(i)
        h[name]=l
fp.close()
for i in h.keys():
    j=i.split()
    if j[8][3:] in remove:
        pass
    elif j[8][3:] in nr:
        new=i.replace(j[8][3:],nr[j[8][3:]])+";type=nr_support"
        print(new)
        for x in h[i]:
            new=x.replace(j[8][3:],nr[j[8][3:]])
            print(new)
    else:
        new=i+";type=novel"
        print(new)
        for x in h[i]:
            print(x)
