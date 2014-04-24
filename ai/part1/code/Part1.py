import re
import os

a=raw_input("Ask a query:\n")

def add_to_dict(dictionary, fname):
    f = open(fname, 'r')
    for line in f:
		    temp = line[:-1]
		    temp = temp.split(',')
		    a = temp[0]
		    b = temp[1:]
		    if a not in dictionary:
			dictionary[a] = b

def parse_detail(dictionary,fname):
    f = open(fname, 'r')
    count = 0
    for line in f:
	dictionary[count] = line[0:-1]
	count = count + 1

def player_details(dictionary,fname):
    f = open(fname, 'r')
    count = 0
    for line in f:
	temp = line[-1]
	temp = line.split('\t')
	age = str(temp[3]).split()
	a = int(age[0])
	if temp[0] not in dictionary:
		dictionary[temp[0]] = a
	count = count + 1

def run_dict(dictionary, fname):
    f = open(fname, 'r')
    for line in f:
		    temp = line[:-1]
		    temp = temp.split(',')
		    a = temp[0]
		    b = temp[1:]
		    if a not in dictionary:
			dictionary[a] = int(b[1])
		    elif a in dictionary:
			value = dictionary[a] + int(b[1])
			dictionary[a] = value

def get_openers(dictionary,fname):
    f = open(fname,'r')
    count = 1
    for line in f :
	if count < 3:
	    temp = line[:-1]
	    temp = temp.split(',')
	    a = temp[0]
	    b= temp[1:]
	    if a not in dictionary:
		dictionary[a] = b
	else:
	    break
	count += 1




d1={}
d2={}
d3={}
d4={}
d5={}
d11={}
d22={}
d33={}
d44={}
d55={}


p1=None
p2=None
number_of='0'
final_score='0'
maximum=0
part1_try=0
dict_1=a.split("match,");
o_no=None
query=None

if(dict_1[0].find('first')!=-1):
	odi="first"
elif(dict_1[0].find('One')!=-1):
  part1_try=1
elif(dict_1[0].find('Two')!=-1):
  part1_try=1
elif(dict_1[0].find('second')!=-1):
	odi="second"
elif(dict_1[0].find('Three')!=-1):
  part1_try=1
elif(dict_1[0].find('Four')!=-1):
  part1_try=1
elif(dict_1[0].find('Five')!=-1):
  part1_try=1
elif(dict_1[0].find('third')!=-1):
	odi="third"
elif(dict_1[0].find('fourth')!=-1):
	odi="fourth"
elif(dict_1[0].find('fifth')!=-1):
	odi="fifth"
#print part1_try
#print "ho gya\n"

if(dict_1[1].find("of which")!=-1):
	d=dict_1[1].split("of which")
elif(dict_1[1].find("in which")!=-1):
	d=dict_1[1].split("in which")
elif(dict_1[1].find("who")!=-1):
	d=dict_1[1].split("who")
#print "hojaaaaaaa\n"


if d[1].find("ball")!=-1:
	query="ball"
elif d[1].find('caught')!=-1:
  part1_try=2
elif d[1].find('bowled')!=-1:
  part1_try=2
elif d[1].find("over")!=-1:
	query="over"
elif d[1].find("dismissed")!=-1:
	query="p1"
elif d[1].find("hit")!=-1:
	query="p2"
elif d[1].find("bowler")!=-1:
	query="p1"

if((d[0].find("hit"))!=-1):
	l=d[0].split("hit")
	p2=l[0].lstrip()
	p2=p2.rstrip()
elif((d[0].find("bowl"))!=-1):
	l=d[0].split("bowl")
	p1=l[0].lstrip()
	p1=p1.rstrip()
elif((d[0].find("was out"))!=-1):
	l=d[0].split("was")
	p2=l[0].lstrip()
	p2=p2.rstrip()

