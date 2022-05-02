#!/usr/bin/env python
import re
gene={}
cds={}
fp=open("rna_support1.gff3",'r')
for i in fp:
    i=re.sub('\n','',i)
    j=i.split()
    if j[2]=="gene":
        alllist=[]
        cdslist=[]
        name=i
    else:
        alllist.append(i)
        gene[name]=alllist
        if j[2]=="CDS":
            cdslist.append(i)
        cds[name]=cdslist
fp.close()
for i in gene.keys():
    print(i)
    n=1
    j=i.split()
    for x in gene[i]:
        y=x.split()
        if y[2]!="exon":
            print(x)
        else:
            for a in cds[i]:
                b=a.split()
                if y[3]==b[3] or y[4]==b[4] or (int(b[3])>int(y[3]) and int(b[4])<int(y[4])):
                    new=y[0]+'\t'+y[1]+'\t'+y[2]+'\t'+y[3]+'\t'+y[4]+'\t'+y[5]+'\t'+y[6]+'\t'+y[7]+'\t'+j[8][:-1]+'.exon'+str(n)+';Parent='+j[8][3:-1]+'.mRNA'
                    print(new)
                    n+=1
                    break

                
