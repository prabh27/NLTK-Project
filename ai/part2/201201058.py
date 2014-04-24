import nltk
import sys

query1_ans = []
query2_ans = []
query3_ans = []
query4_ans = []
query5_ans = []
query6_ans = []
query7_ans = []
query8_ans = []
query9_ans = []
query10_ans = []
query11_ans = []
query12_ans = []
query13_ans = []
query14_ans = []
query15_ans = []
query18_ans = []
query20_ans = []
avg_details={}

# function to add the contents of file, after proper parsing, to the given dictionary
def add_to_dict(dictionary, fname):
    c=','
    f = open(fname, 'r')
    for line in f:
        temp = line[:-1]
        temp = temp.split(c)
        a = temp[0]
        b = temp[1:]
        if a not in dictionary:
            dictionary[a] = b

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

# It retrieves the variable names corresponding to players, who have greater than 0 sixes
def parse_for_six_thanfour(bat):
    toreturn  = []
    # number of six hit are in 6th column
    for i in bat:
        temp = bat[i]
        num_six = int(temp[5])
        num_four = int(temp[4])
        if num_six > num_four:
            toreturn.append(i)
    return toreturn

def parse_for_1boundary(bat):
    toreturn  = []
    # number of boundary hit are in 5th column
    for i in bat:
        temp = bat[i]
        runs = int(temp[1])
      #  print i + '->' + str(num_four)
        if runs > 50:
            toreturn.append(i)
    return toreturn

def parse_for_1wicket(ball):
    toreturn  = []
    # number of boundary hit are in 5th column
    for i in ball:
        temp = ball[i]
        num_wickets = int(temp[3])
        if num_wickets > 0:
            toreturn.append(i)
    return toreturn


def parse_for_50runs(bat):
    toreturn  = []
    # number of boundary hit are in 5th column
    for i in bat:
        temp = bat[i]
        runs = int(temp[1])
      #  print i + '->' + str(num_four)
        if runs > 50:
            toreturn.append(i)
    return toreturn

def parse_for_scorehundred(bat):
    toreturn  = []
    for i in bat:
        temp = bat[i]
        runs = int(temp[1])
        if runs > 99:
            toreturn.append(i)
    return toreturn

def parse_for_nowickets(ball):
    toreturn  = []
    # number of boundary hit are in 5th column
    for i in ball:
        temp = ball[i]
        wickets = int(temp[3])
        if wickets == 0:
            toreturn.append(i)
    return toreturn

def parse_for_rhb_bowlers(balls,profile):
    toreturn  = []
    # team for which player plays is in 3rd column
    for i in balls:
        temp = profile[i]
        temp1 = temp[-1]
        if 'right' in temp1 or 'Right' in temp1:
            if (int(balls[i][3])>0):
                toreturn.append(i)
    return toreturn


def parse_for_lhb_bowlers(balls,profile):
    toreturn  = []
    # team for which player plays is in 3rd column
    for i in balls:
        temp = profile[i]
        temp1 = temp[-1]
        if 'left' in temp1 or 'Left' in temp1:
            if (int(balls[i][3])>0):
                toreturn.append(i)
    return toreturn

def parse_for_7overs(ball):
    toreturn  = []
    for i in ball:
        temp = ball[i]
        overs = float(temp[0])
        if overs > 7:
            toreturn.append(i)
    return toreturn

def parse_for_economygr8_than8(ball):
    toreturn  = []
    for i in ball:
        temp = ball[i]
        economy = float(temp[4])
        if economy > 8.00:
            toreturn.append(i)
    return toreturn

mom = []
def parse_gt2player_match(player_match):
    toreturn  = []
    for i in player_match:
        temp = player_match[i]
        player = temp[0]
        if player in mom:
            toreturn.append(player)
        else:
            mom.insert(len(mom),player)
    return toreturn

# the function to make the model and answer the query, given the properly formatted strings
def make_model_and_answer(v, query, name_to_var):
        val = nltk.parse_valuation(v)
        dom = val.domain
        m = nltk.Model(dom, val)
        g = nltk.Assignment(dom, [])
        result = m.evaluate(query, g)
        # to show the variable (corresponding to player names) for which "srate(x) -> gtsix(x) you can do
        if result:
            l = nltk.LogicParser()
            c1 = l.parse(' ((m_of_match(x)) & (m_of_match(x) -> players_winteam(x)))')
            varnames =  m.satisfiers(c1, 'x', g)
            for i in varnames:
                for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
                    if q == i:
                        if p not in query3_ans:
                            query1_ans.insert(len(query1_ans),p)
        return result

def generate_and_solve_query1(m_of_match,winning_team,profile):
    # for this query, we only need to consider the columns in bats dictionary
    var=m_of_match[0]
    c1 = [var]
    c2 = parse_for_players_winteam(profile,winning_team)
    name_to_var = {}
    count = 0;
    for i in profile:
        if i not in name_to_var:
            name_to_var[i] = 'r' + str(count)
            count += 1
    # Now for creating a Model, we need to write down a string which shows mapping from predicates to varible names
    temp_strin1 = ''
    for i in name_to_var:
        temp_strin1 += i + ' => ' + name_to_var[i] + '\n'

    # this is for the predicate "m_of_match"
    temp_strin2 = 'm_of_match => {'
    for i in c1:
        temp_strin2 += name_to_var[i] +  ','
    temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
    temp_strin2 += '} \n'
    #now for the predicate "players_winteam"
    temp_strin3 = 'players_winteam => {'
    if c2!=[]:
        for i in c2:
            temp_strin3 += name_to_var[i] + ','
        temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
    temp_strin3 += '}'
    v = temp_strin1 + temp_strin2 + temp_strin3

    # now forming the query
    query = 'all x (m_of_match(x) -> players_winteam(x))'
    result = make_model_and_answer(v, query, name_to_var)
    return result

# the function to make the model and answer the query, given the properly formatted strings
def make_model_and_answer2(v, query, name_to_var):
        val = nltk.parse_valuation(v)
        dom = val.domain
        #print query
        #print val
        m = nltk.Model(dom, val)
        g = nltk.Assignment(dom, [])
        result = m.evaluate(query, g)
       # print "111"
        #print result
        # to show the variable (corresponding to player names) for which "srate(x) -> gtsix(x) you can do
        if result:
            l = nltk.LogicParser()
            c1 = l.parse('((duck(x)) & players_losing_team(x))')
            varnames =  m.satisfiers(c1, 'x', g)
            for i in varnames:
                for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
                    if q == i:
                        query2_ans.insert(len(query2_ans),p)
        return result



def generate_and_solve_query2(bats,winning_team,profile):
    c1 = parse_for_duck(bats);
    c2 = parse_for_players_losing_team(winning_team,profile);
    name_to_var = {}
    count = 0;
    for i in profile:
        if i not in name_to_var:
            name_to_var[i] = 'r' + str(count)
            count += 1
    # Now for creating a Model, we need to write down a string which shows mapping from predicates to varible names
    temp_strin1 = ''
    for i in name_to_var:
        temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
    # this is for the predicate "duck"
    temp_strin2 = 'duck => {'
    if c1!=[]:
        for i in c1:
            temp_strin2 += name_to_var[i] +  ','
        temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
    temp_strin2 += '} \n'
    #now for the predicate "players_winteam"
    temp_strin3 = 'players_losing_team => {'
    if c2!=[]:
        for i in c2:
            temp_strin3 += name_to_var[i] + ','
        temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
    temp_strin3 += '}'
    v = temp_strin1 + temp_strin2 + temp_strin3
    # now forming the query
    query = 'exists x (duck(x) & players_losing_team(x))'
    result = make_model_and_answer2(v, query, name_to_var)
    return result

def make_model_and_answer3(v, query, name_to_var):
    val = nltk.parse_valuation(v)
    dom = val.domain
    m = nltk.Model(dom, val)
    g = nltk.Assignment(dom, [])
    result = m.evaluate(query, g)
    #print "11111"
   # print result
    # to show the variable (corresponding to player names) for which "srate(x) -> gtsix(x) you can do
    if result:
        l = nltk.LogicParser()
        c1 = l.parse('(srate(x) -> gtsixthan4(x)))')
        varnames =  m.satisfiers(c1, 'x', g)
        for i in varnames:
            for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
                if q == i:
                    if p not in query3_ans:
                        query3_ans.insert(len(query3_ans),p)
    return result

def generate_and_solve_query3(bats):
    # for this query, we only need to consider the columns in bats dictionary
    c1 = parse_for_sr(bats, 200.0)
    c2 = parse_for_six_thanfour(bats)
    #Now constructing strings which are needed to create the model:
    name_to_var = {}
    count = 0
    for i in bats:
        if i not in name_to_var:
            name_to_var[i] = 'r' + str(count)
            count += 1
    # Now for creating a Model, we need to write down a string which shows mapping from predicates to varible names
    temp_strin1 = ''
    for i in name_to_var:
        temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
    # this is for the predicate "srate"
    temp_strin2 = 'srate => {'
    if c1!=[]:
        for i in c1:
            temp_strin2 += name_to_var[i] +  ','
        temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
    temp_strin2 += '} \n'
    #now for the predicate "gtsixthan4"
    temp_strin3 = 'gtsixthan4 => {'
    if c2!=[]:
        for i in c2:
            temp_strin3 += name_to_var[i] + ','
        temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
    temp_strin3 += '}'
    v = temp_strin1 + temp_strin2 + temp_strin3
   # print v
    # now forming the query
    query = 'all x (srate(x) & srate(x) -> gtsixthan4(x))'
    result = make_model_and_answer3(v, query, name_to_var)
    return result

def query3_parse(info1,info2,info3,info4,info5,info6,info7,info8,info9,info10):
	dict1={}
	dict2={}
	lis1=[]
	lis2=[]
	lis3=[]
	lis4=[]
	lis5=[]
	lis6=[]
	lis7=[]
	lis8=[]
	lis9=[]
	lis10=[]
	lis11=[]
	lis12=[]
	lis13=[]
	lis14=[]
	lis15=[]
	lis16=[]
	lis17=[]
	lis18=[]
	lis19=[]
	lis20=[]

	for k in info1:
		p=info1[k]
		if float(p[6])>200:
			lis1.append(k)
		if int(p[5])>int(p[4]):
			lis11.append(k)
	for i in info2.keys():
		if float(info2.get(i)[-1])>200:
			lis2.append(i)
		if int(info2.get(i)[5])>int(info2.get(i)[4]):
			lis12.append(i)
	for i in info3.keys():
		if float(info3.get(i)[-1])>200:
			lis3.append(i)
		if int(info3.get(i)[5])>int(info3.get(i)[4]):
			lis13.append(i)
	for i in info4.keys():
		if float(info4.get(i)[-1])>200:
			lis4.append(i)
		if int(info4.get(i)[5])>int(info4.get(i)[4]):
			lis14.append(i)
	for i in info5.keys():
		if float(info5.get(i)[-1])>200:
			lis5.append(i)
		if int(info5.get(i)[5])>int(info5.get(i)[4]):
			lis15.append(i)
	for i in info6.keys():
		if float(info6.get(i)[-1])>200:
			lis6.append(i)
		if int(info6.get(i)[5])>int(info6.get(i)[4]):
			lis16.append(i)
	for i in info7.keys():
		if float(info7.get(i)[-1])>200:
			lis7.append(i)
		if int(info7.get(i)[5])>int(info7.get(i)[4]):
			lis17.append(i)
	for i in info8.keys():
		if float(info8.get(i)[-1])>200:
			lis8.append(i)
		if int(info8.get(i)[5])>int(info8.get(i)[4]):
			lis18.append(i)
	for i in info9.keys():
		if float(info9.get(i)[-1])>200:
			lis9.append(i)
		if int(info9.get(i)[5])>int(info9.get(i)[4]):
			lis19.append(i)
	for i in info10.keys():
		if float(info10.get(i)[-1])>200:
			lis10.append(i)
		if int(info10.get(i)[5])>int(info10.get(i)[4]):
			lis20.append(i)
	dict1['in1']=lis1
	dict1['in3']=lis2
	dict1['in5']=lis3
	dict1['in7']=lis4
	dict1['in9']=lis5
	dict1['in2']=lis6
	dict1['in4']=lis7
	dict1['in6']=lis8
	dict1['in8']=lis9
	dict1['in10']=lis10
	dict2['in1']=lis11
	dict2['in3']=lis12
	dict2['in5']=lis13
	dict2['in7']=lis14
	dict2['in9']=lis15
	dict2['in2']=lis16
	dict2['in4']=lis17
	dict2['in6']=lis18
	dict2['in8']=lis19
	dict2['in10']=lis20

	return dict1,dict2



