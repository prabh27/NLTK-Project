import nltk
from nltk.corpus import wordnet as wn
import math
import re
import pickle
import os
from common import *


def ai(no,who,what,words):
	#1
	os.chdir("../DataSet/match"+str(1))
	inn1 = pickle.load(open(str(no)+"1comm.p","rb"))
   	inn2 = pickle.load(open(str(no)+"2comm.p","rb"))

	tu=[]
	syns=wn.synsets('dismissed')
	for s in syns:
	    for l in s.lemmas:
	            tu.append(l.name)
#print tu
	for i in range(0,len(tu)):
		for j in inn1:
			if tu[i] in inn1[j]['why'] and inn1[j]['to']=='Ryder' and inn1[j]['what']=='OUT':
				print '1a) Dismissed in over ' + str(i)
				print '1b) How was he dismissed ' + str(inn1[j]['why'])
	for i in inn1:
		if inn1[i]['what']=='OUT' and inn1[i]['to']=='Ryder':
			print '1a) Dismissed in over ' + str(i)
			print '1b) How was he dismissed ' + str(inn1[i]['why'])


	#Algorithm Used involves calculating the boundary in which commentaters used words like classy etc. and amongst them the one with with ax lenght indicating that the commentator was excited is selected

	wer=[]
	#2
	print 'The best boundary'
	os.chdir("../match"+str(2))
	inn1 = pickle.load(open(str(2)+"1comm.p","rb"))
   	inn2 = pickle.load(open(str(2)+"2comm.p","rb"))

	tu=[]
	syns=wn.synsets('classy')
	for s in syns:
	    for l in s.lemmas:
	            tu.append(l.name)
	syns=wn.synsets('super')
	for s in syns:
	    for l in s.lemmas:
	            tu.append(l.name)
	syns=wn.synsets('elegant')
	for s in syns:
	    for l in s.lemmas:
	            tu.append(l.name)
	syns=wn.synsets('fine')
	for s in syns:
	    for l in s.lemmas:
	            tu.append(l.name)

	for j in range(0,len(tu)):
		for i in inn1:
			if tu[j] in inn1[i]['why']:
				if inn1[i]['what']=='4 run':
					#print str(i),
					wer.append(str(i) + str(inn1[i]))
	for j in range(0,len(tu)):
		for i in inn2:
			if tu[j] in inn2[i]['why'] :
				if inn2[i]['what']=='4 run':
				#print str(i),
				#print inn2[i]
					wer.append(str(i) + str(inn2[i]))
