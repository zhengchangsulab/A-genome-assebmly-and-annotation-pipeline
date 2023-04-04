#!/usr/bin/env python
import re,sys
gff=sys.argv[1]
h={}
fp=open(gff,'r')
for i in fp:
    i=re.sub('\n','',i)
    j=i.split()
    if j[2]=='gene' or j[2]=='pseudogene':
        name=i
        l=[]
    else:
        l.append(i)
        h[name]=l
fp.close()
for i in h.keys():
    print(i)
    if i.split()[2]=='gene':
        exon=[]
        cds=[]
        gene_start=re.match('ID=',i.split()[8]).end()
        gene_end=re.search(';',i.split()[8]).start()
        gene_name=i.split()[8][gene_start:gene_end]
        for a in h[i]:
            b=a.split()
            if b[2]=='CDS':
                cds.append((int(b[3]),int(b[4])))
            if b[2]=='exon':
                exon.append((int(b[3]),int(b[4])))
        new_exon=sorted(exon)
        new_cds=sorted(cds)
        n=1
        for a in h[i]:
            b=a.split()
            if b[2]=='mRNA':
                print(a)
            elif b[2]=='CDS':
                x=re.search('CDS',b[8]).start()
                y=re.search(';',b[8]).start()
                number=b[8][x:y]
                new='ID='+gene_name+'.CDS'+str(n)+';Parent='+gene_name+'.mRNA'
                print(b[0]+'\t'+b[1]+'\t'+b[2]+'\t'+str(new_cds[n-1][0])+'\t'+str(new_cds[n-1][1])+'\t'+b[5]+'\t'+b[6]+'\t'+'0'+'\t'+new)
                n+=1
            else:
                x=re.search('exon',b[8]).start()
                y=re.search(';',b[8]).start()
                number=b[8][x:y]
                new='ID='+gene_name+'.exon'+str(n)+';Parent='+gene_name+'.mRNA'
                print(b[0]+'\t'+b[1]+'\t'+b[2]+'\t'+str(new_exon[n-1][0])+'\t'+str(new_exon[n-1][1])+'\t'+b[5]+'\t'+b[6]+'\t'+b[7]+'\t'+new)
    else:
        exon=[]
        gene_start=re.match('ID=',i.split()[8]).end()
        gene_end=re.search(';',i.split()[8]).start()
        gene_name=i.split()[8][gene_start:gene_end]
        for a in h[i]:
            b=a.split()
            if b[2]=='exon':
                exon.append((int(b[3]),int(b[4])))
        new_exon=sorted(exon)
        n=1
        for a in h[i]:
            b=a.split()
            x=re.search('exon',b[8]).start()
            y=re.search(';',b[8]).start()
            number=b[8][x:y]
            new='ID='+gene_name+'.exon'+str(n)+';Parent='+gene_name+'.mRNA'
            print(b[0]+'\t'+b[1]+'\t'+b[2]+'\t'+str(new_exon[n-1][0])+'\t'+str(new_exon[n-1][1])+'\t'+b[5]+'\t'+b[6]+'\t'+b[7]+'\t'+new)
            n+=1
