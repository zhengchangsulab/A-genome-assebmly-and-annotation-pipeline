#!/usr/bin/env python
import re
h={}
fp=open("test.fa",'r')
for i in fp:
    i=re.sub('\n','',i)
    if re.match('>',i):
        name=i[1:]
    else:
        h[name]=i
fp.close()
problem=[]
for i in h.keys():
    string=h[i]
    if re.search('NN',string):
        problem.append(i)
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
fp=open("test",'r')
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
    j=i.split()
    if j[8] not in problem:
        print(i)
        for x in extend[i]:
            print(x)
    else:
        for a in best2.keys():
            y=a.split()
            if j[8]==y[8]:
                print(a)
                for b in best2[a]:
                    print(b)

