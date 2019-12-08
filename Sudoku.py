import random,time

class Sudoku():

    map_table = {0:0, 3:1, 6:2, 27:3, 30:4, 33:5, 54:6, 57:7, 60:8}

    def __init__(self, array, is_random, in_row = [False for i in range(9*9)], in_column = [False for i in range(9*9)], in_sub_square = [False for i in range(9*9)]):
        self.array = array
        self.in_row = in_row
        self.in_column = in_column
        self.in_sub_square = in_sub_square

        if is_random:
            for idx in range(9*9):
                if self.array[idx] != ' ':
                    self.in_row[9*(idx//9) + int(self.array[idx]) - 1] = True
                    self.in_column[9*(idx%9) + int(self.array[idx]) - 1] = True
                    self.in_sub_square[9*self.map_table[self.get_start_of_sub_square(idx)] + int(self.array[idx]) - 1] = True


    #is True if is valid to put number 's' to cell at index 'idx'
    def can_play(self,idx,s):
        return (not self.in_row[9*(idx//9) + int(s) - 1] and not self.in_column[9*(idx%9) + int(s) - 1] and not self.in_sub_square[9*self.map_table[self.get_start_of_sub_square(idx)] + int(s) - 1])

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

        for idx in range(9*9):
            for num in range(9):
                if self.array[idx] == ' ' and self.is_unique(idx,str(num + 1)):

                    self.array[idx] = str(num + 1)

                    self.in_row[9*(idx//9) + num] = True
                    self.in_column[9*(idx%9) + num] = True
                    self.in_sub_square[9*self.map_table[self.get_start_of_sub_square(idx)] + num] = True

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
                new_in_row = self.in_row[:]
                new_in_column = self.in_column[:]
                new_in_sub_square = self.in_sub_square[:]

                new_array[idx] = num
                new_in_row[9*(idx//9) + int(num) - 1] = True
                new_in_column[9*(idx%9) + int(num) - 1] = True
                new_in_sub_square[9*self.map_table[self.get_start_of_sub_square(idx)] + int(num) - 1] = True
                
                yield Sudoku(new_array,False,new_in_row,new_in_column,new_in_sub_square) #generate a new Sudoku state
    
    #finds the start index of sub square that contains the number 'idx'
    def get_start_of_sub_square(self,idx):
        start_points = [60,57,54,33,30,27,6,3,0]
        for point in start_points:

            for i in range(3):
                for j in range(3):

                    if point + i + 9*j == idx:
                        return point
 
    #is True when Sudoku is finished
    def isFull(self):
        return ' ' not in self.array
    
    #returns the score of that state
    #score is the sum of cases that we can't put a number in a cell
    def score(self):
        score = 0
        
        for idx in range(9*9):
            if self.array[idx] == ' ':
                for s in range(9):
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



#this is the hardest Sudoku in the world!
s = [
    '8',' ',' ',' ',' ',' ',' ',' ',' ',
    ' ',' ','3','6',' ',' ',' ',' ',' ',
    ' ','7',' ',' ','9',' ','2',' ',' ',
    ' ','5',' ',' ',' ','7',' ',' ',' ',
    ' ',' ',' ',' ','4','5','7',' ',' ',
    ' ',' ',' ','1',' ',' ',' ','3',' ',
    ' ',' ','1',' ',' ',' ',' ','6','8',
    ' ',' ','8','5',' ',' ',' ','1',' ',
    ' ','9',' ',' ',' ',' ','4',' ',' '
    ]

if __name__ == '__main__':
    
    #DFS plus CNF
    t1 = time.time()

    sudoku = Sudoku(s,True)
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

    queue[len(queue) - 1].print()

    t2 = time.time()
    print()
    print(str(t2 - t1) + ' seconds')
