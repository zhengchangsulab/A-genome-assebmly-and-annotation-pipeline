#!/usr/bin/env python
import re
ref_h=[]
fp=open("final_ref_gene.gff3",'r')
for i in fp:
    i=re.sub('\n','',i)
    j=i.split()
    if j[2]=="gene" or j[2]=="pseudogene":
        ref_h.append(i)
fp.close()
rna_h={}
l=[]
fp=open("rna_based.gff3",'r')
for i in fp:
    i=re.sub('\n','',i)
    j=i.split()
    if j[2]=="gene":
        name=i
        if l!=[]:
            rna_h[name1]=l
            l=[]
    else:
        name1=name
        l.append(i)
rna_h[name1]=l
fp.close()
new_rna_h={}
for i in rna_h.keys():
    j=i.split()
    start=int(j[3])
    end=int(j[4])
    label=0
    for x in ref_h:
        y=x.split()
        s=int(y[3])
        e=int(y[4])
        if j[0]==y[0]: #and j[6]==y[6]:
            if e<start or s>end:
                pass
            else:
                label=1
                break
    if label==0:
        new_rna_h[i]=rna_h[i]
for i in new_rna_h.keys():
    print(i)
    for a in new_rna_h[i]:
        print(a)
