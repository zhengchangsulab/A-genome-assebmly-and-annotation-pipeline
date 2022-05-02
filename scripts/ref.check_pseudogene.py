#!/usr/bin/env python
import re
fp=open("parameter.txt",'r')
for i in fp:
    i=re.sub('\n','',i)
    if re.match('bed_file=',i):
        a=re.match('bed_file=',i)
        a=a.end()
        notsupport=i[a:]
fp.close()
ll=[]
fp=open(notsupport,'r')
for i in fp:
    i=re.sub('\n','',i)
    j=i.split()
    if int(j[1])==0:
        j[1]=1
    j[2]=int(j[2])-1
    l1=[j[0],int(j[1]),int(j[2])]
    ll.append(l1)
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
        if j[2]=='CDS':
            l.append(i)
h[name1]=l
fp.close()
for i in h.keys():
    label=0
    for j in h[i]:
        a=j.split()
        chrname=a[0]
        start=int(a[3])
        end=int(a[4])
        for x in ll:
            if chrname==x[0]:
                if end<x[1] or start>x[2]:
                    pass
                else:
                    label=1
                    break
    if label==1:
        print(i)

