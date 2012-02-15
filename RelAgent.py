#Author: Brandon Gier
#Purpose: To imitate a production-rule based agent and react to percepts


#Analyzes percepts from a file in the same directoy and makes appropriate gestures
def makeGestures(path):
    f = open(path)
    for line in f.readlines():
        inpt = eval(line)
        print ("Percepts are: " + inpt[0] + " and " + inpt[1] + " Action taken is: " + match(inpt))
    raw_input("Press any key to exit")
    f.close()


#Following lines establish the database of possible inputs and how to respond
ruleSet = [[["happy", "unsure"], "smile"], [["happy", "positive"], "smile"],
           [["happy", "negative"], "nod"]]

ruleSet.append([["sad", "positive"], "frown"])
ruleSet.append([["sad", "unsure"], "frown"])
ruleSet.append([["sad", "negative"], "frown"])
ruleSet.append([["neutral", "positive"], "nod"])
ruleSet.append([["neutral", "negative"], "nod"])
ruleSet.append([["neutral", "unsure"], "blink"])

#Returns appropriate gesture based on percept input. If invalid percept is given, return error.
def match(inpt):
    for match in ruleSet:
        conds = match[0]
        if conds[0] == inpt[0] :
            if conds[1] == inpt[1]:
                return match[1]
    return 'error'
