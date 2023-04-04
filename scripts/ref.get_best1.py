#!/usr/bin/env python
import re
fp=open("parameter.txt",'r')
for i in fp:
    i=re.sub('\n','',i)
    if re.match('ref_cds_name=',i):
        a=re.match('ref_cds_name=',i)
        a=a.end()
        cds=i[a:]
    if re.match('ref_splign=',i):
        a=re.match('ref_splign=',i)
        a=a.end()
        splign=i[a:]
fp.close()
h={}
fp=open(cds,'r')
for i in fp:
    i=re.sub('\n','',i)
    if re.match('>',i):
        j=i.split()
        name=j[1].replace('=','-')[1:-1]
        h[j[0][1:]]=name
fp.close()
gene_splign={}
number_splign={}
fp=open(splign,'r')
for i in fp:
    i=re.sub('\n','',i)
    j=i.split()
    if j[0]=='#':
        pass
    else:
        if j[0] not in number_splign.keys():
            l=[]
            l.append(i)
            number_splign[j[0]]=l
        else:
            l=number_splign[j[0]]
            l.append(i)
            number_splign[j[0]]=l
        x=h[j[1]]
        if x in gene_splign.keys():
            l=gene_splign[x]
            if j[0] not in l:
                l.append(j[0])
            gene_splign[x]=l
        else:
            l=[]
            l.append(j[0])
            gene_splign[x]=l
fp.close()
fp1=open("best1",'w')
for i in gene_splign.keys():
    max_score=0
    for x in gene_splign[i]:
        map_len=0
        total_score=0
        for z in number_splign[x]:
            z1=z.split()
            map_len+=int(z1[4])
            if z1[3]=='-':
                ide=0
            else:
                ide=float(z1[3])
            total_score+=ide*int(z1[4])
        ave_score=round(total_score/map_len,3)
        if ave_score>max_score:
            max_score=ave_score
            choose=x
    s=[]
    e=[]
    for x in number_splign[choose]:
        y=x.split()
        if y[7]!='-':
            start=min(int(y[7]),int(y[8]))
            end=max(int(y[7]),int(y[8]))
            s.append(start)
            e.append(end)
            fp1.write(str(start)+'-'+str(end)+',')
            contig=y[2][4:]
            if (int(y[5])-int(y[6]))*(int(y[7])-int(y[8]))>0:
                string="+"
            else:
                string="-"
        else:
            if min(int(y[5]),int(y[6]))==1:
                fp1.write("start-"+y[4]+",")
            elif y[9]=="<M-Gap>":
                fp1.write("MGap-"+y[4]+",")
            else:
                fp1.write("stop-"+y[4]+",")
    start=min(s)
    end=max(e)
    fp1.write('\t'+contig+'\t'+str(start)+'\t'+str(end)+'\t'+string+'\t'+str(max_score)+'\t'+i+'\t'+choose+'\n')
fp1.close()
