import random,time

class Sudoku():

    def __init__(self, array):
        self.array = array


    #is True if is valid to put number 's' to cell at index 'idx'
    def can_play(self,idx,s):
        return (s not in self.getRow(idx//9)) and (s not in self.getColumn(idx%9)) and (s not in self.get_sub_square(idx))

    #is True if the only valid number you can put at cell with index 'idx' is 's'
    def is_unique(self,idx,s):

        if self.can_play(idx,s):

            start = 60

            #finds the sub square in which the cell with index 'idx' belongs
            start_points = [60,57,54,33,30,27,6,3,0] #the indexes that every sub square starts
            for point in start_points:
                done = False
                for i in range(3):
                    for j in range(3):
                        if point + i + 9*j == idx:
                            start = point
                            done = True
                            break
                    if done:
                        break
            
            #checks if is valid to put number 's' in any other cell of this sub square
            for i in range(3):
                for j in range(3):
                    if start + i + 9*j != idx and self.array[start + i + 9*j] == ' ':
                        if self.can_play(start + i + 9*j,s):
                            return False
            
            return True
        
        return False
        

    #finds an empty cell and checks if there is a unique number
    #which should be in that cell
    def start(self):
        nums = [str(i+1) for i in range(9)]

        for idx in range(9*9):
            for s in nums:
                if self.array[idx] == ' ' and self.is_unique(idx,s):
                    self.array[idx] = s
                    return True
        
        return False
    
    #it is called when we have to try some cases
    #to see which next move is correct
    #creates a generator of some possible next moves
    def test(self):
        nums = [str(i + 1) for i in range(9)] #all posible numbers
        idx = 0
        tests = 10

        #finds the cell with the least cases
        for i in range(9*9):

            if self.array[i] == ' ':

                cnt = 0
                for num in nums:
                    if self.can_play(i,num):
                        cnt += 1
                if cnt < tests:
                    idx = i
                    tests = cnt

        for num in nums:

            if self.can_play(idx,num):
                
                new_array = self.array[:]
                new_array[idx] = num
                yield Sudoku(new_array) #generate a new Sudoku state

    
    #return the column with index 'index'
    #'index' is a number between 0 and 8
    def getColumn(self, index):
        column = []
        for i in range(9):
            column.append(self.array[9*i + index])
        return column

    #return the row with index 'index'
    #'index' is a number between 0 and 8
    def getRow(self, index):
        return self.array[9*index: 9*index + 9]

    #finds the sub square in which number 'idx' belongs
    def get_sub_square(self,idx):
        start_points = [60,57,54,33,30,27,6,3,0]
        for point in start_points:

            nums = []
            for i in range(3):
                for j in range(3):

                    if point + i + 9*j == idx:

                        sub_square = []
                        for i in range(3):
                            for j in range(3):
                                sub_square.append(self.array[point + i + 9*j])

                        return sub_square
 
    #is True when Sudoku is finished
    def isFull(self):
        return ' ' not in self.array
    
    #returns the score of that state
    #score is the sum of cases that we can't put a number in a cell
    def score(self):
        score = 0
        
        for idx in range(9*9):
            for s in range(10):
                if not self.can_play(idx,str(s + 1)):
                    score += 1
        
        return score

    def print(self):
        for i in range(9):
            print(self.array[9*i],' ',self.array[9*i + 1],' ',self.array[9*i + 2],'|', end = '')
            print(self.array[9*i + 3],' ',self.array[9*i + 4],' ',self.array[9*i + 5],'|', end = '')
            print(self.array[9*i + 6],' ',self.array[9*i + 7],' ',self.array[9*i + 8])
            if (i + 1)%3 == 0 and i < 8:
                print('---------------------------------')



s = [
    ' ','8',' ','5',' ','6',' ','2',' ',
    '4',' ','9',' ',' ',' ','5','6',' ',
    '6','5',' ',' ','2',' ',' ','1',' ',
    ' ',' ',' ',' ',' ','1',' ',' ',' ',
    ' ',' ',' ',' ',' ','8','2',' ','3',
    '9',' ',' ',' ',' ',' ',' ',' ',' ',
    ' ','6',' ','3',' ','2','9',' ',' ',
    '3',' ','1','9',' ',' ',' ',' ',' ',
    ' ',' ',' ','8','1',' ','6',' ',' '
    ]

if __name__ == '__main__':
    
    #DFS plus CNF
    sudoku = Sudoku(s)
    queue = [sudoku]
    while not queue[len(queue) - 1].isFull():

        if queue[len(queue) - 1].start() == False: #it means that can't find unique next step

            pop = queue.pop()
            tests = [] #some possible next steps
            for test in pop.test():
                tests.append(test)
            
            sorted(tests,key = lambda x: x.score())
            for test in tests:
                queue.append(test)
        
            pop.print()
            print()

    queue[len(queue) - 1].print()
    time.sleep(1000)