p=l[1].split("in over")
if len(p)>=2:
	t=p[1].lstrip()
	if(t[0]!='s'):
		s=t.split(' ')
		o_no=s[0].rstrip(',')

l=re.findall("\d+",p[0])
if len(l)>0:
	number_of=l[0]
	w=p[0].rstrip()
	final_score=w.split(' ')[-1].rstrip(',')
	if final_score.find("six")!=-1:
		final_score="six"
	elif final_score.find("four")!=-1:
		final_score="four"
	elif final_score.find("wide")!=-1:
		final_score="wide"

elif ((p[0].find("max"))!=-1):
		maximum=1
		w=p[0].rstrip()
		final_score=w.split(' ')[-1].rstrip(',')
		if final_score.find("six")!=-1:
			final_score="six"
		elif final_score.find("four")!=-1:
			final_score="four"
		elif final_score.find("wide")!=-1:
			final_score="wide"
else:
	w=p[0].rstrip()
	final_score=w.split(' ')[-1].rstrip(',')
	if final_score.find("six")!=-1:
		final_score="six"
	elif final_score.find("four")!=-1:
		final_score="four"
	elif final_score.find("wide")!=-1:
		final_score="wide"

if odi == "first":
	lines = open('../dataset/match1.txt','r').readlines()
if odi == "second":
	lines = open('../dataset/match2.txt','r').readlines()
if odi == "third":
	lines = open('../dataset/match3.txt','r').readlines()
if odi == "fourth":
	lines = open('../dataset/match4.txt','r').readlines()
if odi == "fifth":
	lines = open('../dataset/match5.txt','r').readlines()



if query=='p1':
	bowler=[]
	if maximum == 1 or number_of!= '0':
		maxi = 0
		count = 0
		p1 = None
		maximum_p = {}

	for i in range(len(lines)):
		if p2 != None and p1 == None:
			search = "to "+p2
		elif p1!=None and p2 == None:
			search = p1 + " to"
		elif p1!=None and p2!=None:
			search = p1+" to "+p2
		if re.search(search,lines[i]):
			#print lines[i]
			if(re.search(final_score,lines[i+1])):
				if maximum == 0 and number_of == '0':
					b = lines[i].split('to')[0]
					if b not in bowler:
						bowler.append(b)
				elif maximum == 1 or number_of!='0' :
					if p1 == None:
						p1 = lines[i].split('to')[0]
						count = count+1
						maximum_p[p1]=count
						print "Count:" + str(count)
					else:
						if(lines[i].split('to')[0] == p1):
							count = count + 1
							print "Count:" + str(count)
							maximum_p[p1]=count
						else:
							print p1
							maximum_p[p1] = count
							if count > maxi:
								maxi = count
							p1 = lines[i].split('to')[0]
							count = 1
							maximum_p[p1]=count
	if maximum == 1 or number_of!= '0':
		print maximum_p
		if maximum==0 and number_of!='0':
		     maxi = str(number_of)
		for i in maximum_p:
			if str(maximum_p[i]) == str(maxi):
				print i
	elif maximum==0 and number_of == '0':
		print bowler

if query == 'p2':
	batsmen = []
	if maximum == 1 or number_of!='0' :
		maxi = 0
		count = 0
		p2 = None
		maximum_p2 = {}

	for i in range(len(lines)):
		if p2 != None and p1 == None:
			search = "to "+p2
		elif p1!=None and p2 == None:
			search = p1 + " to"

			search = p1+" to "+p2
		if re.search(search,lines[i]):
			print lines[i]
			if maximum == 0 and number_of=='0':
				if(re.search(final_score,lines[i+1])):
					b = lines[i].split('to')[0]
					if b not in batsmen:
						batsmen.append(b)
			elif maximum == 1 or number_of!='0':
				if p2 == None:
					p2 = lines[i].split('to')[1]
					count = count+1
					maximum_p2[p2]=count
					print "Count:" + str(count)
				else:
					if(lines[i].split('to')[1] == p2):
						count = count + 1
						print "Count:" + str(count)
						maximum_p2[p2]=count
					else:
						print p2
						maximum_p2[p2] = count
						if count > maxi:
							maxi = count
						p2 = lines[i].split('to')[1]
						count = 1
						maximum_p2[p2]=count
	if maximum == 1 or number_of!='0':
		print maximum_p2
		if maximum==0 and number_of!='0':
		     maxi = str(number_of)
		for i in maximum_p2:
			if str(maximum_p2[i]) == maxi:
				print i
	elif maximum == 0 and number_of=='0':
		print batsmen

