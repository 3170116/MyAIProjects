class Queens():

    def __init__(self, queens):
        self.queens = queens
        self.chess = []
        for i in range(queens**2):
            self.chess.append(' ')
    

    def findPlaces(self):
        def isOk(chess):
            i = 0
            for q in chess:
                if q == 'Q':
                    #horizontal check
                    r = i//(self.queens)
                    row = chess[r*self.queens : r*self.queens + self.queens]
                    if row.count(q) > 1:
                        return False
                    
                    #vertical check
                    verCounter = 0
                    for r in range(self.queens):
                        if chess[r*self.queens + i%self.queens] == q:
                            verCounter += 1
                    if verCounter > 1:
                        return False
                    
                    #diagonal check
                    diagCounter = 0

                    place = i
                    place = place - self.queens - 1 #check up and left
                    while place >= 0:
                        if chess[place] == 'Q':
                            diagCounter += 1
                        place = place - self.queens - 1
                    place = i
                    place = place + self.queens + 1 #check down and right
                    while place < self.queens**2:
                        if chess[place] == 'Q':
                            diagCounter += 1
                        place = place + self.queens + 1
                    
                    place = i
                    place = place - (self.queens - 1) #check up and right
                    while place >= 0 and place%self.queens > i%self.queens:
                        if chess[place] == 'Q':
                            diagCounter += 1
                        place = place - (self.queens - 1)
                    place = i
                    place = place + (self.queens - 1) #check down and left
                    while place%self.queens < i%self.queens and place < self.queens**2:
                        if chess[place] == 'Q':
                            diagCounter += 1
                        place = place + (self.queens - 1)
                    
                    if diagCounter > 0:
                        return False

                i += 1
            
            return True

        queue = [self.chess[0:]]
        while len(queue) > 0:
            if  queue[0].count('Q') == self.queens and isOk(queue[0]):
                break
            
            #find first row without queen
            for row in range(self.queens):
                if 'Q' not in queue[0][row*self.queens: row*self.queens + self.queens]:
                    for col in range(self.queens):
                        chess = queue[0][0:]
                        chess[row*self.queens + col] = 'Q'
                        if isOk(chess):
                            queue.append(chess)
            del queue[0]
        
        if len(queue) > 0:
            self.chess = queue[0]
        return self.chess



#main
q = 5
queens = Queens(q)
chess = queens.findPlaces()
for i in range(q):
    print(chess[q*i:q*i + q])