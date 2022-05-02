#!/usr/bin/env python
import re,sys
genome=sys.argv[1]
h={}
s=""
fp=open(genome,'r')
for i in fp:
    i=re.sub('\n','',i)
    if re.match('>',i):
        a=re.search('_np',i)
        a=a.start()
        name=i[:a]
        if s!="":
            h[name1]=s
            s=""
    else:
        name1=name
        s+=i.upper()
h[name1]=s
fp.close()
for i in h.keys():
    print(i)
    print(h[i])
