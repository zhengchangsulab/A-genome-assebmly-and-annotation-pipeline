#!/usr/bin/env python
import re
n=0
fp=open("best1.greater0.985.sort",'r')
for i in fp:
    j=i.split()
    if n==0:
        n=1
        chr_name=j[1]
        start=int(j[2])
        end=int(j[3])
        string=j[4]
        iden=float(j[5])
        gene=j[6]
        exon=j[0].split(',')
        exon.remove('')
    else:
        if j[1]==chr_name and j[4]==string and int(j[2])<=end:
            if float(j[5])>iden:
                iden=float(j[5])
                start=int(j[2])
                end=int(j[3])
                gene=j[6]
                exon=j[0].split(',')
                exon.remove('')
        else:
            print(chr_name+'\t'+'RNAseq'+'\t'+'gene'+'\t'+str(start)+'\t'+str(end)+'\t'+'.'+'\t'+string+'\t'+'.'+'\t'+"ID="+gene)
            print(chr_name+'\t'+'RNAseq'+'\t'+'mRNA'+'\t'+str(start)+'\t'+str(end)+'\t'+'.'+'\t'+string+'\t'+'.'+'\t'+"ID="+gene+".mRNA;Parent="+gene)
            l1=[]
            for x in exon:
                a=re.search('-',x)
                a1=a.start()
                a2=a.end()
                fi=int(x[:a1])
                en=int(x[a2:])
                l1.append((fi,en))
            num=0
            for x in sorted(l1):
                num+=1
                print(chr_name+'\t'+'RNAseq'+'\t'+'exon'+'\t'+str(x[0])+'\t'+str(x[1])+'\t'+'.'+'\t'+string+'\t'+'.'+'\t'+"ID="+gene+".exon"+str(num)+";Parent="+gene+".mRNA")
                print(chr_name+'\t'+'RNAseq'+'\t'+'CDS'+'\t'+str(x[0])+'\t'+str(x[1])+'\t'+'.'+'\t'+string+'\t'+'0'+'\t'+"ID="+gene+".CDS"+str(num)+";Parent="+gene+".mRNA")
            chr_name=j[1]
            start=int(j[2])
            end=int(j[3])
            string=j[4]
            iden=float(j[5])
            gene=j[6]
            exon=j[0].split(',')
            exon.remove('')
print(chr_name+'\t'+'RNAseq'+'\t'+'gene'+'\t'+str(start)+'\t'+str(end)+'\t'+'.'+'\t'+string+'\t'+'.'+'\t'+"ID="+gene)
print(chr_name+'\t'+'RNAseq'+'\t'+'mRNA'+'\t'+str(start)+'\t'+str(end)+'\t'+'.'+'\t'+string+'\t'+'.'+'\t'+"ID="+gene+".mRNA;Parent="+gene)
l1=[]
for x in exon:
    a=re.search('-',x)
    a1=a.start()
    a2=a.end()
    fi=int(x[:a1])
    en=int(x[a2:])
    l1.append((fi,en))
num=0
for x in sorted(l1):
    num+=1
    print(chr_name+'\t'+'RNAseq'+'\t'+'exon'+'\t'+str(x[0])+'\t'+str(x[1])+'\t'+'.'+'\t'+string+'\t'+'.'+'\t'+"ID="+gene+".exon"+str(num)+";Parent="+gene+".mRNA")
    print(chr_name+'\t'+'RNAseq'+'\t'+'CDS'+'\t'+str(x[0])+'\t'+str(x[1])+'\t'+'.'+'\t'+string+'\t'+'0'+'\t'+"ID="+gene+".CDS"+str(num)+";Parent="+gene+".mRNA")
