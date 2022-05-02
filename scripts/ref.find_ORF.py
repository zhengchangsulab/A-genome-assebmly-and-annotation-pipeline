#!/usr/bin/env python
import re
cds={}
fp=open("cds.fa",'r')
for i in fp:
    i=re.sub('\n','',i)
    if re.match('>',i):
        name=i[1:]
    else:
        cds[name]=i
fp.close()
h={}
l=[]
fp=open("best2.gff3",'r')
for i in fp:
    i=re.sub('\n','',i)
    j=i.split()
    if j[2]=="gene":
        name=i
        if l!=[]:
            h[name1]=l
            l=[]
    else:
        name1=name
        l.append(i)
h[name1]=l
fp.close()
pseudo=[]
for i in cds.keys():
    string=cds[i]
    label=0
    if len(string)%3==0:
        for x in range(3,len(string)-3,3):
            if string[x:x+3]=="TAG" or string[x:x+3]=="TAA" or string[x:x+3]=="TGA":
                label=1
                break
    else:
        label=1
    if label==1:
        pseudo.append(i)
fp=open("best2_truegene.gff3",'w')
fp1=open("best2_pseudogene.gff3",'w')
for i in h.keys():
    j=i.split()
    if j[8] in pseudo:
        fp1.write(i+'\n')
        for x in h[i]:
            fp1.write(x+'\n')
    else:
        fp.write(i+'\n')
        for x in h[i]:
            fp.write(x+'\n')
fp.close()
fp1.close()