if query == 'over':
	over = []
	if maximum == 1 or number_of!= '0':
		maxi = 0
		count = 0
		over = None
		maxover = {}
	for i in range(len(lines)):
		if p2 != None and p1 == None:
			search = "to "+p2
		elif p1!=None and p2 == None:
			search = p1 + " to"
		elif p1!=None and p2!=None:
			search = p1+" to "+p2

		if re.search(search,lines[i]):
			print lines[i]
			if(re.search(final_score,lines[i+1])):
				if maximum == 0 and number_of=='0':
					over.append(lines[i-1].split('.')[0])
				elif maximum == 1  or number_of!='0':
					if over == None:
						over = lines[i-1].split('.')[0]
						count = count+1
						maxover[over]=count
						print "Count:" + str(count)
					else:
						if(lines[i-1].split('.')[0] == over):
							count = count + 1
							print "Count:" + str(count)
							maxover[over]=count
						else:
							print over
							maxover[over] = count
							if count > maxi:
								maxi = count
							over = lines[i-1].split('.')[0]
							count = 1
							maxover[over]=count
	if maximum == 1 or number_of!='0':
		print maxover
		if maximum==0 and number_of!='0':
		     maxi = number_of
		     print maxi
		for i in maxover:
			print maxover[i]
			if str(maxover[i]) == maxi:
				print i
	elif maximum == 0 and number_of=='0':
		print over

if query == "ball":
	ball = []
	if p2 != None and p1 == None:
		search = "to "+p2
	elif p1!=None and p2 == None:
		search = p1 + " to"
	elif p1!=None and p2!=None:
		search = p1+" to "+p2
	for i in range(len(lines)):
		if re.search(search,lines[i]):
			print lines[i]
			if(re.search(final_score,lines[i+1])):
				over = lines[i-1].split('.')[0]
				if over == o_no:
					ball.append(lines[i-1].split('.')[1])
	print ball


def add_to_list(list1, fname):
    c=','
    f = open(fname, 'r')
    for line in f:
        temp = line[:-1]
        temp = temp.split(c)
        a = temp[0]
        b = temp[1:]
        if a not in list1:
            list1.insert(len(list1),a)
    return list1

def add_to_dict_profile(dictionary, fname):
    c='\t'
    f = open(fname, 'r')
    for line in f:
        temp = line[:-1]
        temp = temp.split(c)
        a = temp[0]
        b = temp[1:]
        if a not in dictionary:
            dictionary[a] = b
       # print dictionary[a]

# It retrieves the variable names corresponding to players of the match
def parse_for_players_winteam(profile,winning_team):
        toreturn  = []
        if winning_team[0] == 'tied':
            return toreturn
        # team for which player plays is in 3rd column
        for i in profile:
            temp = profile[i]
            temp1 = temp[3]
            temp2 = temp1.split(', ')
            if winning_team[0] in temp2:
                toreturn.append(i)
        return toreturn

def parse_lessthan26(profile):
    toreturn  = []
    # team for which player plays is in 3rd column
    for i in profile:
        temp = profile[i]
        temp1 = temp[2]
        temp2 = temp1.split(' ')
        temp3 = int(temp2[0])
        if temp3 < 26:
            toreturn.append(i)
    return toreturn



