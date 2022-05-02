#!/usr/bin/env python
import re
fp=open("parameter.txt",'r')
for i in fp:
    i=re.sub('\n','',i)
    if re.match("min_RNA_score=",i):
        a=re.match("min_RNA_score=",i)
        a=a.end()
        score=float(i[a:])
fp.close()
fp=open("sorted.best1",'r')
for i in fp:
    i=re.sub('\n','',i)
    j=i.split()
    if float(j[5])>score:
        print(i)
fp.close()
