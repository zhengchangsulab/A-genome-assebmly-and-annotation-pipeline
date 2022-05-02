#!/usr/bin/env python
import re
cds={}
annotation={}
fp=open("rna_support.gff3",'r')
for i in fp:
    i=re.sub('\n','',i)
    j=i.split()
    if j[2]=="gene":
        genes=i
        anno_l=[]
        a=re.match('ID=',j[8])
        a=a.end()
        b=re.search(';',j[8])
        b=b.start()
        name=j[8][a:b]
        l=[]
    else:
        anno_l.append(i)
        annotation[genes]=anno_l
        if j[2]=="CDS":
            for x in range(int(j[3]),int(j[4])+1,1):
                l.append(x)
                cds[name]=(l,j[6])
fp.close()
new_h={}
fp=open("new_old.name",'r')
for i in fp:
    i=re.sub('\n','',i)
    j=i.split()
    new_h[j[2]]=j[1]
fp.close()
orf={}
fp=open("rna_uniq_good_orf.fa",'r')
for i in fp:
    i=re.sub('\n','',i)
    if re.match('>',i):
        name=i[1:]
    else:
        orf[name]=i
fp.close()
cds_h={}
fp=open("rna_uniq_cds.fa",'r')
for i in fp:
    i=re.sub('\n','',i)
    if re.match('>',i):
        name=i[1:]
    else:
        cds_h[name]=i
fp.close()
new_cds={}
for i in cds.keys():
    new_l=[]
    orf_string=orf[new_h[i]]
    a=re.search('-',new_h[i])
    a=a.start()
    cds_string=cds_h[new_h[i][:a]]
    b=re.search(orf_string,cds_string)
    b1=b.start()
    b2=b.end()
    if cds[i][1]=="+":
        for x in range(b1,b2,1):
            new_l.append(cds[i][0][x])
        new_cds[i]=new_l
    else:
        ll=cds[i][0]
        ll.reverse()
        for x in range(b1,b2,1):
            new_l.append(ll[x])
        new_l.reverse()
        new_cds[i]=new_l
final_cds={}
for i in new_cds.keys():
    n=0
    l=[]
    for j in new_cds[i]:
        if n==0:
            start=j
        if j==start+n:
            end=j
        else:
            n=0
            l.append((start,end))
            start=j
        n+=1
    l.append((start,end))
    final_cds[i]=l
for i in annotation.keys():
    print(i)
    j=i.split()
    a=re.match('ID=',j[8])
    a=a.end()
    b=re.search(';',j[8])
    b=b.start()
    name=j[8][a:b]
    for x in annotation[i]:
        y=x.split()
        if y[2]!="CDS":
            print(x)
    l=final_cds[name]
    number=1
    for i in l:
        print(j[0]+'\t'+j[1]+'\t'+'CDS'+'\t'+str(i[0])+'\t'+str(i[1])+'\t'+j[5]+'\t'+j[6]+'\t'+'0'+'\t'+"ID="+name+".CDS"+str(number)+";Parent="+name+".mRNA")
        number+=1
