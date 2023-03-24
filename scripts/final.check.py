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
    n=1
    print(i)
    if i.split()[2]=='gene':
        for a in h[i]:
            b=a.split()
            if b[2]=='mRNA':
                print(a)
            elif b[2]=='CDS':
                x=re.search('CDS',b[8]).start()
                y=re.search(';',b[8]).start()
                number=b[8][x:y]
                new=b[8].replace(number,'CDS'+str(n))
                print(b[0]+'\t'+b[1]+'\t'+b[2]+'\t'+b[3]+'\t'+b[4]+'\t'+b[5]+'\t'+b[6]+'\t'+'0'+'\t'+new)
                n+=1
            else:
                x=re.search('exon',b[8]).start()
                y=re.search(';',b[8]).start()
                number=b[8][x:y]
                new=b[8].replace(number,'exon'+str(n))
                print(b[0]+'\t'+b[1]+'\t'+b[2]+'\t'+b[3]+'\t'+b[4]+'\t'+b[5]+'\t'+b[6]+'\t'+b[7]+'\t'+new)
    else:
        for a in h[i]:
            b=a.split()
            x=re.search('exon',b[8]).start()
            y=re.search(';',b[8]).start()
            number=b[8][x:y]
            new=b[8].replace(number,'exon'+str(n))
            print(b[0]+'\t'+b[1]+'\t'+b[2]+'\t'+b[3]+'\t'+b[4]+'\t'+b[5]+'\t'+b[6]+'\t'+b[7]+'\t'+new)
            n+=1
