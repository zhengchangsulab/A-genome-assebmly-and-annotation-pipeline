#!/usr/bin/env python
import re
first={}
fp=open("total.support",'r')
for i in fp:
    i=re.sub('\n','',i)
    a=re.search('-',i)
    a1=a.end()
    a2=a.start()
    name=i[:a2]
    length=int(i[a1:])
    if name not in first.keys():
        first[name]=length
    else:
        if length>first[name]:
            first[name]=length
fp.close()
fp1=open("new_old.name",'w')
anno={}
fp=open("rna_uniq1.gff3",'r')
for i in fp:
    i=re.sub('\n','',i)
    j=i.split()
    if j[2]=="gene":
        name=i
        l=[]
    else:
        l.append(i)
        anno[name]=l
fp.close()
n=0
for i in first.keys():
    n+=1
    for x in anno.keys():
        y=x.split()
        if y[8]==i:
            new="ID=Gal"+str(n)+";"
            fp1.write(i+'\t'+i+'-'+str(first[i])+'\t'+"Gal"+str(n)+'\n')
            print(y[0]+'\t'+y[1]+'\t'+y[2]+'\t'+y[3]+'\t'+y[4]+'\t'+y[5]+'\t'+y[6]+'\t'+y[7]+'\t'+new)
            for a in anno[x]:
                b=a.replace(i[3:],"Gal"+str(n))
                print(b)
fp1.close()
