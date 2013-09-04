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
sum,sum1,sum2,sum3,inter,beg,adv=0,0,0,0,0,0,0
for u in fname:
    sum=sum+int(u[8])
    if u[7]== "Intermediate":
        sum1=sum1+int(u[8])
        inter+=1
    if u[7]== "Beginner":
        sum2=sum2+int(u[8])
        beg+=1
    if u[7]== "Advanced":
        sum3=sum3+int(u[8])
        adv+=1
overallaveragelikes = sum/l
print "overallaveragelikes=",overallaveragelikes
avgvotesforinter= sum1/inter
print "average votes for intermediate level=",avgvotesforinter
avgvotesforbeg= sum2/beg
print "average votes for beginner level=",avgvotesforbeg
avgvotesforadv= sum3/adv
print "average votes for advanced level=",avgvotesforadv
