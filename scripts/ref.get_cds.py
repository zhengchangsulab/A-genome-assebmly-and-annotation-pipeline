#!/usr/bin/env python
import re,sys
fp=open("parameter.txt",'r')
for i in fp:
    i=re.sub('\n','',i)
    if re.match('genome=',i):
        a=re.match('genome=',i)
        a=a.end()
        genome=i[a:]
fp.close()
gff3=sys.argv[1]
h={}
l=[]
fp=open(gff3,'r')
for i in fp:
    i=re.sub('\n','',i)
    j=i.split()
    if j[2]=="gene":
        name=j[8]
        if l!=[]:
            h[name1]=l
            l=[]
    else:
        if j[2]=="CDS":
            name1=name
            l.append(i)
h[name1]=l
fp.close()
genome_h={}
s=""
fp=open(genome,'r')
for i in fp:
    i=re.sub('\n','',i)
    if re.match('>',i):
        name=i[1:]
        if s!="":
            genome_h[name1]=s
            s=""
    else:
        name1=name
        s+=i.upper()
genome_h[name1]=s
fp.close()
def find_complementary(kmer):
    kmer=kmer[::-1]
    trantab=str.maketrans('ACGT','TGCA')
    string=kmer.translate(trantab)
    return(string)
for i in h.keys():
    cds=""
    for j in h[i]:
        a=j.split()
        strand=a[6]
        string=genome_h[a[0]][int(a[3])-1:int(a[4])]
        cds+=string
    if strand=='-':
        cds=find_complementary(cds)
    print('>'+i)
    print(cds)
