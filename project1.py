import urllib2
from bs4 import BeautifulSoup
x = urllib2.urlopen("http://in.pycon.org/funnel/2013/")
y = x.read()
c=[]
i,j=0,0
name, fname = [], []
soup = BeautifulSoup(y)
b = soup.find_all('td')
for z in b:
    c.append(z.get_text())
l = len(soup.find_all(colspan="8"))
while j<l:
    while i<11:
        name.append(c.pop(0))
        i+=1
    fname.append(name)
    name=[]
    j+=1
    i=0
sum=sum1=sum2=sum3=inter=beg=adv=sum4=sum5=sum6=sum7=sum8=sum9=sum0=sci=soft=infr=web=emb=cor=work=sum4b=sum5b=sum6b=sum7b=sum8b=sum9b=sum0b=scib=softb=infrb=webb=embb=corb=workb=sum4a=sum5a=sum6a=sum7a=sum8a=sum9a=sum0a=scia=softa=infra=weba=emba=cora=worka=0
for u in fname:
    sum=sum+int(u[8])
    if u[7]== "Intermediate":
        sum1=sum1+int(u[8])
        inter+=1
        if u[5]== "Scientific Computing":
	    sum4=sum4+int(u[8])
	    sci+=1
	if u[5]== "Software Development Tools":
	    sum5=sum5+int(u[8])
	    soft+=1
	if u[5]== "Infrastructure":
	    sum6=sum6+int(u[8])
	    infr+=1
	if u[5]== "Web Development":
	    sum7=sum7+int(u[8])
	    web+=1
	if u[5]== "Embedded/Real-time Python":
	    sum8=sum8+int(u[8])
	    emb+=1
	if u[5]== "Core Python":
            sum9=sum9+int(u[8])
	    cor+=1
	if u[5]== "Workshops":
	    sum0=sum0+int(u[8])
	    work+=1
    if u[7]== "Beginner":
        sum2=sum2+int(u[8])
        beg+=1
	if u[5]== "Scientific Computing":
            sum4b=sum4b+int(u[8])
            scib+=1
        if u[5]== "Software Development Tools":
            sum5b=sum5b+int(u[8])
            softb+=1
        if u[5]== "Infrastructure":
            sum6b=sum6b+int(u[8])
            infrb+=1
        if u[5]== "Web Development":
            sum7b=sum7b+int(u[8])
            webb+=1
        if u[5]== "Embedded/Real-time Python":
            sum8b=sum8b+int(u[8])
            embb+=1
        if u[5]== "Core Python":
            sum9b=sum9b+int(u[8])
            corb+=1
        if u[5]== "Workshops":
            sum0b=sum0b+int(u[8])
            workb+=1
    if u[7]== "Advanced":
        sum3=sum3+int(u[8])
        adv+=1
	if u[5]== "Scientific Computing":
            sum4a=sum4a+int(u[8])
            scia+=1 
        if u[5]== "Software Development Tools":
            sum5a=sum5a+int(u[8])
            softa+=1
        if u[5]== "Infrastructure":
            sum6a=sum6a+int(u[8])
            infra+=1
        if u[5]== "Web Development":
            sum7a=sum7a+int(u[8])
            weba+=1
        if u[5]== "Embedded/Real-time Python":
            sum8a=sum8a+int(u[8])
            emba+=1
        if u[5]== "Core Python":
            sum9a=sum9a+int(u[8])
            cora+=1
        if u[5]== "Workshops":
            sum0a=sum0a+int(u[8])
            worka+=1

overallaveragelikes = sum/l
print "Over all average likes=",overallaveragelikes

avgvotesforinter= sum1/inter
print "Average votes for intermediate level=",avgvotesforinter

avgvotesforbeg= sum2/beg
print "Average votes for beginner level=",avgvotesforbeg

avgvotesforadv= sum3/adv
print "Average votes for advanced level=",avgvotesforadv

avgvotesforinterforsci = sum4/sci
print "Average votes for intermediate level for Scientific Computing=",avgvotesforinterforsci

avgvotesforinterforsoft = sum5/soft
print "Average votes for intermediate level for Software Development Tools=",avgvotesforinterforsoft

avgvotesforinterforinfr = sum6/infr
print "Average votes for intermediate level for Infrastructure=",avgvotesforinterforinfr

avgvotesforinterforweb = sum7/web
print "Average votes for intermediate level for Web Development=",avgvotesforinterforweb

avgvotesforinterforemb = sum8/emb
print "Average votes for intermediate level for Embedded/Real-time Python=",avgvotesforinterforemb

avgvotesforinterforcor = sum9/cor
print "Average votes for intermediate level for Core Python=",avgvotesforinterforcor

avgvotesforinterforwork = sum0/work
print "Average votes for intermediate level for Workshops=",avgvotesforinterforwork

avgvotesforinterforscib = sum4b/scib
print "Average votes for Beginner level for Scientific Computing=",avgvotesforinterforscib

avgvotesforinterforsoftb = sum5b/softb
print "Average votes for Beginner level for Software Development Tools=",avgvotesforinterforsoftb

avgvotesforinterforinfrb = sum6b/infrb
print "Average votes for Beginner level for Infrastructure=",avgvotesforinterforinfrb

avgvotesforinterforwebb = sum7b/webb
print "Average votes for Beginner level for Web Development=",avgvotesforinterforwebb

avgvotesforinterforembb = sum8b/embb
print "Average votes for Beginner level for Embedded/Real-time Python=",avgvotesforinterforembb

avgvotesforinterforcorb = sum9b/corb
print "Average votes for Beginner level for Core Python=",avgvotesforinterforcorb

avgvotesforinterforworkb = sum0b/workb
print "Average votes for Beginner level for Workshops=",avgvotesforinterforworkb

avgvotesforinterforscia = sum4a/scia
print "Average votes for Advanced level for Scientific Computing=",avgvotesforinterforscia

if sum5a!=0:
    avgvotesforinterforsofta = sum5a/softa
    print "Average votes for Advanced level for Software Development Tools=",avgvotesforinterforsofta
else:
    print "There is no proposal for advanced level for Software Development Tools"

if sum6a!=0:
    avgvotesforinterforinfra = sum6a/infra
    print "Average votes for Advanced level for Infrastructure=",avgvotesforinterforinfra
else:
    print "There is no proposal for advanced level for Infrastructure"

avgvotesforinterforweba = sum7a/weba
print "Average votes for Advanced level for Web Development=",avgvotesforinterforweba

avgvotesforinterforemba = sum8a/emba
print "Average votes for Advanced level for Embedded/Real-time Python=",avgvotesforinterforemba

avgvotesforinterforcora = sum9a/cora
print "Average votes for Advanced level for Core Python=",avgvotesforinterforcora

avgvotesforinterforworka = sum0a/worka
print "Average votes for Advanced level for Workshops=",avgvotesforinterforworka


