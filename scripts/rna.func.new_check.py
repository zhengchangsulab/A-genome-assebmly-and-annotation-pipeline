#!/usr/bin/env python
import re
n=0
l=[]
fp=open("novel_gene",'r')
for i in fp:
    i=re.sub('\n','',i)
    j=i.split()
    if n==0:
        start=int(j[3])
        end=int(j[4])
        chrname=j[0]
        l.append(i)
    else:
        if j[0]==chrname and int(j[3])>=start and int(j[4])<=end:
            pass
        else:
            l.append(i)
            start=int(j[3])
            end=int(j[4])
            chrname=j[0]
    n=1
fp.close()
h={}
fp=open("rna_support6.gff3",'r')
for i in fp:
    i=re.sub('\n','',i)
    j=i.split()
    if j[2]=="gene":
        name=i
        ll=[]
    else:
        ll.append(i)
        h[name]=ll
fp.close()
for i in h.keys():
    if re.search("type=nr_support",i):
        print(i)
        for x in h[i]:
            print(x)
    else:
        if i in l:
            print(i)
            for x in h[i]:
                print(x)

