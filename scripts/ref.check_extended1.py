#!/usr/bin/env python
import re
fp=open("parameter.txt",'r')
for i in fp:
    i=re.sub('\n','',i)
    if re.match('genome=',i):
        a=re.match('genome=',i)
        a=a.end()
        genome=i[a:]
fp.close()
h={}
fp=open(genome,'r')
for i in fp:
    i=re.sub('\n','',i)
    if re.match('>',i):
        name=i[1:]
        s=0
    else:
        s+=len(i)
        h[name]=s
fp.close()
best2={}
fp=open("best2.gff3",'r')
for i in fp:
    i=re.sub('\n','',i)
    j=i.split()
    if j[2]=="gene":
        name=i
        l=[]
    else:
        l.append(i)
        best2[name]=l
fp.close()
extend={}
fp=open("extended_pseudogene.gff3",'r')
for i in fp:
    i=re.sub('\n','',i)
    j=i.split()
    if j[2]=="gene":
        name=i
        l=[]
    else:
        l.append(i)
        extend[name]=l
fp.close()
for i in extend:
    n=1
    j=i.split()
    s=re.match("ID=",j[8])
    s=s.end()
    e=re.search(";",j[8])
    e=e.start()
    gene=j[8][s:e]
    if int(j[3])<0 or int(j[4])>h[j[0]]:
        for x in best2:
            y=x.split()
            if j[8]==y[8]:
                print(x)
                for a in best2[x]:
                    print(a)
                break
    else:
        print(i)
        for b in extend[i]:
            c=b.split()
            if c[2]=="mRNA":
                print(b)
            elif c[2]=="exon":
                print(c[0]+'\t'+c[1]+'\t'+c[2]+'\t'+c[3]+'\t'+c[4]+'\t'+c[5]+'\t'+c[6]+'\t'+c[7]+'\t'+"ID="+gene+".exon"+str(n)+";Parent="+gene+".mRNA")
            else:
                print(c[0]+'\t'+c[1]+'\t'+c[2]+'\t'+c[3]+'\t'+c[4]+'\t'+c[5]+'\t'+c[6]+'\t'+c[7]+'\t'+"ID="+gene+".CDS"+str(n)+";Parent="+gene+".mRNA")
                n+=1