def make_model_and_answer4(v, query, name_to_var):
    val = nltk.parse_valuation(v)
    dom = val.domain
    m = nltk.Model(dom, val)
    g = nltk.Assignment(dom, [])
    result = m.evaluate(query, g)
    # to show the variable (corresponding to player names) for which "srate(x) -> gtsix(x) you can do
    if result:
        l = nltk.LogicParser()
        c1 = l.parse('(belongwinteam(x) & 1boundary(x) & belowstr(x))')
        varnames =  m.satisfiers(c1, 'x', g)
        for i in varnames:
            print i
            for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
                if q == i:
                    if p not in query4_ans:
                        query4_ans.insert(len(query4_ans),p)
    return result


def generate_and_solve_query4(bats,winning_team,profile):
    c1 = parse_for_players_winteam(profile,winning_team);
    c2 = parse_for_1boundary(bats);
    c3 = parse_for_belowstr(bats,100);
#    print c1
 #   print c2
 #   print c3
    name_to_var = {}
    count = 0
    for i in profile:
        if i not in name_to_var:
            name_to_var[i] = 'r' + str(count)
            count += 1
    # Now for creating a Model, we need to write down a string which shows mapping from predicates to varible names
    temp_strin1 = ''
    for i in name_to_var:
        temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
    # this is for the predicate "srate"
    temp_strin2 = 'belongwinteam => {'
    if c1!=[]:
        for i in c1:
            temp_strin2 += name_to_var[i] +  ','
        temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
    temp_strin2 += '} \n'
    #now for the predicate "gtsixthan4"
    temp_strin3 = '1boundary => {'
    if c2!=[]:
        for i in c2:
            temp_strin3 += name_to_var[i] + ','
        temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
    temp_strin3 += '} \n'
    #print name_to_var
    temp_strin4 = 'belowstr => {'
    if c3!=[]:
        for i in c3:
            temp_strin4 += name_to_var[i] + ','
        temp_strin4 = temp_strin4[:-1]  #removing the extra "," charater
    temp_strin4 += '}'
    v = temp_strin1 + temp_strin2 + temp_strin3 + temp_strin4
    #print v
    # now forming the query
    query = 'all x (belongwinteam(x) & 1boundary(x) & belowstr(x))'
    result = make_model_and_answer4(v, query, name_to_var)
    return result

def make_model_and_answer5(v, query, name_to_var):
    val = nltk.parse_valuation(v)
    dom = val.domain
    m = nltk.Model(dom, val)
    g = nltk.Assignment(dom, [])
    result = m.evaluate(query, g)
    # to show the variable (corresponding to player names) for which "srate(x) -> gtsix(x) you can do
    if result:
        l = nltk.LogicParser()
        c1 = l.parse('(50runs(x) & 1wicket(x))')
        varnames =  m.satisfiers(c1, 'x', g)
     #   print varnames
        for i in varnames:
       #     print i
            for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
                if q == i:
                    if p not in query5_ans:
                        query5_ans.insert(len(query5_ans),p)
    return result

def  generate_and_solve_query5(bats,balls,profile):
    c1 = parse_for_50runs(bats);
    c2 = parse_for_1wicket(balls);
   # print "-----c1----"
    #print c1
   # print c2
    name_to_var = {}
    count = 0
    for i in profile:
        if i not in name_to_var:
            name_to_var[i] = 'r' + str(count)
            count += 1
    # Now for creating a Model, we need to write down a string which shows mapping from predicates to varible names
    temp_strin1 = ''
    for i in name_to_var:
        temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
    # this is for the predicate "srate"
    temp_strin2 = '50runs => {'
    if c1!=[]:
        for i in c1:
            temp_strin2 += name_to_var[i] +  ','
        temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
    temp_strin2 += '} \n'
    #now for the predicate "gtsixthan4"
    #print name_to_var
    temp_strin3 = '1wicket => {'
    if c2!=[]:
        for i in c2:
            temp_strin3 += name_to_var[i] + ','
        temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
    temp_strin3 += '}'
    v = temp_strin1 + temp_strin2 + temp_strin3
    #print v
    # now forming the query
    query = 'exists x (50runs(x) & 1wicket(x))'
    result = make_model_and_answer5(v, query, name_to_var)
    return result

def make_model_and_answer6(v, query, name_to_var):
    val = nltk.parse_valuation(v)
    dom = val.domain
    m = nltk.Model(dom, val)
    g = nltk.Assignment(dom, [])
    result = m.evaluate(query, g)
    # to show the variable (corresponding to player names) for which "srate(x) -> gtsix(x) you can do
    if result:
        l = nltk.LogicParser()
        c1 = l.parse('(nowickets(x) & 7overs(x))')
        varnames =  m.satisfiers(c1, 'x', g)
     #   print varnames
        for i in varnames:
       #     print i
            for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
                if q == i:
                    if p not in query6_ans:
                        query6_ans.insert(len(query6_ans),p)
    return result


def  generate_and_solve_query6(balls):
    c1 = parse_for_nowickets(balls);
    c2 = parse_for_7overs(balls);
   # print "-----c1----"
    #print c1
   # print c2
    name_to_var = {}
    count = 0
    for i in balls:
        if i not in name_to_var:
            name_to_var[i] = 'r' + str(count)
            count += 1
    # Now for creating a Model, we need to write down a string which shows mapping from predicates to varible names
    temp_strin1 = ''
    for i in name_to_var:
        temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
    # this is for the predicate "srate"
    temp_strin2 = 'nowickets => {'
    if c1!=[]:
        for i in c1:
            temp_strin2 += name_to_var[i] +  ','
        temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
    temp_strin2 += '} \n'
    #now for the predicate "gtsixthan4"
    temp_strin3 = '7overs => {'
    if c2!=[]:
        for i in c2:
            temp_strin3 += name_to_var[i] + ','
        temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
    temp_strin3 += '}'
    v = temp_strin1 + temp_strin2 + temp_strin3
    #print v
    # now forming the query
    query = 'exists x (nowickets(x) & 7overs(x))'
    result = make_model_and_answer6(v, query, name_to_var)
    return result

def make_model_and_answer7(v, query, name_to_var):
    val = nltk.parse_valuation(v)
    dom = val.domain
    m = nltk.Model(dom, val)
    g = nltk.Assignment(dom, [])
    result = m.evaluate(query, g)
    # to show the variable (corresponding to player names) for which "srate(x) -> gtsix(x) you can do
    if result:
        l = nltk.LogicParser()
        c1 = l.parse('(nowickets(x) & 8economy(x))')
        varnames =  m.satisfiers(c1, 'x', g)
        for i in varnames:
       #     print i
            for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
                if q == i:
                    if p not in query7_ans:
                        query7_ans.insert(len(query7_ans),p)
    return result

def  generate_and_solve_query7(balls):
    c1=parse_for_nowickets(balls);
    c2=parse_for_economygr8_than8(balls);
    name_to_var = {}
    count = 0
    for i in balls:
        if i not in name_to_var:
            name_to_var[i] = 'r' + str(count)
            count += 1
    # Now for creating a Model, we need to write down a string which shows mapping from predicates to varible names
    temp_strin1 = ''
    for i in name_to_var:
        temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
    # this is for the predicate "srate"
    temp_strin2 = 'nowickets => {'
    if c1!=[]:
        for i in c1:
            temp_strin2 += name_to_var[i] +  ','
        temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
    temp_strin2 += '} \n'
    #now for the predicate "gtsixthan4"
    temp_strin3 = '8economy => {'
    if c2!=[]:
        for i in c2:
            temp_strin3 += name_to_var[i] + ','
        temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
    temp_strin3 += '}'
    v = temp_strin1 + temp_strin2 + temp_strin3
    # now forming the query
    query = 'exists x (nowickets(x) & 8economy(x))'
    result = make_model_and_answer7(v, query, name_to_var)
    return result

def make_model_and_answer8(v, query, name_to_var):
    val = nltk.parse_valuation(v)
    dom = val.domain
    m = nltk.Model(dom, val)
    g = nltk.Assignment(dom, [])
    result = m.evaluate(query, g)
    # to show the variable (corresponding to player names) for which "srate(x) -> gtsix(x) you can do
    if result:
        l = nltk.LogicParser()
        c1 = l.parse('(scorehundred(x) & players_losingteam(x))')
        varnames =  m.satisfiers(c1, 'x', g)
        for i in varnames:
       #     print i
            for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
                if q == i:
                    if p not in query8_ans:
                        query8_ans.insert(len(query8_ans),p)
    return result

def generate_and_solve_query8(bats,winning_team,profile):
    c1 = parse_for_scorehundred(bats);
    c2 = parse_for_players_losing_team(winning_team,profile);
    name_to_var = {}
    count = 0
    for i in profile:
        if i not in name_to_var:
            name_to_var[i] = 'r' + str(count)
            count += 1
    # Now for creating a Model, we need to write down a string which shows mapping from predicates to varible names
    temp_strin1 = ''
    for i in name_to_var:
        temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
    # this is for the predicate "srate"
    temp_strin2 = 'scorehundred=> {'
    if c1!=[]:
        for i in c1:
            temp_strin2 += name_to_var[i] +  ','
        temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
 #   else:
  #      temp_strin2 += ' '
    temp_strin2 += '} \n'
    #now for the predicate "gtsixthan4"
    temp_strin3 = 'players_losingteam => {'
    if c2!=[]:
        for i in c2:
            temp_strin3 += name_to_var[i] + ','
        temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
    temp_strin3 += '}'
    v = temp_strin1 + temp_strin2 + temp_strin3
    # now forming the query
    query = 'exists x (scorehundred(x) & players_losingteam(x))'
    result = make_model_and_answer8(v, query, name_to_var)
    return result

