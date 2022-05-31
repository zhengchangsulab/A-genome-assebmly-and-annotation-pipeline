#!/usr/bin/env python
import re
h={}
fp=open("rna_support2.gff3",'r')
for i in fp:
    i=re.sub('\n','',i)
    j=i.split()
    if j[2]=='gene':
        name=i
        l=[]
    else:
        l.append(i)
        h[name]=l
fp.close()
for i in h.keys():
    j=i.split()
    first=[]
    end=[]
    for x in h[i]:
        y=x.split()
        if y[2]=='exon':
            first.append(y[3])
            end.append(y[4])
    if first!=[]:
        print(j[0]+'\t'+j[1]+'\t'+j[2]+'\t'+first[0]+'\t'+end[-1]+'\t'+j[5]+'\t'+j[6]+'\t'+j[7]+'\t'+j[8])
        for x in h[i]:
            y=x.split()
            if y[2]=='mRNA':
                print(y[0]+'\t'+y[1]+'\t'+y[2]+'\t'+first[0]+'\t'+end[-1]+'\t'+y[5]+'\t'+y[6]+'\t'+y[7]+'\t'+y[8])
            else:
                print(x)
