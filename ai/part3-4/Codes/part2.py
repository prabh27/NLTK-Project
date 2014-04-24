#Anubhav Srivastava
#201201105

#1 
#For all matches, player of match award is given to player of winning team.

def solver(string):
	gi=0
	cons=0
	cont=0
	then=0
	an=0
	l=[]
	io=[]
	l=string.split(',')
	if 'For all' or 'for all' in l[0]:
		ans='all(x)'

	elif 'there exists' or 'There exists' in l[0]:
		ans='exists(x)'
	ans+='('	
	#Connector
	if 'is given to' in l[1]:
		io=l[1].split('is given to')
		gi=1
	if 'consists of' in l[1]:
		io=l[1].split('consists of')
		cons=1
	if 'contains' in l[1]:
		io=l[1].split('contains')
		cont=1
	if 'then' in l[1]:
		io=l[1].split('then')
		then=1
	if 'and' in l[1]:
		io=l[1].split('and')
		an=1

	if 'player of match' in io[0]:
		ans+='pom(x)'
	if 'losing side' in io[0]:
		ans+='losing(x)'
	if 'strike rate' in io[0]:
		val=io[0].split()
		for i in range(0,len(val)):
			if 'above' in val[i]:
				break
#print i
		if 'is above %s'%val[i+1] in io[0]:
			ans+='strategt(x,'
			ans+=str(val[i+1])
			ans+=')'
		
		for i in range(0,len(val)):
			if 'below' in val[i]:
				break
#print i,len(val)
		if i!=len(val)-1:
			if 'is below %s'%val[i+1] in io[0]:
				ans+='stratelt(x,'
				ans+=str(val[i+1])
				ans+=')'

	if 'player of winning team' in io[0]:
		ans+='pwinner(x)'
	if '1 ducks' in io[0]:
		ans+='duckeq1(x)'
	if 'more sixes than fours' in io[0]:
		ans+='sixgtfr(x)'

	if an==1:
		ans+=' & '
	if then==1:
		ans+=' => '
	else :
		ans += ' & '

	if 'player of match' in io[1]:
		ans+='pom(x)'
	if 'losing side' in io[1]:
		ans+='losing(x)'
	if 'strike rate' in io[1]:
		val=io[1].split()
		for i in range(0,len(val)):
			if 'above' in val[i]:
				break
#print i
		if 'is above %s'%val[i+1] in io[1]:
			ans+='strategt(x,'
			ans+=str(val[i+1])
			ans+=')'
		
		for i in range(0,len(val)):
			if 'below' in val[i]:
				break
#print i,len(val)
		if i!=len(val)-1:
			if 'is below %s'%val[i+1] in io[1]:
				ans+='stratelt(x,'
				ans+=str(val[i+1])
				ans+=')'
	
	if 'player of winning team' in io[1]:
		ans+='pwinner(x)'
	if 'ducks' in io[1]:
		val=io[1].split()
		for i in range(0,len(io[1])):
			if 'ducks' in val[i]:
				break
		ans+='duckeq(x,'
		ans+=val[i-1]
		ans+=')'
	if 'more sixes than fours' in io[1]:
		ans+='sixgtfr(x)'
	ans+=')'
	print ans
#	print io
def main():
	string=raw_input()
	solver(string)
if __name__ == "__main__":
    main()