def wickets_claimed_rhb(balls,c1):
    rhb_wickets = 0;
    for bowler in c1:
        if bowler in balls:
            temp = balls[bowler];
            temp1 = int(temp[3])
            rhb_wickets += temp1
    return rhb_wickets

def wickets_claimed_lhb(balls,c2):
    lhb_wickets = 0;
    for bowler in c2:
        if bowler in balls:
            temp = balls[bowler];
            temp1 = int(temp[3])
            lhb_wickets += temp1
    return lhb_wickets

def make_model_and_answer9(v, query, name_to_var):
    val = nltk.parse_valuation(v)
    #print val
    dom = val.domain
    m = nltk.Model(dom, val)
    g = nltk.Assignment(dom, [])
    result = m.evaluate(query, g)
    # to show the variable (corresponding to player names) for which "srate(x) -> gtsix(x) you can do
    if result:
        l = nltk.LogicParser()
        c1 = l.parse('(rhb_bowlers_btlhb(x))')
        varnames =  m.satisfiers(c1, 'x', g)
        for i in varnames:
       #     print i
            for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
                if q == i:
                    if p not in query9_ans:
                        query9_ans.insert(len(query9_ans),p)
    return result


def parse_for_rhb_gtlhb(balls,profile):
    c1 = parse_for_rhb_bowlers(balls,profile);
    c2 = parse_for_lhb_bowlers(balls,profile);
    right_wickets = wickets_claimed_rhb(balls,c1);
    left_wickets = wickets_claimed_lhb(balls,c2);
    if right_wickets > left_wickets:
        toreturn = c1;
    else:
        toreturn = []
    return toreturn

def generate_and_solve_query9(balls,profile):
    c1 = parse_for_rhb_gtlhb(balls,profile);
    name_to_var = {}
    count = 0
    for i in balls:
        if i not in name_to_var:
            name_to_var[i] = 'r' + str(count)
            count += 1
    # Now for creating a Model, we need to write down a string which shows mapping from predicates to varible names
    temp_strin1 = ''
    for i in name_to_var:
        temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
    # this is for the predicate "srate"
    temp_strin2 = 'rhb_bowlers_btlhb=> {'
    if c1!=[]:
        for i in c1:
            temp_strin2 += name_to_var[i] +  ','
        temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
 #   else:
  #      temp_strin2 += ' '
    temp_strin2 += '}'
    #now for the predicate "gtsixthan4"
 #   temp_strin3 = 'lhb_bowlers => {'
#    if c2!=[]:
     #   for i in c2:
      #      temp_strin3 += name_to_var[i] + ','
      #  temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
   # temp_strin3 += '}'
    v = temp_strin1 + temp_strin2
   # print v
    # now forming the query
    query = 'exists x (rhb_bowlers_btlhb(x))'
    result = make_model_and_answer9(v, query, name_to_var)
    return result

def make_model_and_answer10(v, query, name_to_var):
    val = nltk.parse_valuation(v)
    dom = val.domain
    m = nltk.Model(dom, val)
    g = nltk.Assignment(dom, [])
    result = m.evaluate(query, g)
    # to show the variable (corresponding to player names) for which "srate(x) -> gtsix(x) you can do
    if result:
        l = nltk.LogicParser()
        c1 = l.parse('(lessthan26(x) & gt250run(x) & noducks(x))')
        varnames =  m.satisfiers(c1, 'x', g)
        for i in varnames:
       #     print i
            for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
                if q == i:
                    if p not in query10_ans:
                        query10_ans.insert(len(query10_ans),p)
    return result


def generate_and_solve_query10(bats1,bats2,bats3,bats4,bats5,profile):
    c1 = parse_lessthan26(profile);
    c2 = parse_250run(bats1,bats2,bats3,bats4,bats5);
    c3 = no_ducks;
    name_to_var = {}
    count = 0
    for i in profile:
        if i not in name_to_var:
            name_to_var[i] = 'r' + str(count)
            count += 1
    temp_strin1 = ''
    for i in name_to_var:
        temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
    temp_strin2 = 'lessthan26=> {'
    if c1!=[]:
        for i in c1:
            temp_strin2 += name_to_var[i] +  ','
        temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
    temp_strin2 += '}\n'
    temp_strin3 = 'gt250run => {'
    if c2!=[]:
        for i in c2:
            temp_strin3 += name_to_var[i] + ','
        temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
    temp_strin3 += '}\n'
    temp_strin4 = 'noducks => {'
    if c3!=[]:
        for i in c3:
            temp_strin4 += name_to_var[i] + ','
        temp_strin4 = temp_strin4[:-1]  #removing the extra "," charater
    temp_strin4 += '}'
    v = temp_strin1 + temp_strin2 + temp_strin3 + temp_strin4
    # now forming the query
    query = 'exists x (lessthan26(x) & gt250run(x) & noducks(x))'
    result = make_model_and_answer10(v, query, name_to_var)
    return result

def parse_players_odi(bats,balls):
    toreturn = []
    for i in bats:
        toreturn.append(i);
    for i in balls:
        if i not in toreturn:
            toreturn.append(i);
    return toreturn

def make_model_and_answer11(v, query, name_to_var):
    val = nltk.parse_valuation(v)
    dom = val.domain
    m = nltk.Model(dom, val)
    g = nltk.Assignment(dom, [])
    result = m.evaluate(query, g)
    # to show the variable (corresponding to player names) for which "srate(x) -> gtsix(x) you can do
    if result:
        l = nltk.LogicParser()
        c1 = l.parse('played_1odi(x) & played_2odi(x) & played_3odi(x) & played_4odi(x) & played_5odi(x)')
        varnames =  m.satisfiers(c1, 'x', g)
        for i in varnames:
       #     print i
            for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
                if q == i:
                    if p not in query11_ans:
                        query11_ans.insert(len(query11_ans),p)
    return result


def generate_and_solve_query11(bats1,bats2,bats3,bats4,bats5,balls1,balls2,balls3,balls4,balls5,profile):
    c1 = parse_players_odi(bats1,balls1);
    c2 = parse_players_odi(bats2,balls2);
    c3 = parse_players_odi(bats3,balls3);
    c4 = parse_players_odi(bats4,balls4);
    c5 = parse_players_odi(bats5,balls5);
    name_to_var = {}
    count = 0
    for i in profile:
        if i not in name_to_var:
            name_to_var[i] = 'r' + str(count)
            count += 1
    temp_strin1 = ''
    for i in name_to_var:
        temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
    temp_strin2 = 'played_1odi=> {'
    if c1!=[]:
        for i in c1:
            temp_strin2 += name_to_var[i] +  ','
        temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
    temp_strin2 += '}\n'
    temp_strin3 = 'played_2odi => {'
    if c2!=[]:
        for i in c2:
            temp_strin3 += name_to_var[i] + ','
        temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
    temp_strin3 += '}\n'
    temp_strin4 = 'played_3odi => {'
    if c3!=[]:
        for i in c3:
            temp_strin4 += name_to_var[i] + ','
        temp_strin4 = temp_strin4[:-1]  #removing the extra "," charater
    temp_strin4 += '}\n'
    temp_strin5 = 'played_4odi => {'
    if c4!=[]:
        for i in c4:
            temp_strin5 += name_to_var[i] + ','
        temp_strin5 = temp_strin5[:-1]  #removing the extra "," charater
    temp_strin5 += '}\n'
    temp_strin6 = 'played_5odi => {'
    if c5!=[]:
        for i in c5:
            temp_strin6 += name_to_var[i] + ','
        temp_strin6 = temp_strin6[:-1]  #removing the extra "," charater
    temp_strin6 += '}'
    v = temp_strin1 + temp_strin2 + temp_strin3 + temp_strin4 + temp_strin5 + temp_strin6
    # now forming the query
    query = 'exists x (played_1odi(x) & played_2odi(x) & played_3odi(x) & played_4odi(x) & played_5odi(x))'
    result = make_model_and_answer11(v, query, name_to_var)
    return result

wides={}
def parse_greaterwides_thanjadeja(balls1,balls2,balls3,balls4,balls5):
    player1_wides = 0;
    player2_wides = 0;
    for i in balls1:
        details = balls1[i]
        if len(details) == 6:
            temp = details[5]
            wides_nb = temp.split(',')
            if 'w' in wides_nb[len(wides_nb)-1]:
                j=0;
                wides[i] = 0;
                while wides_nb[len(wides_nb)-1][j]!='w':
                    if wides_nb[len(wides_nb)-1][j]!= '(':
                        wides[i] += int(wides_nb[len(wides_nb)-1][j])
                    j = j+1;
        else:
            wides[i] = 0
    for i in balls2:
        details = balls2[i]
        if len(details) == 6:
            temp = details[5]
            wides_nb = temp.split(',')
            if 'w' in wides_nb[len(wides_nb)-1]:
                j=0;
                if i not in wides:
                    wides[i] = 0;
                while wides_nb[len(wides_nb)-1][j]!='w':
                    if wides_nb[len(wides_nb)-1][j]!= '(':
                        wides[i] += int(wides_nb[len(wides_nb)-1][j])
                    j = j+1;
        else:
            if i not in wides:
                wides[i] = 0
    for i in balls3:
        details = balls3[i]
        if len(details) == 6:
            temp = details[5]
            wides_nb = temp.split(',')
            if 'w' in wides_nb[len(wides_nb)-1]:
                j=0;
                if i not in wides:
                    wides[i] = 0;
                while wides_nb[len(wides_nb)-1][j]!='w':
                    if wides_nb[len(wides_nb)-1][j]!= '(':
                        wides[i] += int(wides_nb[len(wides_nb)-1][j])
                    j = j+1;
        else:
            if i not in wides:
                wides[i] = 0
    for i in balls4:
        details = balls4[i]
        if len(details) == 6:
            temp = details[5]
            wides_nb = temp.split(',')
            if 'w' in wides_nb[len(wides_nb)-1]:
                j=0;
                if i not in wides:
                    wides[i] = 0;
                while wides_nb[len(wides_nb)-1][j]!='w':
                    if wides_nb[len(wides_nb)-1][j]!= '(':
                        wides[i] += int(wides_nb[len(wides_nb)-1][j])
                    j = j+1;
        else:
            if i not in wides:
                wides[i] = 0
    for i in balls5:
        details = balls5[i]
        if len(details) == 6:
            temp = details[5]
            wides_nb = temp.split(',')
            if 'w' in wides_nb[len(wides_nb)-1]:
                j=0;
                if i not in wides:
                    wides[i] = 0;
                while wides_nb[len(wides_nb)-1][j]!='w':
                    if wides_nb[len(wides_nb)-1][j]!= '(':
                        wides[i] += int(wides_nb[len(wides_nb)-1][j])
                    j = j+1;
        else:
            if i not in wides:
                wides[i] = 0
    wides_jadeja = wides['RA Jadeja']
#    print wides_jadeja
    toreturn=[]
    for i in wides:
        if wides[i] > wides_jadeja:
           # if i == 'I Sharma':
            #    print wides[i]
            toreturn.append(i)
    return toreturn

