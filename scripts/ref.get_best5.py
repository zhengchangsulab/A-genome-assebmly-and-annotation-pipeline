#!/usr/bin/env python
import re
h={}
fp=open("ref_based1.gff3",'r')
for i in fp:
    i=re.sub('\n','',i)
    j=i.split()
    if j[2]=="gene" or j[2]=="pseudogene":
        name=i
        l=[]
    else:
        l.append(i)
        h[name]=l
fp.close()
fp1=open("ref_true_gene.gff3",'w')
fp2=open("ref_pseudogene.gff3",'w')
for i in h.keys():
    j=i.split()
    if j[2]=="gene":
        fp1.write(i+'\n')
        for x in h[i]:
            fp1.write(x+'\n')
    else:
        fp2.write(i+'\n')
        for x in h[i]:
            if re.search('.mRNA',x):
                a=re.search('.mRNA',x).start()
                fp2.write(x[:a]+'\n')
            else:
                fp2.write(x+'\n')
fp1.close()
fp2.close()

