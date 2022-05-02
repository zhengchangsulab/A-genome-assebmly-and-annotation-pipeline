#!/usr/bin/env python
import re
h={}
l=[]
fp=open("final_truegene.gff3",'r')
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
for i in h.keys():
    print(i+';type=truegene')
    for x in h[i]:
        print(x)
notsupport=[]
fp=open("shortreads_notsupport.pseudogene",'r')
for i in fp:
    i=re.sub('\n','',i)
    notsupport.append(i)
fp.close()
h={}
l=[]
fp=open("final_pseudogene.gff3",'r')
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
for i in h.keys():
    if i in notsupport:
        print(i+';type=partial')
        for x in h[i]:
            print(x)
    else:
        j=i.split()
        j[2]="pseudogene"
        print(j[0]+'\t'+j[1]+'\t'+j[2]+'\t'+j[3]+'\t'+j[4]+'\t'+j[5]+'\t'+j[6]+'\t'+j[7]+'\t'+j[8]+';type=pseudogene')
        for x in h[i]:
            if x.split()[2]=="exon":
                print(x)
