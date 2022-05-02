#!/usr/bin/env python
import re
n=0
fp1=open("extend_log.txt",'w')
fp=open("sorted_best1",'r')
for i in fp:
    j=i.split()
    if n==0:
        extend=[]
        n=1
        chr_name=j[1]
        start=int(j[2])
        end=int(j[3])
        string=j[4]
        iden=float(j[5])
        gene=j[6]
        exon=j[0].split(",")
        exon.remove('') 
        for x in range(len(exon)):
            if re.match('start',exon[x]) or re.match('stop',exon[x]):
                extend.append(exon[x])
            elif re.match('MGap',exon[x]):
                a=re.search('-',exon[x-1])
                before=(exon[x-1][:a.start()],exon[x-1][a.end():])
                a=re.search('-',exon[x+1])
                after=(exon[x+1][:a.start()],exon[x+1][a.end():])
                if int(before[0])<int(after[0]):
                    st=exon[x]+":"+before[1]+'-'+after[0]
                else:
                    st=exon[x]+":"+after[1]+'-'+before[0]
                extend.append(st)
            else:
                pass
    else:
        if j[1]==chr_name and j[4]==string and int(j[2])<=end:
            if float(j[5])>iden:
                extend=[]
                iden=float(j[5])
                start=int(j[2])
                end=int(j[3])
                gene=j[6]
                exon=j[0].split(",")
                exon.remove('')
                for x in range(len(exon)):
                    if re.match('start',exon[x]) or re.match('stop',exon[x]):
                        extend.append(exon[x])
                    elif re.match('MGap',exon[x]):
                        a=re.search('-',exon[x-1])
                        before=(exon[x-1][:a.start()],exon[x-1][a.end():])
                        a=re.search('-',exon[x+1])
                        after=(exon[x+1][:a.start()],exon[x+1][a.end():])
                        if int(before[0])<int(after[0]):
                            st=exon[x]+":"+before[1]+'-'+after[0]
                        else:
                            st=exon[x]+":"+after[1]+'-'+before[0]
                        extend.append(st)
                    else:
                        pass
        else:
            print(chr_name+'\t'+'BestRef'+'\t'+'gene'+'\t'+str(start)+'\t'+str(end)+'\t'+'.'+'\t'+string+'\t'+'.'+'\t'+"ID="+gene+";score="+str(iden))
            print(chr_name+'\t'+'BestRef'+'\t'+'mRNA'+'\t'+str(start)+'\t'+str(end)+'\t'+'.'+'\t'+string+'\t'+'.'+'\t'+"ID="+gene+".mRNA;Parent="+gene)
            l1=[]
            for x in exon:
                a=re.search('-',x)
                a1=a.start()
                a2=a.end()
                if x[:a1]=='start' or x[:a1]=='stop' or x[:a1]=='MGap':
                    pass
                else:
                    fi=int(x[:a1])
                    en=int(x[a2:])
                    l1.append((fi,en))
            num=0
            for x in sorted(l1):
                num+=1
                print(chr_name+'\t'+'BestRef'+'\t'+'exon'+'\t'+str(x[0])+'\t'+str(x[1])+'\t'+'.'+'\t'+string+'\t'+'.'+'\t'+"ID="+gene+".exon"+str(num)+";Parent="+gene+".mRNA")
                print(chr_name+'\t'+'BestRef'+'\t'+'CDS'+'\t'+str(x[0])+'\t'+str(x[1])+'\t'+'.'+'\t'+string+'\t'+'0'+'\t'+"ID="+gene+".CDS"+str(num)+";Parent="+gene+".mRNA")
            fp1.write("ID="+gene+";score="+str(iden))
            if extend==[]:
                fp1.write('\t'+'notextend'+'\n')
            else:
                for x in extend:
                    fp1.write('\t'+x)
                fp1.write('\n')
            extend=[]
            chr_name=j[1]
            start=int(j[2])
            end=int(j[3])
            string=j[4]
            iden=float(j[5])
            gene=j[6]
            exon=j[0].split(",")
            exon.remove('')
            for x in range(len(exon)):
                if re.match('start',exon[x]) or re.match('stop',exon[x]):
                    extend.append(exon[x])
                elif re.match('MGap',exon[x]):
                    a=re.search('-',exon[x-1])
                    before=(exon[x-1][:a.start()],exon[x-1][a.end():])
                    a=re.search('-',exon[x+1])
                    after=(exon[x+1][:a.start()],exon[x+1][a.end():])
                    if int(before[0])<int(after[0]):
                        st=exon[x]+":"+before[1]+'-'+after[0]
                    else:
                        st=exon[x]+":"+after[1]+'-'+before[0]
                    extend.append(st)
                else:
                    pass
print(chr_name+'\t'+'BestRef'+'\t'+'gene'+'\t'+str(start)+'\t'+str(end)+'\t'+'.'+'\t'+string+'\t'+'.'+'\t'+"ID="+gene+";score="+str(iden))
print(chr_name+'\t'+'BestRef'+'\t'+'mRNA'+'\t'+str(start)+'\t'+str(end)+'\t'+'.'+'\t'+string+'\t'+'.'+'\t'+"ID="+gene+".mRNA;Parent="+gene)
l1=[]
for x in exon:
    a=re.search('-',x)
    a1=a.start()
    a2=a.end()
    if x[:a1]=='start' or x[:a1]=='stop' or x[:a1]=='MGap':
        pass
    else:
        fi=int(x[:a1])
        en=int(x[a2:])
        l1.append((fi,en))
num=0
for x in sorted(l1):
    num+=1
    print(chr_name+'\t'+'BestRef'+'\t'+'exon'+'\t'+str(x[0])+'\t'+str(x[1])+'\t'+'.'+'\t'+string+'\t'+'.'+'\t'+"ID="+gene+".exon"+str(num)+";Parent="+gene+".mRNA")
    print(chr_name+'\t'+'BestRef'+'\t'+'CDS'+'\t'+str(x[0])+'\t'+str(x[1])+'\t'+'.'+'\t'+string+'\t'+'0'+'\t'+"ID="+gene+".CDS"+str(num)+";Parent="+gene+".mRNA")
fp1.write("ID="+gene+";score="+str(iden))
if extend==[]:
    fp1.write('\t'+'notextend'+'\n')
else:
    for x in extend:
        fp1.write('\t'+x)
    fp1.write('\n')
fp1.close()
fp.close()
