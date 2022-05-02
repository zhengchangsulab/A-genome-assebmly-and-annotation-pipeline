#!/usr/bin/env python
import re
fp=open("parameter.txt",'r')
for i in fp:
    i=re.sub('\n','',i)
    if re.match('non_coding=',i):
        a=re.match('non_coding=',i)
        a=a.end()
        cmscan=i[a:]
fp.close()
h={}
fp=open(cmscan,'r')
for i in fp:
    i=re.sub('\n','',i)
    j=i.split()
    if len(j)>=2:
        if j[0]=="Query:":
            name=j[1]
            l=[]
        else:
            if j[1]=='!' and j[9]=='cm':
                s=min(int(j[6]),int(j[7]))
                e=max(int(j[6]),int(j[7]))
                l.append([s,e,j[8],j[5],j[2]])
                h[name]=l
fp.close()
h1={}
fp=open("rna_uniq.gff3",'r')
for i in fp:
    i=re.sub('\n','',i)
    j=i.split()
    if j[2]=="gene":
        name=i
        l=[]
    else:
        l.append(i)
        h1[name]=l
fp.close()
for i in h1.keys():
    i=re.sub('\n','',i)
    j=i.split()
    start=int(j[3])
    end=int(j[4])
    label=0
    if j[0] in h.keys():
        for y in h[j[0]]:
            s=y[0]
            e=y[1]
            if e<start or s>end:
                pass
            else:
                label=1
                break
        if label==0:
            print(i)
            for x in h1[i]:
                print(x)
    else:
        print(i)
        for x in h1[i]:
            print(x)
