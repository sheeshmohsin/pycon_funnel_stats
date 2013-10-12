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

if sum!=0:
    overallaveragelikes = sum/l
    print "Over all average likes=",overallaveragelikes
else:
    print "There is no proposal for talks"

if sum1!=0:
    avgvotesforinter= sum1/inter
    print "Average votes for intermediate level=",avgvotesforinter
else:
    print "There is no proposal under Intermediate level"
if sum2!=0:
    avgvotesforbeg= sum2/beg
    print "Average votes for beginner level=",avgvotesforbeg
else:
    print "There is no proposal under Beginner level"

if sum3!=0:
    avgvotesforadv= sum3/adv
    print "Average votes for advanced level=",avgvotesforadv
else:
    print "There is no proposal under advancel level"

if sum4!=0:
    avgvotesforinterforsci = sum4/sci
    print "Average votes for intermediate level for Scientific Computing=",avgvotesforinterforsci
else:
    print "There is no proposal for intermediate level for Scientific Computing"

if sum5!=0:
    avgvotesforinterforsoft = sum5/soft
    print "Average votes for intermediate level for Software Development Tools=",avgvotesforinterforsoft
else:
    print "There is no proposal for intermediate level for Software Development Tools"

if sum6!=0:
    avgvotesforinterforinfr = sum6/infr
    print "Average votes for intermediate level for Infrastructure=",avgvotesforinterforinfr
else:
    print "There is no proposal for intermediate level for Infrastructure"

if sum7a!=0:
    avgvotesforinterforweb = sum7/web
    print "Average votes for intermediate level for Web Development=",avgvotesforinterforweb
else:
    print "There is no proposal for intermediate level for Web Development"

if sum8!=0:
    avgvotesforinterforemb = sum8/emb
    print "Average votes for intermediate level for Embedded/Real-time Python=",avgvotesforinterforemb
else:
    print "There is no proposal for intermediate level for Embedded/Real-time Python"

if sum9!=0:
    avgvotesforinterforcor = sum9/cor
    print "Average votes for intermediate level for Core Python=",avgvotesforinterforcor
else:
    print "There is no proposal for intermediate level for Core Python"

if sum0!=0:
    avgvotesforinterforwork = sum0/work
    print "Average votes for intermediate level for Workshops=",avgvotesforinterforwork
else:
    print "There is no proposal for intermediate level for Workshops"

if sum4b!=0:
    avgvotesforinterforscib = sum4b/scib
    print "Average votes for Beginner level for Scientific Computing=",avgvotesforinterforscib
else:
    print "There is no proposal for Beginner level for Scientific Computing"

if sum5b!=0:
    avgvotesforinterforsoftb = sum5b/softb
    print "Average votes for Beginner level for Software Development Tools=",avgvotesforinterforsoftb
else:
    print "There is no proposal for Beginner level for Software Development Tools"

if sum6b!=0:
    avgvotesforinterforinfrb = sum6b/infrb
    print "Average votes for Beginner level for Infrastructure=",avgvotesforinterforinfrb
else:
    print "There is no proposal for Beginner level for Infrastructure"

if sum7b!=0:
    avgvotesforinterforwebb = sum7b/webb
    print "Average votes for Beginner level for Web Development=",avgvotesforinterforwebb
else:
    print "There is no proposal for Beginner level for Web Development"

if sum8b!=0:
    avgvotesforinterforembb = sum8b/embb
    print "Average votes for Beginner level for Embedded/Real-time Python=",avgvotesforinterforembb
else:
    print "There is no proposal for Beginner level for Embedded/Real-time Python"

if sum9b!=0:
    avgvotesforinterforcorb = sum9b/corb
    print "Average votes for Beginner level for Core Python=",avgvotesforinterforcorb
else:
    print "There is no proposal for Beginner level for Core Python"

if sum0b!=0:
    avgvotesforinterforworkb = sum0b/workb
    print "Average votes for Beginner level for Workshops=",avgvotesforinterforworkb
else:
    print "There is no proposal for Beginner level for Workshops"

if sum4a!=0:
    avgvotesforinterforscia = sum4a/scia
    print "Average votes for Advanced level for Scientific Computing=",avgvotesforinterforscia
else:
    print "There is no proposal for advanced level for Scientific Computing"

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

if sum7a!=0:
    avgvotesforinterforweba = sum7a/weba
    print "Average votes for Advanced level for Web Development=",avgvotesforinterforweba
else:
    print "There is no proposal for advanced level for Web Developement"

if sum8a!=0:
    avgvotesforinterforemba = sum8a/emba
    print "Average votes for Advanced level for Embedded/Real-time Python=",avgvotesforinterforemba
else:
    print "There is no proposal for advanced level for Embedded/Real-time Python"

if sum9a!=0:
    avgvotesforinterforcora = sum9a/cora
    print "Average votes for Advanced level for Core Python=",avgvotesforinterforcora
else:
    print "There is no proposal for advanced level for Core Python"

if sum0a!=0:
    avgvotesforinterforworka = sum0a/worka
    print "Average votes for Advanced level for Workshops=",avgvotesforinterforworka
else:
    print "There is no proposal for advanced level for Workshops"

print "Total Number of people applied for talks=",l
print "Total Number of proposals under intermediate level=",inter
print "Total Number of proposals under beginner level=",beg
print "Total Number of proposals under advanced level=",adv
