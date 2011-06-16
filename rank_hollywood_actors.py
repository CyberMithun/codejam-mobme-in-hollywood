#!/usr/bin/python
import imdb
im=imdb.IMDb()
top250=im.get_top250_movies()
top100=top250[:100]
a=[]
dq={}
topact=0
namam=''
for i in range(100):
	dd=top100[i]
	im.update(dd)
	cc=dd['cast']
	a.append(cc[0])
	
	
for name in a:
	acto=a.count(name)
	while(name in dq)==False:
		dq[name]=acto
	
mq=sorted(dq, key=dq.get, reverse=True)
for i in range(100):
	print "Rank:",
	print i+1,
	print "Actor:",
	print mq[i]
	