#print wer[0]
#print wer
	maxi=0
	for i in range(0,len(wer)):
		if len(wer[i])>maxi:
			ind=i
			maxi=len(wer[i])
	print wer[ind]

	wer=[]
	#3
	print 'Overs in which Kohli was most active'
	os.chdir("../match"+str(4))
	inn1 = pickle.load(open(str(4)+"1comm.p","rb"))
   	inn2 = pickle.load(open(str(4)+"2comm.p","rb"))
	sorta=[]

	for i in inn1:
		if inn1[i]['to']=='Kohli':
			sorta.append(i)
	sorta=sorta[:-1]
	print 'Kohli played between the overs ' + min(sorta) + '-' + max(sorta)
	print 'Kohli was most active'

	syns=wn.synsets('active')
	for s in syns:
	    for l in s.lemmas:
	            tu.append(l.name)

	for j in range(0,len(tu)):
		for i in inn2:
			if tu[j] in inn2[i]['why'] :
				if inn2[i]['to']=='Kohli':
					wer.append(str(i) + str(inn2[i]))
	print wer


	#4
	print 'The most interesting over of match 3'
	runer=[]
	runs1=[]
	runs2=[]
	for i in range(0,51):
		runs1.append(0)
	for i in range(0,51):
		runs2.append(0)

	os.chdir("../match"+str(3))
	inn1 = pickle.load(open(str(3)+"1comm.p","rb"))
   	inn2 = pickle.load(open(str(3)+"2comm.p","rb"))
	for i in inn1:
		if len(i)<6:
			runer=inn1[i]['what'].split()
			if runer[0]!='no' and len(runer)!=1:
				runs1[int(math.floor(float(i)))]+=int(runer[0])
	for i in inn2:
		if len(i)<6:
			runer=inn2[i]['what'].split()
			if runer[0]!='no' and len(runer)!=1:
				runs2[int(math.floor(float(i)))]+=int(runer[0])

	print runs1
	print runs2
	tu=[]
	syns=wn.synsets('pulsating')
	for s in syns:
	    for l in s.lemmas:
	            tu.append(l.name)
	syns=wn.synsets('enthralling')
	for s in syns:
	    for l in s.lemmas:
	            tu.append(l.name)
	syns=wn.synsets('berserk')
	for s in syns:
	    for l in s.lemmas:
	            tu.append(l.name)
	syns=wn.synsets('amazing')
	for s in syns:
	    for l in s.lemmas:
	            tu.append(l.name)


	arr=[]
	for j in range(0,len(tu)):
		for i in inn1:
			if tu[j] in inn1[i]['why'] :
				wer.append(str(i) + str(inn1[i]))

	for i in range(0,len(wer)):
		l=wer[i].split(',')
		w=l[0].split('{')
		arr.append(w[0].split('.')[0])
	arr.sort()
	print arr
	fdist = nltk.FreqDist(arr) # creates a frequency distribution from a list
	most_common = fdist.max()    # returns a single element
	top_three = fdist.keys()[:3] # returns a list
	val=[]

	for i in range(0,51):
		val.append(0)

	for i in range(0,3):
		val[int(top_three[i])]+=40*(2-i)

	for i in range(0,3):
		val[int(top_three[i])]+=int(top_three[i])
	maxi=0
	for i in range(0,len(val)):
		if val[i]>maxi:
			ind=i
	print 'Innings 1 ' + 'Over ' + str(ind)


	for j in range(0,len(tu)):
		for i in inn2:
			if tu[j] in inn2[i]['why'] :
				wer.append(str(i) + str(inn2[i]))
	tu=[]
	syns=wn.synsets('pulsating')
	for s in syns:
	    for l in s.lemmas:
	            tu.append(l.name)
	syns=wn.synsets('enthralling')
	for s in syns:
	    for l in s.lemmas:
	            tu.append(l.name)
	syns=wn.synsets('berserk')
	for s in syns:
	    for l in s.lemmas:
	            tu.append(l.name)
	syns=wn.synsets('amazing')
	for s in syns:
	    for l in s.lemmas:
	            tu.append(l.name)



	arr=[]
	for j in range(0,len(tu)):
		for i in inn1:
			if tu[j] in inn1[i]['why'] :
				wer.append(str(i) + str(inn1[i]))

	for i in range(0,len(wer)):
		l=wer[i].split(',')
		w=l[0].split('{')
		arr.append(w[0].split('.')[0])
	arr.sort()
	print arr
	fdist = nltk.FreqDist(arr) # creates a frequency distribution from a list
	most_common = fdist.max()    # returns a single element
	top_three = fdist.keys()[:3] # returns a list
	val=[]

	for i in range(0,51):
		val.append(0)

	for i in range(0,3):
		val[int(top_three[i])]+=40*(2-i)

	for i in range(0,3):
		val[int(top_three[i])]+=int(top_three[i])
	maxi=0
	for i in range(0,len(val)):
		if val[i]>maxi:
			ind=i
	print 'Innings 2 Over ' + str(ind)


	#5

	os.chdir("../match"+str(4))
	inn1 = pickle.load(open(str(4)+"1comm.p","rb"))
   	inn2 = pickle.load(open(str(4)+"2comm.p","rb"))

	for i in inn2:
		if 'amazing' in inn2[i]['why']:
			print inn2[i]

#wer.append(str(i) + str(inn1[i]))


	#6
	print 'Weather conditions of match 4'
	po=[]
	os.chdir("../match"+str(4))
	inn1 = open("weather","rb")
	lo=inn1.readlines()
	tu=[]
	syns=wn.synsets('sunny')
	for s in syns:
	    for l in s.lemmas:
	            tu.append(l.name)
	syns=wn.synsets('clear')
	for s in syns:
	    for l in s.lemmas:
	            tu.append(l.name)


	tuq=[]
	syns=wn.synsets('rain')
	for s in syns:
	    for l in s.lemmas:
	            tuq.append(l.name)

	syns=wn.synsets('overcast')
	for s in syns:
	    for l in s.lemmas:
	            tuq.append(l.name)

	flag=0
	for j in range(0,len(tu)):
		for i in range(0,len(lo)):
			if tu[j] in lo[i]:
				print 'sunny'
				flag=1
				break
			if flag==1:
				break
	flag=0
	for j in range(0,len(tuq)):
		for i in range(0,len(lo)):
			if tuq[j] in lo[i]:
				print 'rainy'
				flag=1
				break
			if flag==1:
				break
#print po

#lo=re.findall('weather',inn1)
#print inn1


#print inn1

def main():
    ans = ai(1,"Ryder",2,3)
#print ans

if __name__ == "__main__":
    main()