catches={}
def parse_greatercatches_thanryder(bats1,bats2,bats3,bats4,bats5):
    for i in bats1:
        details = bats1[i]
        temp = details[0]
        if temp[0] == 'c' and temp[1] == ' ':
            if 'c & b' in temp:
                if temp[6:] in catches:
                    catches[temp[6:]] += 1;
                else:
                    catches[temp[6:]] = 1;
            else:
                temp1 = temp.split(' b ')
                temp2 = temp1[0].split('c ')
                if temp2[1] in catches:
                    catches[temp2[1]] += 1;
                else:
                    catches[temp2[1]] = 1;
    for i in bats2:
        details = bats2[i]
        temp = details[0]
        if temp[0] == 'c' and temp[1] == ' ':
            if 'c & b' in temp:
                if temp[6:] in catches:
                    catches[temp[6:]] += 1;
                else:
                    catches[temp[6:]] = 1;
            else:
                temp1 = temp.split(' b ')
                temp2 = temp1[0].split('c ')
                if temp2[1] in catches:
                    catches[temp2[1]] += 1;
                else:
                    catches[temp2[1]] = 1;
    for i in bats3:
        details = bats3[i]
        temp = details[0]
        if temp[0] == 'c' and temp[1] == ' ':
            if 'c & b' in temp:
                if temp[6:] in catches:
                    catches[temp[6:]] += 1;
                else:
                    catches[temp[6:]] = 1;
            else:
                temp1 = temp.split(' b ')
                temp2 = temp1[0].split('c ')
                if temp2[1] in catches:
                    catches[temp2[1]] += 1;
                else:
                    catches[temp2[1]] = 1;
    for i in bats4:
        details = bats4[i]
        temp = details[0]
        if temp[0] == 'c' and temp[1] == ' ':
            if 'c & b' in temp:
                if temp[6:] in catches:
                    catches[temp[6:]] += 1;
                else:
                    catches[temp[6:]] = 1;
            else:
                temp1 = temp.split(' b ')
                temp2 = temp1[0].split('c ')
                if temp2[1] in catches:
                    catches[temp2[1]] += 1;
                else:
                    catches[temp2[1]] = 1;
    for i in bats5:
        details = bats5[i]
        temp = details[0]
        if temp[0] == 'c' and temp[1] == ' ':
            if 'c & b' in temp:
                if temp[6:] in catches:
                    catches[temp[6:]] += 1;
                else:
                    catches[temp[6:]] = 1;
            else:
                temp1 = temp.split(' b ')
                temp2 = temp1[0].split('c ')
                if temp2[1] in catches:
                    catches[temp2[1]] += 1;
                else:
                    catches[temp2[1]] = 1;
    catches_ryder = catches['Ryder']
    toreturn=[]
    for i in catches:
        if catches[i] > catches_ryder:
            toreturn.append(i)
    return toreturn



def make_model_and_answer12(v, query, name_to_var):
    val = nltk.parse_valuation(v)
    dom = val.domain
    m = nltk.Model(dom, val)
    g = nltk.Assignment(dom, [])
    result =  m.evaluate(query, g)
    # to show the variable (corresponding to player names) for which "srate(x) -> gtsix(x) you can do
    return result

def generate_and_solve_query12(balls1,balls2,balls3,balls4,balls5):
 #   wickets_gr8jadeja = parse_greaterwides_thanjadeja(balls1,balls2,balls3,balls4,balls5);
    c1 = ['I Sharma'];
    c2 = parse_greaterwides_thanjadeja(balls1,balls2,balls3,balls4,balls5);
    name_to_var = {}
    count = 0
    for i in wides:
        name_to_var[i] = 'r' + str(count)
        count += 1
    temp_strin1 = ''
    for i in name_to_var:
        temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
    temp_strin2 = 'is_IshantSharma => {'
    if c1!=[]:
        for i in c1:
            temp_strin2 += name_to_var[i] +  ','
        temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
    temp_strin2 += '}\n'
    temp_strin3 = 'widesgt_RJadeja => {'
    if c2!=[]:
        for i in c2:
            temp_strin3 += name_to_var[i] + ','
        temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
    temp_strin3 += '}'
    v = temp_strin1 + temp_strin2 + temp_strin3
    # now forming the query
    query = 'exists x(widesgt_RJadeja(x) & is_IshantSharma(x))'
    result = make_model_and_answer12(v, query, name_to_var)
    return result

def make_model_and_answer13(v, query, name_to_var):
    val = nltk.parse_valuation(v)
    dom = val.domain
    m = nltk.Model(dom, val)
    g = nltk.Assignment(dom, [])
    result = m.evaluate(query, g)
    # to show the variable (corresponding to player names) for which "srate(x) -> gtsix(x) you can do
    if result:
        l = nltk.LogicParser()
        c1 = l.parse('(catches_gtRyder(x) & is_Southee(x))')
        varnames =  m.satisfiers(c1, 'x', g)
        for i in varnames:
            for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
                if q == i:
                    if p not in query13_ans:
                        query13_ans.insert(len(query13_ans),p)
    return result


def generate_and_solve_query13(bats1,bats2,bats3,bats4,bats5):
    c1 = ['Southee'];
    c2 = parse_greatercatches_thanryder(bats1,bats2,bats3,bats4,bats5);
    name_to_var = {}
    count = 0
    for i in catches:
        name_to_var[i] = 'r' + str(count)
        count += 1
    temp_strin1 = ''
    for i in name_to_var:
        temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
    temp_strin2 = 'catches_gtRyder => {'
    if c2!=[]:
        for i in c2:
            temp_strin2 += name_to_var[i] + ','
        temp_strin2 = temp_strin2[:-1]  #removing the extra "," charater
    temp_strin2 += '}\n'
    temp_strin3 = 'is_Southee => {'
    if c1!=[]:
        for i in c1:
            temp_strin3 += name_to_var[i] + ','
        temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
    temp_strin3 += '}'
    v = temp_strin1 + temp_strin2 + temp_strin3
    # now forming the query
    query = 'exists x(catches_gtRyder(x) & is_Southee(x))'
    result = make_model_and_answer13(v, query, name_to_var)
    return result

def make_model_and_answer14(v, query, name_to_var):
    val = nltk.parse_valuation(v)
    dom = val.domain
    m = nltk.Model(dom, val)
    g = nltk.Assignment(dom, [])
    result = m.evaluate(query, g)
    # to show the variable (corresponding to player names) for which "srate(x) -> gtsix(x) you can do
    if result:
        l = nltk.LogicParser()
        c1 = l.parse('(gt2player_match(x))')
        varnames =  m.satisfiers(c1, 'x', g)
        for i in varnames:
            for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
                if q == i:
                    if p not in query14_ans:
                        query14_ans.insert(len(query14_ans),p)
    return result


def generate_and_solve_query14(player_match,profile):
    c1 = parse_gt2player_match(player_match);
    name_to_var = {}
    count = 0
    for i in profile:
        name_to_var[i] = 'r' + str(count)
        count += 1
    temp_strin1 = ''
    for i in name_to_var:
        temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
    temp_strin2 = 'gt2player_match => {'
    if c1!=[]:
        for i in c1:
            temp_strin2 += name_to_var[i] + ','
        temp_strin2 = temp_strin2[:-1]  #removing the extra "," charater
    temp_strin2 += '}'
    v = temp_strin1 + temp_strin2
    # now forming the query
    query = 'exists x(gt2player_match(x))'
    result = make_model_and_answer14(v, query, name_to_var)
    return result

bowler_1inn={}
bowler_2inn={}
def parse_1inn_btter_2inn(ball12,ball11,ball21,ball22,ball32,ball31,ball42,ball41,ball51,ball52):
    for i in ball11:
        details = ball11[i]
       # details = details.split(',')
        wickets = float(details[3])
        economy = float(details[4])
        if i in bowler_1inn:
            bowler_1inn[i] += ((3*wickets));
        else:
            bowler_1inn[i] = (3*wickets);
    for i in ball21:
        details = ball21[i]
       # details = details.split(',')
        wickets = float(details[3])
        economy = float(details[4])
        if i in bowler_1inn:
            bowler_1inn[i] += ((3*wickets));
        else:
            bowler_1inn[i] = (3*wickets);
    for i in ball31:
        details = ball31[i]
       # details = details.split(',')
        wickets = float(details[3])
        economy = float(details[4])
        if i in bowler_1inn:
            bowler_1inn[i] += ((3*wickets));
        else:
            bowler_1inn[i] = (3*wickets);
    for i in ball41:
        details = ball41[i]
     #   details = details.split(',')
        wickets = float(details[3])
        economy = float(details[4])
        if i in bowler_1inn:
            bowler_1inn[i] += ((3*wickets));
        else:
            bowler_1inn[i] = (3*wickets);
    for i in ball51:
        details = ball51[i]
      #  details = details.split(',')
        wickets = float(details[3])
        economy = float(details[4])
        if i in bowler_1inn:
            bowler_1inn[i] += ((3*wickets));
        else:
            bowler_1inn[i] = (3*wickets);

    for i in ball12:
        details = ball12[i]
       # details = details.split(',')
        wickets = float(details[3])
        economy = float(details[4])
        if i in bowler_2inn:
            bowler_2inn[i] += (3*wickets);
        else:
            bowler_2inn[i] = (3*wickets);
    for i in ball22:
        details = ball22[i]
   #     details = details.split(',')
        wickets = float(details[3])
        economy = float(details[4])
        if i in bowler_2inn:
            bowler_2inn[i] += (3*wickets);
        else:
            bowler_2inn[i] = (3*wickets);
    for i in ball32:
        details = ball32[i]
    #    details = details.split(',')
        wickets = float(details[3])
        economy = float(details[4])
        if i in bowler_2inn:
            bowler_2inn[i] += (3*wickets);
        else:
            bowler_2inn[i] = (3*wickets);
    for i in ball42:
        details = ball42[i]
     #   details = details.split(',')
        wickets = float(details[3])
        economy = float(details[4])
        if i in bowler_2inn:
            bowler_2inn[i] += (3*wickets);
        else:
            bowler_2inn[i] = (3*wickets);
    for i in ball52:
        details = ball52[i]
      #  details = details.split(',')
        wickets = float(details[3])
        economy = float(details[4])
        if i in bowler_2inn:
            bowler_2inn[i] += (3*wickets);
        else:
            bowler_2inn[i] = (3*wickets);
    toreturn = []
    for i in bowler_1inn:
        if i in bowler_2inn:
            if bowler_1inn[i] > bowler_2inn[i]:
                toreturn.append(i)
    return toreturn
def make_model_and_answer15(v, query, name_to_var):
    val = nltk.parse_valuation(v)
    dom = val.domain
    m = nltk.Model(dom, val)
    g = nltk.Assignment(dom, [])
    result = m.evaluate(query, g)
    # to show the variable (corresponding to player names) for which "srate(x) -> gtsix(x) you can do
    if result:
        l = nltk.LogicParser()
        c1 = l.parse('(better1inn_than_2inn(x) & is_jadeja(x))')
        varnames =  m.satisfiers(c1, 'x', g)
        for i in varnames:
       #     print i
            for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
                if q == i:
                    if p not in query15_ans:
                        query15_ans.insert(len(query15_ans),p)
    return result



