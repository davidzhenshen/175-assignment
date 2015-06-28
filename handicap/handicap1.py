import math

class Member:
    def __init__(self, name, par):
        self.name = name
        self.par = par
        self.rounds = []
    
    def getName(self):
        return self.name
    
    def noBiggerThan10(self, nr):
        if nr > 10:
            return 10
        else:
            return nr
    
    def addRound(self, _str):
        _round = _str.split(" ")
        self.rounds.append(_round)
    
    def calc(self):
        result = "Scratch"
        if len(self.rounds) < 20:
            print (self.name + ": Needs to play more golf!")
            return
        
        netScores = []
        for aRound in self.rounds:
            tmpNetScore = 0
            for shot in aRound:
                tmpNetScore += self.noBiggerThan10(int(shot))
            netScores.append(tmpNetScore)
        
        sortedNetScores = sorted(netScores)
        # print (sortedNetScores)

        total = 0
        for idx in range(0,10):
            total += sortedNetScores[idx]
        
        total /= 10
        totalInt = int(math.ceil(total))
        totalInt -= self.par
        print (self.name + ": " + str(totalInt))

# A = Member("ABC")
# A.calc()

def getMember(name, par, mems):
    for mem in mems:
        if (mem.getName() == name):
            return mem
    newMember = Member(name, par)
    mems.append(newMember)
    return newMember

members = []
par = []

file = open('golfdata.dat','r')
lines = file.readlines()
# print(lines)

# line1 par
par = lines[0].rstrip().split(" ")[1:]
parTotal = 0
for item in par:
    parTotal += int(item)
# print (parTotal)


# line3 first member
lineNr = 2
while (len(lines) >= lineNr + 1):
    _n = lines[lineNr].rstrip()
    _d = lines[lineNr+1].rstrip()

    tmpMember = getMember(_n, parTotal, members)
    tmpMember.addRound(_d)
    
    lineNr += 3

print ("The handicaps for members of Shady Valley G&CC are:")
for mem in members:
    mem.calc()