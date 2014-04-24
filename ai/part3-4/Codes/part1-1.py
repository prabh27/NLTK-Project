# Author: Anubhav Srivastava
# 201201105

import os
from common import *
import re
import pickle

def getinpstr(inpty):
    if "which" in inpty:
        if "which over" in " ".join(inpty) or "which overs" in " ".join(words) or "which over(s)" in " ".join(words):
            return 2
        elif "which ball" in " ".join(inpty):
            return 1
        elif "bowler" in " ".join(inpty):
            return 5
    elif "who" in inpty:
        if "dismissed" in inpty:
            return 3
        elif "hit" in inpty:
            return 4
    

def ai(no,who,what,inpty):
    os.chdir("../DataSet/match"+str(no))
    inn1 = pickle.load(open(str(no)+"1comm.p","rb"))
    inn2 = pickle.load(open(str(no)+"2comm.p","rb"))
    over = -1
    if "over" in inpty:
        print inpty
        for i in inpty:
            try:
                over = int(i)
            except:
                pass
        over = str(over)
        if over != "-1":
         for i in inn1:
            if re.match(over+'\.*',i):
                pass
            else:
                inn1[i]['what'] = ""
                inn1[i]['to'] = ""
                inn1[i]['from'] = ""
                inn1[i]['why'] = ""
         for i in inn2:
            if re.match(over+'\.*',i):
                pass
            else:
                inn2[i]['what'] = ""
                inn2[i]['to'] = ""
                inn2[i]['from'] = ""
                inn2[i]['why'] = ""

    scarr={}
    scarr['ones']=1
    scarr['twos']=2
    scarr['fours']=4
    scarr['sixes']=6
    scarr['threes']=3
    scarr['four']=4
    scarr['six']=6
    scarr['wide']=-1
    scarr['no ball']=-2
    runs1=[]
    runs2=[]
    for i in inn1:
		if len(i)<6:
			runer=inn1[i]['what'].split()
			'''if runer[0]!='no' and len(runer)!=1:	
				runs1[int(math.floor(float(i)))]+=int(runer[0])
			'''
    for i in inn2:
		if len(i)<6:
			runer=inn2[i]['what'].split()
			'''if runer[0]!='no' and len(runer)!=1:	
				runs2[int(math.floor(float(i)))]+=int(runer[0])
			'''
#print runs1
#print runs2

    if what == 3:
        for i in inn1:
            print inn1[i]['to']
            if inn1[i]['what'] == 'OUT' and inn1[i]['to'] in who:
                return inn1[i]["from"]
        for i in inn2:
            print inn2[i]['to'],
            print who
            if inn2[i]['what'] == 'OUT' and inn2[i]['to'] in who:
                return inn2[i]["from"]

    elif what == 1 or what == 2:
        for k in inpty:
            k = k.lower()
        for l in inpty:
            print l
            for j in scarr:
                if j == l:
                    ans = []
                    for i in inn1:
                        print str(scarr[j]) + ' run',
                        print inn1[i]['what']
                        if (str(scarr[j]) + ' run') in inn1[i]['what'].lower() and inn1[i]['to'] in who:
                            ans.append(inn1[i])
                    for i in inn2:
                        print str(scarr[j]) + ' run',
                        print inn2[i]['what'].lower()
                        if (str(scarr[j]) + ' run') in inn2[i]['what'].lower() and inn2[i]['to'] in who:
                            ans.append(inn2[i])
                    return ans
        if 'wicket' in inpty or 'out' in inpty:
            for i in inn1:
                if inn1[i]['what'] == 'OUT' and inn1[i]['to'] in who:
                    return i
            for i in inn2:
                if inn2[i]['what'] == 'OUT' and inn2[i]['to'] in who:
                    return i
    os.chdir("..")


def main():
    inpstr = raw_input()
    parse = inpstr.split(' ')
    playerprofile1 = "../DataSet/player_profile/indian_players_profile.txt"
    playerprofile2 = "../DataSet/player_profile/nz_players_profile.txt"
    indiaplayers = listplayers(playerprofile1)
    nzplayers = listplayers(playerprofile2)
    players = indiaplayers+nzplayers
    
    num={} 
    num['first']=1
    num['fourth']=4
    num['second']=2
    num['third']=3
    num['forth']=4
    num['fifth']=5

    for i in range(len(parse)):
        if parse[i] in num:
            match=num[parse[i]]
	    break
    final = ""

    prev = 0
    for j in players:
            ans = ""
            ct = 0
            x = j.split(" ")
            for k in x:
                for i in range(len(parse)):
                    if parse[i].lower() == k.lower():
                        ans += k + " "
                        ct+=1
                        if ct>prev:
                            prev = ct
                            final = ans
 
    player = final
    
    quest = getinpstr(parse)
#   print match
#   print player
#   print quest
    ans = ai(match,player,quest,parse)
    print ans

if __name__ == "__main__":
    main()
