#!/usr/bin/env python
import re
fp=open("parameter.txt",'r')
for i in fp:
    i=re.sub('\n','',i)
    if re.match("rna_splign=",i):
        a=re.match("rna_splign=",i)
        a=a.end()
        splign=i[a:]
fp.close()
splign_h={}
fp=open(splign,'r')
for i in fp:
    i=re.sub('\n','',i)
    j=i.split()
    if j[0]=='#':
        pass
    else:
        name=j[1][4:]
        if name not in splign_h.keys():
            l=[]
            l.append(i)
            splign_h[name]=l
        else:
            l=splign_h[name]
            l.append(i)
            splign_h[name]=l
fp.close()
fp1=open("best1",'w')
for i in splign_h.keys():
    number={}
    number1={}
    for y in splign_h[i]:
        y1=y.split()
        if y1[0] in number.keys():
            l=number[y1[0]]
            l.append(y)
            number[y1[0]]=l
        else:
            l=[]
            l.append(y)
            number[y1[0]]=l
    for y in number.keys():
        label=0
        for m in number[y]:
            m1=m.split()
            if m1[9]=="AG<exon>GT" or m1[9]=="AG<exon>GC":
                label=1
                break
        if label==1:
            number1[y]=number[y]
    max_identity=0
    if number1!={}:
        for y in number1.keys():
            map_len=0
            identity=0
            for z in number[y]:
                z1=z.split()
                map_len+=int(z1[4])
                if z1[3]=='-':
                    ide=0
                else:
                    ide=float(z1[3])
                identity+=ide*int(z1[4])
                ave_iden=round(identity/map_len,3)
            if ave_iden>max_identity:
                max_identity=ave_iden
                choose=y
                score=ave_iden
        isoform=[]
        for x in splign_h[i]:
            y=x.split()
            if y[0]==choose and y[7]!='-':
                contig=y[2][4:]
                start=min(int(y[7]),int(y[8]))
                end=max(int(y[7]),int(y[8]))
                if int(y[7])<int(y[8]):
                    string="+"
                else:
                    string="-"
                items=[contig,start,end,string]
                isoform.append(items)
        s=[]
        e=[]
        for x in isoform:
            s.append(x[1])
            e.append(x[2])
            fp1.write(str(x[1])+'-'+str(x[2])+',')
        start=min(s)
        end=max(e)
        fp1.write('\t'+x[0]+'\t'+str(start)+'\t'+str(end)+'\t'+x[3]+'\t'+str(score)+'\t'+i+'\t'+choose+'\n')
fp1.close()