def generate_and_solve_query15(ball12,ball11,ball21,ball22,ball32,ball31,ball41,ball42,ball51,ball52):
    c2 = parse_1inn_btter_2inn(ball12,ball11,ball21,ball22,ball32,ball31,ball41,ball42,ball51,ball52);
    c1 = ['RA Jadeja'];
    name_to_var = {}
    count = 0
    for i in bowler_1inn:
        name_to_var[i] = 'r' + str(count)
        count += 1
    temp_strin1 = ''
    for i in name_to_var:
        temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
    temp_strin2 = 'better1inn_than_2inn => {'
    if c2!=[]:
        for i in c2:
            temp_strin2 += name_to_var[i] + ','
        temp_strin2 = temp_strin2[:-1]  #removing the extra "," charater
    temp_strin2 += '}\n'
    temp_strin3 = 'is_jadeja => {'
    if c1!=[]:
        for i in c1:
            temp_strin3 += name_to_var[i] + ','
        temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
    temp_strin3 += '}'
    v = temp_strin1 + temp_strin2 + temp_strin3
    # now forming the query
    query = 'exists x(better1inn_than_2inn(x) & is_jadeja(x))'
    result = make_model_and_answer15(v, query, name_to_var)
    return result

betterthan_jadeja={}
def parse_bttrthan_jadeja(balls1,balls2,balls3,balls4,balls5):
    for i in balls1:
        details = balls1[i]
       # details = details.split(',')
        wickets = float(details[3])
        economy = float(details[4])
        if i in betterthan_jadeja:
            betterthan_jadeja[i] += ((wickets));
        else:
           betterthan_jadeja[i] = (wickets);
    for i in balls2:
        details = balls2[i]
        wickets = float(details[3])
        economy = float(details[4])
        if i in betterthan_jadeja:
           betterthan_jadeja[i] += ((wickets));
        else:
           betterthan_jadeja[i] = (wickets);
    for i in balls3:
        details = balls3[i]
       # details = details.split(',')
        wickets = float(details[3])
        economy = float(details[4])
        if i in betterthan_jadeja:
            betterthan_jadeja[i] += ((wickets));
        else:
            betterthan_jadeja[i] = (wickets);
    for i in balls4:
        details = balls4[i]
     #   details = details.split(',')
        wickets = float(details[3])
        economy = float(details[4])
        if i in betterthan_jadeja:
            betterthan_jadeja[i] += ((wickets));
        else:
            betterthan_jadeja[i] = (wickets);
    for i in balls5:
        details = balls5[i]
      #  details = details.split(',')
        wickets = float(details[3])
        economy = float(details[4])
        if i in betterthan_jadeja:
            betterthan_jadeja[i] += ((wickets));
        else:
            betterthan_jadeja[i] = (wickets);
    toreturn = []
    jadeja_heuristic = betterthan_jadeja['RA Jadeja']
    for i in betterthan_jadeja:
        if betterthan_jadeja[i] > jadeja_heuristic:
                toreturn.append(i)
    return toreturn

def make_model_and_answer17(v, query, name_to_var):
    val = nltk.parse_valuation(v)
    dom = val.domain
    m = nltk.Model(dom, val)
    g = nltk.Assignment(dom, [])
    result = m.evaluate(query, g)
    # to show the variable (corresponding to player names) for which "srate(x) -> gtsix(x) you can do
    return result


def generate_and_solve_query17(balls1,balls2,balls3,balls4,balls5):
    c2 = parse_bttrthan_jadeja(balls1,balls2,balls3,balls4,balls5);
    c1 = ['I Sharma'];
    name_to_var = {}
    count = 0
    for i in balls1:
        if i not in name_to_var:
            name_to_var[i] = 'r' + str(count)
            count += 1
    for i in balls2:
        if i not in name_to_var:
            name_to_var[i] = 'r' + str(count)
            count += 1
    for i in balls3:
        if i not in name_to_var:
            name_to_var[i] = 'r' + str(count)
            count += 1
    for i in balls4:
        if i not in name_to_var:
            name_to_var[i] = 'r' + str(count)
            count += 1
    for i in balls5:
        if i not in name_to_var:
            name_to_var[i] = 'r' + str(count)
            count += 1
    temp_strin1 = ''
    for i in name_to_var:
        temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
    temp_strin2 = 'better_than_jadeja => {'
    if c2!=[]:
        for i in c2:
            temp_strin2 += name_to_var[i] + ','
        temp_strin2 = temp_strin2[:-1]  #removing the extra "," charater
    temp_strin2 += '}\n'
    temp_strin3 = 'is_ishant => {'
    if c1!=[]:
        for i in c1:
            temp_strin3 += name_to_var[i] + ','
        temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
    temp_strin3 += '}'
    v = temp_strin1 + temp_strin2 + temp_strin3
    # now forming the query
    query = 'exists x(better_than_jadeja(x) & is_ishant(x))'
    result = make_model_and_answer17(v, query, name_to_var)
    return result

def make_model_and_answer19(v, query, name_to_var):
    val = nltk.parse_valuation(v)
    dom = val.domain
    m = nltk.Model(dom, val)
    g = nltk.Assignment(dom, [])
    result = m.evaluate(query, g)
    # to show the variable (corresponding to player names) for which "srate(x) -> gtsix(x) you can do
    return result


def generate_and_solve_query19(win_toss,win_team):
    c1 = win_team;
    if 'tied' in c1:
        c1=[];
    c2 = win_toss;
    name_to_var = {}
    count = 0
    teams = ['India','New Zealand']
    for i in teams:
        name_to_var[i] = 'r' + str(count)
        count += 1
    temp_strin1 = ''
    for i in name_to_var:
        temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
    temp_strin2 = 'wintoss => {'
    if c2!=[]:
        for i in c2:
            temp_strin2 += name_to_var[i] + ','
        temp_strin2 = temp_strin2[:-1]  #removing the extra "," charater
    temp_strin2 += '}\n'
    temp_strin3 = 'win_team => {'
    if c1!=[]:
        for i in c1:
            temp_strin3 += name_to_var[i] + ','
        temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
    temp_strin3 += '}'
    v = temp_strin1 + temp_strin2 + temp_strin3
    # now forming the query
    query = 'exists x(win_team(x) & wintoss(x))'
    result = make_model_and_answer19(v, query, name_to_var)
    return result

bat_details={}
def retrieve_bat_details(bats1,bats2,bats3,bats4,bats5):
    for i in bats1:
        details = bats1[i]
        runs = float(details[1])
        sixes = float(details[5])
        srate = float(details[6])
        if i not in bat_details:
            bat_details[i] = [runs,sixes,srate];
        else:
            bat_details[i][0] += runs;
            bat_details[i][1] += sixes;
            bat_details[i][2] += srate;
    for i in bats2:
        details = bats2[i]
        runs = float(details[1])
        sixes = float(details[5])
        srate = float(details[6])
        if i not in bat_details:
            bat_details[i] = [runs,sixes,srate];
        else:
            bat_details[i][0] += runs;
            bat_details[i][1] += sixes;
            bat_details[i][2] += srate;
    for i in bats3:
        details = bats3[i]
        runs = float(details[1])
        sixes = float(details[5])
        srate = float(details[6])
        if i not in bat_details:
            bat_details[i] = [runs,sixes,srate];
        else:
            bat_details[i][0] += runs;
            bat_details[i][1] += sixes;
            bat_details[i][2] += srate;
    for i in bats4:
        details = bats4[i]
        runs = float(details[1])
        sixes = float(details[5])
        srate = float(details[6])
        if i not in bat_details:
            bat_details[i] = [runs,sixes,srate];
        else:
            bat_details[i][0] += runs;
            bat_details[i][1] += sixes;
            bat_details[i][2] += srate;
    for i in bats5:
        details = bats5[i]
        runs = float(details[1])
        sixes = float(details[5])
        srate = float(details[6])
        if i not in bat_details:
            bat_details[i] = [runs,sixes,srate];
        else:
            bat_details[i][0] += runs;
            bat_details[i][1] += sixes;
            bat_details[i][2] += srate;
    return bat_details

ball_details={}
def retrieve_ball_details(balls1,balls2,balls3,balls4,balls5):
    for i in balls1:
        details = balls1[i]
        wickets = float(details[3])
        economy = float(details[4])
       # srate = float(details[6])
        if i not in ball_details:
            ball_details[i] = [wickets,economy];
        else:
            ball_details[i][0] += wickets;
            ball_details[i][1] += economy;
        #    ball_details[i][2] += srate;
    for i in balls2:
        details = balls2[i]
        wickets = float(details[3])
        economy = float(details[4])
       # srate = float(details[6])
        if i not in ball_details:
            ball_details[i] = [wickets,economy];
        else:
            ball_details[i][0] += wickets;
            ball_details[i][1] += economy;
        #    ball_details[i][2] += srate;
    for i in balls3:
        details = balls3[i]
        wickets = float(details[3])
        economy = float(details[4])
      #  srate = float(details[6])
        if i not in ball_details:
            ball_details[i] = [wickets,economy];
        else:
            ball_details[i][0] += wickets;
            ball_details[i][1] += economy;
       #     ball_details[i][2] += srate;
    for i in balls4:
        details = balls4[i]
        wickets = float(details[3])
        economy = float(details[4])
     #   srate = float(details[6])
        if i not in ball_details:
            ball_details[i] = [wickets,economy];
        else:
            ball_details[i][0] += wickets;
            ball_details[i][1] += economy;
      #      ball_details[i][2] += srate;
    for i in balls5:
        details = balls5[i]
        wickets = float(details[3])
        economy = float(details[4])
       # srate = float(details[6])
        if i not in ball_details:
            ball_details[i] = [wickets,economy];
        else:
            ball_details[i][0] += wickets;
            ball_details[i][1] += economy;
    #        ball_details[i][2] += srate;
    return ball_details



def retrieve_avg_details(bat_details):
    for player in bat_details:
        j=0
        avg_details[player]=[]
        for j in range(0,3):
            avg_details[player].insert(j,(bat_details[player][j])/5);
    return avg_details


def parse_hardhit(bats1,bats2,bats3,bats4,bats5):
    retrieve_bat_details(bats1,bats2,bats3,bats4,bats5);
    retrieve_avg_details(bat_details)
    toreturn = []
    for i in avg_details:
        if avg_details[i][1] > 1.5 and avg_details[i][2] > 90.0:
            toreturn.append(i)
    return toreturn

def make_model_and_answer16(v, query, name_to_var):
    val = nltk.parse_valuation(v)
    dom = val.domain
    m = nltk.Model(dom, val)
    g = nltk.Assignment(dom, [])
    result = m.evaluate(query, g)
    # to show the variable (corresponding to player names) for which "srate(x) -> gtsix(x) you can do
    return result

def generate_and_solve_query16(bats1,bats2,bats3,bats4,bats5,profile):
    c2 = parse_hardhit(bats1,bats2,bats3,bats4,bats5);
    c1 = ['MS Dhoni'];
    name_to_var = {}
    count = 0
    for i in profile:
        name_to_var[i] = 'r' + str(count)
        count += 1
    temp_strin1 = ''
    for i in name_to_var:
        temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
    temp_strin2 = 'hardhit => {'
    if c2!=[]:
        for i in c2:
            temp_strin2 += name_to_var[i] + ','
        temp_strin2 = temp_strin2[:-1]  #removing the extra "," charater
    temp_strin2 += '}\n'
    temp_strin3 = 'is_Dhoni => {'
    if c1!=[]:
        for i in c1:
            temp_strin3 += name_to_var[i] + ','
        temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
    temp_strin3 += '}'
    v = temp_strin1 + temp_strin2 + temp_strin3
    # now forming the query
    query = 'exists x(hardhit(x) & is_Dhoni(x))'
    result = make_model_and_answer16(v, query, name_to_var)
    return result