def parse_for_players_losing_team(winning_team,profile):
    toreturn  = []
    if winning_team[0] == 'tied':
        return toreturn
    if winning_team[0] == 'New Zealand':
        losing_team = 'India'
    else:
        losing_team = 'New Zealand'
    # team for which player plays is in 3rd column
    for i in profile:
        temp = profile[i]
        temp1 = temp[3]
        temp2 = temp1.split(',')
        if losing_team in temp2:
            toreturn.append(i)
    return toreturn

def parse_for_duck(bats):
    toreturn = []
    for i in bats:
        temp = bats[i]
  #      print temp
        temp1 = temp[1]
   #     print temp1
        if temp1=='0':
    #        print temp1
            toreturn.append(i)
    return toreturn

score = {}
no_ducks = []
def parse_250run(bats1,bats2,bats3,bats4,bats5):
    toreturn = []
    for i in bats1:
        temp = bats1[i]
        runs = int(temp[1])
        score[i] = runs
        if runs > 0 :
            no_ducks.insert(len(no_ducks),i)
    for i in bats2:
        temp = bats2[i]
        runs = int(temp[1])
        if i not in score:
            score[i] = runs
        else:
            score[i] += runs
        if runs == 0:
            if i in no_ducks:
                no_ducks.remove(i);
        elif runs > 0:
            if i not in bats1:
                no_ducks.insert(len(no_ducks),i)

    for i in bats3:
        temp = bats3[i]
        runs = int(temp[1])
        if i not in score:
            score[i] = runs
        else:
            score[i] += runs
        if runs == 0:
            if i in no_ducks:
                no_ducks.remove(i);
        elif runs > 0:
            if i not in bats1 and i not in bats2:
                no_ducks.insert(len(no_ducks),i)


    for i in bats4:
        temp = bats4[i]
        runs = int(temp[1])
        if i not in score:
            score[i] = runs
        else:
            score[i] += runs
        if runs == 0:
            if i in no_ducks:
                no_ducks.remove(i);
        elif runs > 0:
            if i not in bats1 and i not in bats2 and i not in bats3 :
                no_ducks.insert(len(no_ducks),i)

    for i in bats5:
        temp = bats5[i]
        runs = int(temp[1])
        if i not in score:
            score[i] = runs
        else:
            score[i] += runs
        if runs == 0:
            if i in no_ducks:
                no_ducks.remove(i);
        elif runs > 0:
            if i not in bats1 and i not in bats2 and i not in bats3 and i not in bats4 :
                no_ducks.insert(len(no_ducks),i)
    for i in score:
        total_score = score[i]
        if total_score > 250:
            toreturn.append(i)
    return toreturn



# This function returns a list of variable, corresponding to players who satisfy the criteria : strike rate > 150.0
def parse_for_sr(bat, num):
    toreturn = []
    # strike rate is in the 7th column
    for i in bat:
        temp = bat[i]
        k = float(temp[6])
        if k > num:
            toreturn.append(i)
    return  toreturn

def parse_for_belowstr(bat,num):
    toreturn = []
    for i in bat:
        temp = bat[i]
        k = float(temp[6])
        if k < num:
            toreturn.append(i)
    return toreturn

def get_middle(dictionary,fname):
    f = open(fname,'r')
    count = 1
    for line in f :
	if count >= 5 and count <=7:
	    temp = line[:-1]
	    temp = temp.split(',')
	    a = temp[0]
	    b= temp[1:]
	    if a not in dictionary:
		dictionary[a] = b
	elif count > 9:
	    break
	count += 1

def player_details2(dictionary,fname):
    f = open(fname, 'r')

    for line in f:
	temp = line[-1]
	temp = line.split('\t')
	a = str(temp[-1])
	if(a.find('Right') != -1):
		if temp[0] not in dictionary:
			dictionary[temp[0]] = 'Right'
	else:
		if temp[0] not in dictionary:
			dictionary[temp[0]] = 'Left'




