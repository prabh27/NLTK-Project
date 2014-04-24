

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

d11={}
d22={}
d33={}
d44={}
d55={}
d1={}
d2={}
d3={}
d4={}
d5={}

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



def part2(string):
	query_1=0
	query_2=0
	query_3=0
	query_4=0
	query_5=0
	dict_1=[]
	dict_2=[]
	dict_1=string.split(',')
	if 'For all' or 'for all' in dict_1[0]:
		final='for_all(x)'

	elif 'there exists' or 'There exists' in dict_1[0]:
		final='there_exists(x'
	final+='('

	if 'consists of' in dict_1[1]:
		dict_2=dict_1[1].split('consists of')
		query_2=1
	if 'contains' in dict_1[1]:
		dict_2=dict_1[1].split('contains')
		query_3=1
	if 'and' in dict_1[1]:
		dict_2=dict_1[1].split('and')
		query_5=1
	if 'is given to' in dict_1[1]:
		dict_2=dict_1[1].split('is given to')
		query_1=1
	if 'then' in dict_1[1]:
		dict_2=dict_1[1].split('then')
		query_4=1

	if 'player of match' in dict_2[0]:
		final+='player_of_match(x)'
	if 'losing side' in dict_2[0]:
		final+='losing_side(x)'
	if 'strike rate' in dict_2[0]:
		output=dict_2[0].split()
		for i in range(0,len(output)):
			if 'above' in output[i]:
				break
		if 'is above %s'%output[i+1] in dict_2[0]:
			final+='strike_rate_gt(x,'
			final+=str(output[i+1])
			final+=')'

		for i in range(0,len(output)):
			if 'below' in output[i]:
				break
#print "ho jaaaaaaa\n"
		if i!=len(output)-1:
			if 'is below %s'%output[i+1] in dict_2[0]:
				final+='strike_rate_lt(x,'
				final+=str(output[i+1])
				final+=')'

	if 'player of winning team' in dict_2[0]:
		final+='player_winningteam(x)'
	if '1 ducks' in dict_2[0]:
		final+='ducks1(x)'
	if 'more sixes than fours' in dict_2[0]:
		final+='six_gt_fours(x)'

	if query_5==1:
		final+=' & '
	if query_4==1:
		final+=' => '
	else :
		final += ' & '

	if 'player of match' in dict_2[1]:
		final+='player_of_match(x)'
	if 'losing side' in dict_2[1]:
		final+='losing_side(x)'
	if 'strike rate' in dict_2[1]:
		output=dict_2[1].split()
		for i in range(0,len(output)):
			if 'above' in output[i]:
				break
#print i
		if 'is above %s'%output[i+1] in dict_2[1]:
			final+='strike_rate_gt(x,'
			final+=str(output[i+1])
			final+=')'

		for i in range(0,len(output)):
			if 'below' in output[i]:
				break
#print i,len(output)
		if i!=len(output)-1:
			if 'is below %s'%output[i+1] in dict_2[1]:
				final+='strike_rate_lt(x,'
				final+=str(output[i+1])
				final+=')'

	if 'player of winning team' in dict_2[1]:
		final+='pwinner(x)'
	if 'ducks' in dict_2[1]:
		output=dict_2[1].split()
		for i in range(0,len(dict_2[1])):
			if 'ducks' in output[i]:
				break
		final+='ducks(x,'
		final+=output[i-1]
		final+=')'
	if 'more sixes than fours' in dict_2[1]:
		final+='six_gt_fours(x)'
	final+=')'
	print final

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




def main():
  d11=add_to_dict(d1,'../dataset/match1.txt')
  d22=add_to_dict(d2,'../dataset/match2.txt')
  d33=add_to_dict(d3,'../dataset/match3.txt')
  d44=add_to_dict(d4,'../dataset/match4.txt')
  d55=add_to_dict(d5,'../dataset/match5.txt')
  string=raw_input("Ask a query:\n")
  part2(string)
if __name__ == "__main__":
    main()