def parse_bterthan_opening(bats1,bats2,bats3,bats4,bats5,opening_batsmen):
    bat_details.clear();avg_details.clear()
    retrieve_bat_details(bats1,bats2,bats3,bats4,bats5);
    retrieve_avg_details(bat_details)
    toreturn = []
    avg_runs_opener=0.0;
    flag=0;
    for player in avg_details:
        flag=0;
        for opener in opening_batsmen:
            if avg_details[opener][0] > avg_details[player][0]:
                flag=0
                break
            else:
                flag=1
        if flag==1:
            toreturn.append(player)
    return toreturn

def make_model_and_answer18(v, query, name_to_var):
    val = nltk.parse_valuation(v)
    dom = val.domain
    m = nltk.Model(dom, val)
    g = nltk.Assignment(dom, [])
    result = m.evaluate(query, g)
    # to show the variable (corresponding to player names) for which "srate(x) -> gtsix(x) you can do
    if result:
        l = nltk.LogicParser()
        c1 = l.parse('(all_middle_btter_opening(x) & belongs_middleorder)')
        varnames =  m.satisfiers(c1, 'x', g)
        for i in varnames:
       #     print i
            for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
                if q == i:
                    if p not in query18_ans:
                        query18_ans.insert(len(query20_ans),p)
    return result

def generate_and_solve_query18(bats1,bats2,bats3,bats4,bats5,opening_batsmen,middle_batsmen):
    opening_heuristic = 0;middle_heuristic=0;
    for i in opening_batsmen:
        opening_heuristic += bat_heuristic(avg_details[i])
    for i in middle_batsmen:
        middle_heuristic += bat_heuristic(avg_details[i])
    c1 = opening_batsmen;
    c2 = middle_batsmen;
    if middle_heuristic > opening_heuristic:
        c1 = c2;
    else:
        c1=[]
   # print p1
   # print p2
    name_to_var = {}
    count = 0
    for i in middle_batsmen:
        name_to_var[i] = 'r' + str(count)
        count += 1
    temp_strin1 = ''
    for i in name_to_var:
        temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
    temp_strin2 = 'all_middle_btter_opening => {'
    if c1!=[]:
        for i in c1:
            temp_strin2 += name_to_var[i] + ','
        temp_strin2 = temp_strin2[:-1]  #removing the extra "," charater
    temp_strin2 += '}\n'
    temp_strin3 = 'belongs_middleorder => {'
    if c2!=[]:
        for i in c2:
            temp_strin3 += name_to_var[i] + ','
        temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
    temp_strin3 += '}'
    v = temp_strin1 + temp_strin2 + temp_strin3
    # now forming the query
    query = 'all x(all_middle_btter_opening(x) & belongs_middleorder)'
    result = make_model_and_answer18(v, query, name_to_var)
    return result

bat_best = -1
def bat_heuristic(details):
    heuristic=0
    #print details
    heuristic = 0.8*(float(details[0])/100);
    heuristic += 0.2*(float(details[2])/200)
    return heuristic

def ball_heuristic(details):
    heuristic=0
    #print details
    heuristic = details[0];
    return heuristic


def make_model_and_answer20(v, query, name_to_var):
    val = nltk.parse_valuation(v)
    dom = val.domain
    m = nltk.Model(dom, val)
    g = nltk.Assignment(dom, [])
    result = m.evaluate(query, g)
    # to show the variable (corresponding to player names) for which "srate(x) -> gtsix(x) you can do
    if result:
        l = nltk.LogicParser()
        c1 = l.parse('highest_heuristic(x)')
        varnames =  m.satisfiers(c1, 'x', g)
        for i in varnames:
       #     print i
            for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
                if q == i:
                    if p not in query20_ans:
                        query20_ans.insert(len(query20_ans),p)
    return result


def generate_and_solve_query20(win,profile):
    newz = 'New Zealand'
    ind = 'India'
    heuristic_nz=0;heuristic_ind=0;
    for i in win:
        if newz in win[i]:
            heuristic_nz += 1
        else:
            heuristic_ind += 1
    team_NewZealand = parse_for_players_winteam(profile,['New Zealand'])
    team_India = parse_for_players_winteam(profile,['India'])
    for player in team_NewZealand:
        if player in bat_details:
            heuristic_nz += bat_heuristic(bat_details[player])
        if player in ball_details:
            heuristic_nz += ball_heuristic(ball_details[player])
    for player in team_India:
        if player in avg_details:
            heuristic_ind += bat_heuristic(avg_details[player])
        if player in ball_details:
            heuristic_ind += ball_heuristic(ball_details[player])
    if heuristic_ind > heuristic_nz:
        c1 = ['India'];
    else:
        c1 = ['New Zealand']
    count=0
    name_to_var={}
    name_to_var['India'] = 'r' + str(count)
    count += 1
    name_to_var['New Zealand'] = 'r' + str(count)
    temp_strin1 = ''
    for i in name_to_var:
        temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
    temp_strin2 = 'highest_heuristic => {'
    if c1!=[]:
        for i in c1:
            temp_strin2 += name_to_var[i] + ','
        temp_strin2 = temp_strin2[:-1]  #removing the extra "," charater
    temp_strin2 += '}'
    v = temp_strin1 + temp_strin2
    # now forming the query
    query = 'exists x(highest_heuristic(x))'
    result = make_model_and_answer20(v, query, name_to_var)
    return result

def make(v,query,parse,dt):
    l = nltk.LogicParser()

    val = nltk.parse_valuation(v)
    #print val

    dom=val.domain
    m = nltk.Model(dom , val)
    dom=m.domain
    #print dom
    g = nltk.Assignment(dom,[])
    #print g
    print "************************"
    #print m.evaluate('all x.( (match(x) & exists y.(team(y) and (pomteam(x,y) and  winteam(x,y)))) | (-match(x)) )', g)
    print m.evaluate(query, g)
    print "************************"

    fmla1 = l.parse(parse)
    varnames = m.satisfiers(fmla1, 'x' ,g)
    print "Satisfiers--->"
    for i in varnames:
        for p,q in dt.iteritems():
            if q == i:
                print p

def var_pair3(strikeplayer,sixplayer):
	name_to_var = {}
   	string1='Innings1 => in1\nInnings2 =>in2\nInnings3 => in3\nInnings4 =>in4\nInnings6 => in6\nInnings7 =>in7\nInnings8 => in8\nInnings9 =>in9\nInnings10 =>in10\n'
	p=[]
   	for i in strikeplayer.values():
		for j in i:
			if j not in p:
	    			p.append(j)
	for i in sixplayer.values():
		for j in i:
			if i not in p:
				p.append(j)
	string2='player => {'
#	print p
	for i in p:
		string2+=i+','
	string2 =string2[:-1]
	string2+='}\n'
   	name_to_var['Innings1'] = 'in1'
   	name_to_var['Innings2'] = 'in2'
   	name_to_var['Innings3'] = 'in3'
   	name_to_var['Innings4'] = 'in4'
   	name_to_var['Innings5'] = 'in5'
   	name_to_var['Innings6'] = 'in6'
   	name_to_var['Innings7'] = 'in7'
   	name_to_var['Innings8'] = 'in8'
   	name_to_var['Innings9'] = 'in9'
   	name_to_var['Innings10'] = 'in10'
	string3='match => {in1,in2,in3,in4,in5,in6,in7,in8,in9,in10}\n'
   	string4 = 'strikeplayer => {'
   	for k,v in strikeplayer.iteritems():
		for i in v:
       			string4 += '('
       			string4 += k +','
       			string4 += i + '),'
   	string4 = string4[:-1]
   	string4 += '}\n'
   	string5 = 'sixplayer => {'
   	for k,v in sixplayer.iteritems():
		for i in v:
       			string5 += '('
       			string5 += k +','
       			string5 += i + '),'
   	string5 = string5[:-1]
   	string5 += '}\n'

	v=''
	v=string1+string2+string3+string4+string5
	query='all x.( (match(x) & all y.((player(y) and ((strikeplayer(x,y) &  sixplayer(x,y))|(-strikeplayer(x,y))))|(-player(y)))) | (-match(x)) )'
	parse='match(x) & all y.((player(y) and strikeplayer(x,y) -> sixplayer(x,y)|-player(y)))'
   	return  v,query,name_to_var,parse


def var_pair12(wideplayer):
   	string4 = 'wideplayer => {'
   	for k,v in wideplayer.iteritems():
		for i in v:
       			string4 += '('
       			string4 += k +','
       			string4 += i + '),'
   	string4 = string4[:-1]
   	string4 += '}'

	v=''
	v=string4
	#print v
	#query='wideplayer(I Sharma,RA Jadeja)'
	parse=''
   	val = nltk.parse_valuation(v)
	#print val
	dom=val.domain
	m = nltk.Model(dom , val)
	dom=m.domain
	g = nltk.Assignment(dom,[('x','I Sharma'),('y','RA Jadeja')])
	print "************************"
	print m.evaluate('wideplayer(x,y)', g)
	print "************************"



def query12_parse(info1,info2,info3,info4,info5):
	dict1={}
	for i in info1.keys():
		if info1.get(i)[-1][-1]==')':
			#print '1'
			if i not in dict1:
				dict1[i]=int(info1.get(i)[-1][-3])
			else:
				s=dict1[i]
				s+=int(info1.get(i)[-1][-3])
				dict1[i]=s
	for i in info2.keys():
		if info2.get(i)[-1][-1]==')':
			#print '2'
			if i not in dict1:
				dict1[i]=int(info2.get(i)[-1][-3])
			else:
				s=dict1[i]
				s+=int(info2.get(i)[-1][-3])
				dict1[i]=s
	for i in info3.keys():
		if info3.get(i)[-1][-1]==')':
			#print '3'
			if i not in dict1:
				dict1[i]=int(info3.get(i)[-1][-3])
			else:
				s=dict1[i]
				s+=int(info3.get(i)[-1][-3])
				dict1[i]=s
	for i in info4.keys():
		if info4.get(i)[-1][-1]==')':
			#print '4'
			if i not in dict1:
				dict1[i]=int(info4.get(i)[-1][-3])
			else:
				s=dict1[i]
				s+=int(info4.get(i)[-1][-3])
				dict1[i]=s
	for i in info5.keys():
		if info5.get(i)[-1][-1]==')':
			if i not in dict1:
				dict1[i]=int(info5.get(i)[-1][-3])
			else:
				s=dict1[i]
				s+=int(info5.get(i)[-1][-3])
				dict1[i]=s
	dict2={}
	for i in dict1.keys():
		list1=[]
		for j in dict1.keys():
			if dict1.get(i)>dict1.get(j):
				list1.append(j)
		dict2[i]=list1
	return dict2



