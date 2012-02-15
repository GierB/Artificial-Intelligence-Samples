#Author: Brandon Gier
#Email: gier.b@husky.neu.edu
#Uses forward chaining to reason about percepts to demonstrate how knowledge-based agents work.


kb = []

#Loads initial knowledge base. Path is the name of the file to be loaded.
#Assumes path is in the same directory
def loadInitialKB(path):
    f = open(path)
    for line in f.readlines():
        kb.append(line.split())
    print("Knowledge Base loaded.")
    

#Processes a percepts file. Path is the file name
#Assumes path is a file in same directory as this.
def processPercepts(path):
    f = open(path)
    for line in f.readlines():
        text = line.replace("\n","")
        if line in kb:
            print("Getting a percept: " + text + " ---- already contained in knowledge base")
        else:
            kb.append(line.replace("\n", ""))
            print("Getting a percept: " + text + " ---- added to knowledge base")
            forwardChain()

#Forward chains to find if more knowledge can be gained from the world.
def forwardChain():
    for ex in kb:
        if "IF" in ex and not(ex[0] in kb):
            intx = ex.index('IF')
            temp = ex[intx+1:]
            allin = 1
            for vals in temp:
                valList = [vals]
                if not vals in kb and not valList in kb:
                    allin = 0
            adds = ex[:intx]
            if allin:
                for news in adds:
                    kb.append(news)
                print("New conclusion from forward chaining is: " + "".join(adds))
                print("\tjustified by " + ", ".join(temp) + " and " + "^".join(temp) + "-->" + "".join(adds))
                forwardChain()
