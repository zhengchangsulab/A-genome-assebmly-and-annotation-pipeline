#!/usr/bin/env python
import re
h={}
l=[]
fp=open("best2_pseudogene.gff3",'r')
for i in fp:
    i=re.sub('\n','',i)
    j=i.split()
    if j[2]=="gene":
        name=i
        if l!=[]:
            h[name1]=l
            l=[]
    else:
        name1=name
        l.append(i)
h[name1]=l
fp.close()
need_extend={}
fp=open("best2_pseudogene_need_extend",'r')
for i in fp:
    i=re.sub('\n','',i)
    j=i.split()
    l=[]
    for x in range(1,len(j)):
        l.append(j[x])
    need_extend[j[0]]=l
fp.close()
rna_exon=[]
fp=open("rna_based.gff3",'r')
for i in fp:
    i=re.sub('\n','',i)
    j=i.split()
    if j[2]=="exon":
        rna_exon.append(i)
fp.close()
fp1=open('pseudogene_part1.gff3','w')
fp2=open('extended_pseudogene.gff3','w')
for i in h.keys():
    j=i.split()
    new_values=h[i]
    if j[8] in need_extend.keys():
        extend=need_extend[j[8]]
        for x in extend:
            if re.match('start-',x):
                a=re.match('start-',x)
                a=a.end()
                number=int(x[a:])
                if j[6]=='+':
                    change=j[3]
                    j[3]=int(j[3])-number
                else:
                    change=j[4]
                    j[4]=int(j[4])+number
                for b in new_values:
                    y=b.split()
                    if y[3]==change:
                        y[3]=str(j[3])
                    elif y[4]==change:
                        y[4]=str(j[4])
                    else:
                        pass
                    st=y[0]+'\t'+y[1]+'\t'+y[2]+'\t'+y[3]+'\t'+y[4]+'\t'+y[5]+'\t'+y[6]+'\t'+y[7]+'\t'+y[8]
                    new_values[new_values.index(b)]=st
            elif re.match('stop-',x):
                a=re.match('stop-',x)
                a=a.end()
                number=int(x[a:])
                if j[6]=='+':
                    change=j[4]
                    j[4]=int(j[4])+number
                else:
                    change=j[3]
                    j[3]=int(j[3])-number
                for b in new_values:
                    y=b.split()
                    if y[3]==change:
                        y[3]=str(j[3])
                    elif y[4]==change:
                        y[4]=str(j[4])
                    else:
                        pass
                    st=y[0]+'\t'+y[1]+'\t'+y[2]+'\t'+y[3]+'\t'+y[4]+'\t'+y[5]+'\t'+y[6]+'\t'+y[7]+'\t'+y[8]
                    new_values[new_values.index(b)]=st
            else:
                a=re.search(':',x).end()
                newstring=x[a:]
                b=re.search('-',newstring)
                b1=b.start()
                start=int(newstring[:b1])
                b2=b.end()
                end=int(newstring[b2:])
                for m in rna_exon:
                    n=m.split()
                    if n[0]==j[0] and n[6]==j[6] and int(n[3])>=start and int(n[4])<=end:
                        new_values.append(m)
                        m1=m.replace('exon','CDS')
                        new_values.append(m1)
        fp2.write(j[0]+'\t'+j[1]+'\t'+j[2]+'\t'+str(j[3])+'\t'+str(j[4])+'\t'+j[5]+'\t'+j[6]+'\t'+j[7]+'\t'+j[8]+'\n')
        for c in new_values:
            fp2.write(c+'\n')
    else:
        fp1.write(i+'\n')
        for x in h[i]:
            fp1.write(x+'\n')
fp1.close()
fp2.close()