def query11_parse(info1,info2,info3,info4,info5):
    dict1 = {}
    dict2 = {}
    dict3 = {}
    dict4 = {}
    dict5 = {}
    temp =[]

    for key in info1.keys():
	temp.append(key)
    dict1['play1'] = temp

    temp =[]
    for key in info2.keys():
	temp.append(key)
    dict1['play2'] = temp

    temp =[]
    for key in info3.keys():
	temp.append(key)
    dict1['play3'] = temp

    temp =[]
    for key in info4.keys():
	temp.append(key)
    dict1['play4'] = temp

    temp =[]
    for key in info5.keys():
	temp.append(key)
    dict1['play5'] = temp

    return dict1


def var_pair11(match1):
	string1='play1 => {'
	for i in match1['play1']:
		string1+=i+','
	string1=string1[:-1]
	string1+='}\n'
	string1+='play2 => {'
	for i in match1['play2']:
		string1+=i+','
	string1=string1[:-1]
	string1+='}\n'
	string1+='play3 => {'
	for i in match1['play3']:
		string1+=i+','
	string1=string1[:-1]
	string1+='}\n'
	string1+='play4 => {'
	for i in match1['play4']:
		string1+=i+','
	string1=string1[:-1]
	string1+='}\n'
	string1+='play5 => {'
	for i in match1['play5']:
		string1+=i+','
	string1=string1[:-1]
	string1+='}\n'

	query='play1(x) and play2(x) and play3(x) and play4(x) and play5(x)'
	l = nltk.LogicParser()
	val = nltk.parse_valuation(string1)
	dom=val.domain
	m = nltk.Model(dom , val)
	dom=m.domain
	g = nltk.Assignment(dom,[])

	fmla1 = l.parse(query)
	print "************************"
	print m.satisfiers(fmla1, 'x' ,g)
	print "************************"






def main():
    bats = {}
    bowl = {}
    player_match = {}
    win = {}
    profile = {}
    toss={}
    bat21 = './dataset/match2/odi2_inn1_bat.txt'
    bat22 = './dataset/match2/odi2_inn2_bat.txt'
    ball21 = './dataset/match2/odi2_inn1_bowl.txt'
    ball22 = './dataset/match2/odi2_inn2_bowl.txt'
    bat11 = './dataset/match1/odi1_inn1_bat.txt'
    bat12 = './dataset/match1/odi1_inn2_bat.txt'
    ball11 = './dataset/match1/odi1_inn1_bowl.txt'
    ball12 = './dataset/match1/odi1_inn2_bowl.txt'
    bat31 = './dataset/match3/odi3_inn1_bat.txt'
    bat32 = './dataset/match3/odi3_inn2_bat.txt'
    ball31 = './dataset/match3/odi3_inn1_bowl.txt'
    ball32 = './dataset/match3/odi3_inn2_bowl.txt'
    bat41 = './dataset/match4/odi4_inn1_bat.txt'
    bat42 = './dataset/match4/odi4_inn2_bat.txt'
    ball42 = './dataset/match4/odi4_inn2_bowl.txt'
    ball41 = './dataset/match4/odi4_inn1_bowl.txt'
    bat51 = './dataset/match5/odi5_inn1_bat.txt'
    bat52 = './dataset/match5/odi5_inn2_bat.txt'
    ball51 = './dataset/match5/odi5_inn1_bowl.txt'
    ball52 = './dataset/match5/odi5_inn2_bowl.txt'
    mom3 = './dataset/match3/mom.txt'
    mom2 = './dataset/match2/mom.txt'
    mom1 = './dataset/match1/mom.txt'
    mom4 = './dataset/match4/mom.txt'
    mom5 = './dataset/match5/mom.txt'
    winning_1 = './dataset/match1/wonby.txt'
    winning_2 = './dataset/match2/wonby.txt'
    winning_3 = './dataset/match3/wonby.txt'
    winning_4 = './dataset/match4/wonby.txt'
    winning_5 = './dataset/match5/wonby.txt'
    toss_5 = './dataset/match5/wontoss.txt'
    toss_4 = './dataset/match4/wontoss.txt'
    toss_3 = './dataset/match3/wontoss.txt'
    toss_2 = './dataset/match2/wontoss.txt'
    toss_1 = './dataset/match1/wontoss.txt'
    profile1 = './dataset/player_profile/indian_players_profile.txt'
    profile2 = './dataset/player_profile/nz_players_profile.txt'
    add_to_dict(player_match,mom1);
    add_to_dict(player_match,mom2);
    add_to_dict(player_match,mom3);
    add_to_dict(player_match,mom4);
    add_to_dict(player_match,mom5);
    add_to_dict(win, winning_1)
    add_to_dict(win, winning_2)
    add_to_dict(win, winning_3)
    add_to_dict(win, winning_4)
    add_to_dict(win, winning_5)
    add_to_dict(toss,toss_5)
    add_to_dict(toss,toss_4)
    add_to_dict(toss,toss_3)
    add_to_dict(toss,toss_2)
    add_to_dict(toss,toss_1)
    add_to_dict_profile(profile,profile1);
    add_to_dict_profile(profile,profile2);

    #for query1
    print "The anwer for the query1 is :\n",
    print "************************"

    for i in range(1,6):
        result = generate_and_solve_query1(player_match[str(i)],win[str(i)],profile)
        if result == 0:
            print "False"
            print "************************"
            break
        #print result
    if result == 1:
        print "True"
        print "************************"
        print "Satisfiers--->"
        print query1_ans

    #for query 2
    print "\nThe answer for the query2 is :\n",
    print "************************"
    for i in range(1,6):
        bats={}
        ball={}
        if i==1:
            add_to_dict(bats,bat11);
            add_to_dict(bats,bat12);
        elif i==2:
            add_to_dict(bats,bat21);
            add_to_dict(bats,bat22);
        elif i==3:
            add_to_dict(bats,bat31);
            add_to_dict(bats,bat32);
        elif i==4:
            add_to_dict(bats,bat41);
            add_to_dict(bats,bat42);
        elif i==5:
            add_to_dict(bats,bat51);
            add_to_dict(bats,bat52);
        result = generate_and_solve_query2(bats,win[str(i)],profile);
        if result == 0:
            print "False"
            print "************************"
            break
    if result == 1:
        print "True"
        print "************************"
        print "Satisfiers--->"
        print query2_ans

    #for query 3

    info1={}
    info2={}
    info3={}
    info4={}
    info5={}
    info6={}
    info7={}
    info8={}
    info9={}
    info10={}


    add_to_dict(info1,bat11);
    add_to_dict(info2,bat21);
    add_to_dict(info3,bat31);
    add_to_dict(info4,bat41);
    add_to_dict(info5,bat51);
    add_to_dict(info6,bat12);
    add_to_dict(info7,bat22);
    add_to_dict(info8,bat32);
    add_to_dict(info9,bat42);
    add_to_dict(info10,bat52);

#   print info1

    q1 = {}
    q2 = {}
    name_to_var3 ={}
    v3 = ''
    query3 =''
    parse3 =''
    q1,q2 = query3_parse(info1,info2,info3,info4,info5,info6,info7,info8,info9,info10);
#print q1
#print q2
    v3,query3,name_to_var3,parse3 = var_pair3(q1,q2)
#    print v3
#    print query1
    print "\nThe answer for query 3 is:\n"
    make(v3,query3,parse3,name_to_var3)

    #for query 4
    print "\nThe answer for the query4 is :\n ",
    print "************************"
    for i in range(1,6):
        bats={}
        if i==1:
            add_to_dict(bats,bat11);
            add_to_dict(bats,bat12);
        elif i==2:
            add_to_dict(bats,bat21);
            add_to_dict(bats,bat22);
        elif i==3:
            add_to_dict(bats,bat31);
            add_to_dict(bats,bat32);
        elif i==4:
            add_to_dict(bats,bat41);
            add_to_dict(bats,bat42);
        elif i==5:
            add_to_dict(bats,bat51);
            add_to_dict(bats,bat52);
        result = generate_and_solve_query4(bats,win[str(i)],profile);
        if result == 0:
            print "False"
            print "************************"
            break
#        print result
        print query4_ans
    if result == 1:
        print "True"
        print "************************"
        print "Satisfiers--->"
        print query4_ans

    #for query 5
    flag=0
    print "\nThe answer for the query5 is :\n ",
    print "************************"
    for i in range(1,6):
        bats={}
        balls={}
        if i==1:
            add_to_dict(bats,bat11);
            add_to_dict(bats,bat12);
            add_to_dict(balls,ball12);
            add_to_dict(balls,ball11);
        elif i==2:
            add_to_dict(bats,bat21);
            add_to_dict(bats,bat22);
            add_to_dict(balls,ball22);
            add_to_dict(balls,ball21);
        elif i==3:
            add_to_dict(bats,bat31);
            add_to_dict(bats,bat32);
            add_to_dict(balls,ball32);
            add_to_dict(balls,ball31);
        elif i==4:
            add_to_dict(bats,bat41);
            add_to_dict(bats,bat42);
            add_to_dict(balls,ball41);
            add_to_dict(balls,ball42);
        elif i==5:
            add_to_dict(bats,bat51);
            add_to_dict(bats,bat52);
            add_to_dict(balls,ball51);
            add_to_dict(balls,ball52);
        result = generate_and_solve_query5(bats,balls,profile);
        if result == 1:
           flag=1
    if flag == 1:
        print "True"
        print "************************"
        print "Satisfiers--->"
        print query5_ans

    # for query6
    print "\nThe answer for the query6 is :\n ",
    print "************************"
    for i in range(1,6):
        balls={}
        if i==1:
            add_to_dict(balls,ball12);
            add_to_dict(balls,ball11);
        elif i==2:
            add_to_dict(balls,ball22);
            add_to_dict(balls,ball21);
        elif i==3:
            add_to_dict(balls,ball32);
            add_to_dict(balls,ball31);
        elif i==4:
            add_to_dict(balls,ball41);
            add_to_dict(balls,ball42);
        elif i==5:
            add_to_dict(balls,ball51);
            add_to_dict(balls,ball52);
        result = generate_and_solve_query6(balls);
        if result == 0:
            print "False"
            print "************************"
            break
        #print result
    if result == 1:
        print "True"
        print "************************"
        print "Satisfiers--->"
        print query6_ans

    # for query7
    flag=0
    print "\nThe answer for the query7 is :\n ",
    print "************************"
    for i in range(1,6):
        balls={}
        if i==1:
            add_to_dict(balls,ball12);
            add_to_dict(balls,ball11);
        elif i==2:
            add_to_dict(balls,ball22);
            add_to_dict(balls,ball21);
        elif i==3:
            add_to_dict(balls,ball32);
            add_to_dict(balls,ball31);
        elif i==4:
            add_to_dict(balls,ball41);
            add_to_dict(balls,ball42);
        elif i==5:
            add_to_dict(balls,ball51);
            add_to_dict(balls,ball52);
        result = generate_and_solve_query7(balls);
        if result == 1:
            flag=1
    if flag == 1:
        print "True"
        print "************************"
        print "Satisfiers--->"
        print query7_ans

    # for query8
    flag=0
    match = []
    print "\nThe answer for the query8 is : \n",
    print "************************"
    for i in range(1,6):
        bats={}
        if i==1:
            add_to_dict(bats,bat11);
            add_to_dict(bats,bat12);
        elif i==2:
            add_to_dict(bats,bat21);
            add_to_dict(bats,bat22);
        elif i==3:
            add_to_dict(bats,bat31);
            add_to_dict(bats,bat32);
        elif i==4:
            add_to_dict(bats,bat41);
            add_to_dict(bats,bat42);
        elif i==5:
            add_to_dict(bats,bat51);
            add_to_dict(bats,bat52);
        result = generate_and_solve_query8(bats,win[str(i)],profile);
       # print result
        if result == 1:
            flag=1
            match.insert(len(match),i)
       # print result
      #  print query8_ans
    if flag == 1:
        print "True"
        print "************************"
        print "Showing the player Names for which query8 satisfies"
        print query8_ans
        print "Showing the matches for which query8 satisfies"
        print match

    # for query9
    flag=0
    print "\nThe answer for the query9 is : \n",
    print "************************"
    for i in range(1,6):
        balls={}
        if i==1:
            add_to_dict(balls,ball12);
            add_to_dict(balls,ball11);
        elif i==2:
            add_to_dict(balls,ball22);
            add_to_dict(balls,ball21);
        elif i==3:
            add_to_dict(balls,ball32);
            add_to_dict(balls,ball31);
        elif i==4:
            add_to_dict(balls,ball41);
            add_to_dict(balls,ball42);
        elif i==5:
            add_to_dict(balls,ball51);
            add_to_dict(balls,ball52);
        result = generate_and_solve_query9(balls,profile);
        if result == 0:
            print "False"
            print "************************"
            break
      #  print result
       # print query9_ans
    if result == 1:
        print "True"
        print "************************"
        print "Showing the right hand bowlers who have taken wickets for which query9 is true"
        print query9_ans

   # for query10
    flag=0
    print "\nThe answer for the query10 is :\n ",
    print "************************"
    bats1={}
    bats2={}
    bats3={}
    bats4={}
    bats5={};balls1={};balls2={};balls3={};balls4={};balls5={}
    add_to_dict(bats1,bat11);
    add_to_dict(bats1,bat12);
    add_to_dict(bats2,bat21);
    add_to_dict(bats2,bat22);
    add_to_dict(bats3,bat31);
    add_to_dict(bats3,bat32);
    add_to_dict(bats4,bat41);
    add_to_dict(bats4,bat42);
    add_to_dict(bats5,bat51);
    add_to_dict(bats5,bat52);
    result = generate_and_solve_query10(bats1,bats2,bats3,bats4,bats5,profile);
    if result == 1:
        print "True"
        print "************************"
        print "Showing the player Names for which query10 satisfies"
        print query10_ans
    else:
        print "False"
        print "************************"

    add_to_dict(balls1,ball12);
    add_to_dict(balls1,ball11);
    add_to_dict(balls2,ball22);
    add_to_dict(balls2,ball21);
    add_to_dict(balls3,ball32);
    add_to_dict(balls3,ball31);
    add_to_dict(balls4,ball41);
    add_to_dict(balls4,ball42);
    add_to_dict(balls5,ball51);
    add_to_dict(balls5,ball52);

    #for query 11
    result = generate_and_solve_query11(bats1,bats2,bats3,bats4,bats5,balls1,balls2,balls3,balls4,balls5,profile);
    print '\nThe answer for the query 11 is :\n'
  #  print "************************"
  #  print query11_ans
  #  print "************************"
    info1 = {}
    info2 = {}
    info3 = {}
    info4 = {}
    info5 = {}
    add_to_dict(info1,bat11)
    add_to_dict(info1,ball11)
    add_to_dict(info1,bat12)
    add_to_dict(info1,ball12)

    add_to_dict(info2,bat21)
    add_to_dict(info2,ball21)
    add_to_dict(info2,bat22)
    add_to_dict(info2,ball22)

    add_to_dict(info3,bat31)
    add_to_dict(info3,ball31)
    add_to_dict(info3,bat32)
    add_to_dict(info3,ball32)

    add_to_dict(info4,bat41)
    add_to_dict(info4,ball41)
    add_to_dict(info4,bat42)
    add_to_dict(info4,ball42)

    add_to_dict(info5,bat51)
    add_to_dict(info5,ball51)
    add_to_dict(info5,bat52)
    add_to_dict(info5,ball52)

    q1 = {}

	#print info1
    q1= query11_parse(info1,info2,info3,info4,info5)
   #  q1 = new.query11_parse(info1,info2,info3,info4,info5)
    var_pair11(q1)


  #for query 12
    result = generate_and_solve_query12(balls1,balls2,balls3,balls4,balls5);
    print '\nThe answer for the query 12 is :\n'

    player={}
    info1={}
    info2={}
    info3={}
    info4={}
    info5={}
    add_to_dict(info1,ball11);
    add_to_dict(info2,ball21);
    add_to_dict(info3,ball31);
    add_to_dict(info4,ball42);
    add_to_dict(info5,ball51);
    #print info1
    q1={}
    query3 =''
    q1 = query12_parse(info1,info2,info3,info4,info5);
    #print q1
    var_pair12(q1)

  #for query 13
    result = generate_and_solve_query13(bats1,bats2,bats3,bats4,bats5);
    print '\nThe answer for the query 13 is :\n'
    print "************************"
    print result
    print "************************"
    print query13_ans

    #for query 14
    result = generate_and_solve_query14(player_match,profile);
    print '\nThe answer for the query 14 is :\n'
    print "************************"
    print result
    print "************************"
    print query14_ans

    #for query 15
    balls12={};balls11={};balls21={};balls22={};balls31={};balls32={};balls41={};balls42={};balls51={};balls52={};
    add_to_dict(balls12,ball12);
    add_to_dict(balls11,ball11);
    add_to_dict(balls22,ball22);
    add_to_dict(balls21,ball21);
    add_to_dict(balls32,ball32);
    add_to_dict(balls31,ball31);
    add_to_dict(balls41,ball41);
    add_to_dict(balls42,ball42);
    add_to_dict(balls51,ball51);
    add_to_dict(balls52,ball52);
    result = generate_and_solve_query15(balls12,balls11,balls21,balls22,balls32,balls31,balls41,balls42,balls52,balls51);
    print '\nThe answer for the query 15 is :\n'
    print "************************"
    print result
    print "************************"
    print query15_ans

#for query 16
    result = generate_and_solve_query16(bats1,bats2,bats3,bats4,bats5,profile);
    print '\nThe answer for the query 16 is :\n'
    print "************************"
    if result==1:
        print "Dhoni belongs to the set of Hard hitting hitting batsmen"

#for query 17
    result = generate_and_solve_query17(balls1,balls2,balls3,balls4,balls5);
    print '\nThe answer for the query 17 is :\n'
    print "************************"
    print result
    print "************************"

#for query 18
    bats12=[];bats11=[];bats21=[];bats22=[];bats31=[];bats32=[];bats41=[];bats42=[];bats51=[];bats52=[];
    add_to_list(bats12,bat12);
    add_to_list(bats11,bat11);
    add_to_list(bats22,bat22);
    add_to_list(bats21,bat21);
    add_to_list(bats32,bat32);
    add_to_list(bats31,bat31);
    add_to_list(bats41,bat41);
    add_to_list(bats42,bat42);
    add_to_list(bats51,bat51);
    add_to_list(bats52,bat52);
    opening_batsmen=[]
    middle_batsmen=[]
    j=0
    for i in bats11:
        if j < 2:
   #         print "j"
    #        print j
            if i not in opening_batsmen:
                opening_batsmen.insert(len(opening_batsmen),i)
        elif j > 2:
                if i not in middle_batsmen:
                    middle_batsmen.insert(len(middle_batsmen),i)
        j += 1
        if j == 5:
            break
  #  print middle_batsmen
    j=0
    for i in bats12:
        if j < 2:
            if i not in opening_batsmen:
                opening_batsmen.insert(len(opening_batsmen),i)
        elif j > 2:
                if i not in middle_batsmen:
                    middle_batsmen.insert(len(middle_batsmen),i)
        j += 1
        if j == 5:
            break
 #   print middle_batsmen
    j=0
    for i in bats21:
        if j < 2:
            if i not in opening_batsmen:
                opening_batsmen.insert(len(opening_batsmen),i)
        elif j > 2:
                if i not in middle_batsmen:
                    middle_batsmen.insert(len(middle_batsmen),i)
        j += 1
        if j == 5:
            break
    j=0
    #print middle_batsmen
    for i in bats22:
        if j < 2:
            if i not in opening_batsmen:
                opening_batsmen.insert(len(opening_batsmen),i)
        elif j > 2:
                if i not in middle_batsmen:
                    middle_batsmen.insert(len(middle_batsmen),i)
        j += 1
        if j == 5:
            break
#    print middle_batsmen
    j=0
    for i in bats31:
        if j < 2:
            if i not in opening_batsmen:
                opening_batsmen.insert(len(opening_batsmen),i)
        elif j > 2:
                if i not in middle_batsmen:
                    middle_batsmen.insert(len(middle_batsmen),i)
        j += 1
        if j == 5:
            break
    j=0
    for i in bats32:
        if j < 2:
            if i not in opening_batsmen:
                opening_batsmen.insert(len(opening_batsmen),i)
        elif j > 2:
                if i not in middle_batsmen:
                    middle_batsmen.insert(len(middle_batsmen),i)
        j += 1
        if j == 5:
            break
    #print opening_batsmen
    j=0
    for i in bats41:
        if j < 2:
            if i not in opening_batsmen:
                opening_batsmen.insert(len(opening_batsmen),i)
        elif j > 2:
                if i not in middle_batsmen:
                    middle_batsmen.insert(len(middle_batsmen),i)
        j += 1
        if j == 5:
            break
    #print opening_batsmen
    j=0
    for i in bats42:
        if j < 2:
            if i not in opening_batsmen:
                opening_batsmen.insert(len(opening_batsmen),i)
        elif j > 2:
                if i not in middle_batsmen:
                    middle_batsmen.insert(len(middle_batsmen),i)
        j += 1
        if j == 5:
            break
   # print opening_batsmen
    j=0
    for i in bats51:
        if j < 2:
            if i not in opening_batsmen:
                opening_batsmen.insert(len(opening_batsmen),i)
        elif j > 2:
                if i not in middle_batsmen:
                    middle_batsmen.insert(len(middle_batsmen),i)
        j += 1
        if j == 5:
            break
  #  print opening_batsmen
    j=0
    for i in bats52:
        if j < 2:
            if i not in opening_batsmen:
                opening_batsmen.insert(len(opening_batsmen),i)
        elif j > 2:
                if i not in middle_batsmen:
                    middle_batsmen.insert(len(middle_batsmen),i)
        j += 1
        if j == 5:
            break
    #print opening_batsmen

    result = generate_and_solve_query18(bats1,bats2,bats3,bats4,bats5,opening_batsmen,middle_batsmen);
    print '\nThe answer for the query 18 is :'
    print result

#for query 19
    for i in range(1,6):
        result = generate_and_solve_query19(toss[str(i)],win[str(i)]);
        if result == 0:
            break
    print '\nThe answer for the query 19 is :'
    print result

#for query 20
    retrieve_ball_details(balls1,balls2,balls3,balls4,balls5);
    result = generate_and_solve_query20(win,profile);
    print '\nThe answer for the query 20 is :'
    print query20_ans

if __name__ == "__main__":
    main()
