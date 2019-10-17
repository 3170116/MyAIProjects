class Atoi():

    def __init__(self, first, second, third):
        self.first_row = first
        self.second_row = second
        self.third_row = third


    def getChildren(self):
        result = []

        if len(self.first_row) > 0:

            if len(self.second_row) == 0 or self.first_row[0] < self.second_row[0]:
                first = self.first_row[0:]
                second = self.second_row[0:]
                third = self.third_row[0:]

                second.insert(0,first[0])
                del first[0]
                result.append(Atoi(first,second,third))
            
            if len(self.third_row) == 0 or self.first_row[0] < self.third_row[0]:
                first = self.first_row[0:]
                second = self.second_row[0:]
                third = self.third_row[0:]

                third.insert(0,first[0])
                del first[0]
                result.append(Atoi(first,second,third))
        
        if len(self.second_row) > 0:

            if len(self.first_row) == 0 or self.second_row[0] < self.first_row[0]:
                first = self.first_row[0:]
                second = self.second_row[0:]
                third = self.third_row[0:]

                first.insert(0,second[0])
                del second[0]
                result.append(Atoi(first,second,third))
            
            if len(self.third_row) == 0 or self.second_row[0] < self.third_row[0]:
                first = self.first_row[0:]
                second = self.second_row[0:]
                third = self.third_row[0:]

                third.insert(0,second[0])
                del second[0]
                result.append(Atoi(first,second,third))
        
        if len(self.third_row) > 0:

            if len(self.first_row) == 0 or self.third_row[0] < self.first_row[0]:
                first = self.first_row[0:]
                second = self.second_row[0:]
                third = self.third_row[0:]

                first.insert(0,third[0])
                del third[0]
                result.append(Atoi(first,second,third))
            
            if len(self.second_row) == 0 or self.third_row[0] < self.second_row[0]:
                first = self.first_row[0:]
                second = self.second_row[0:]
                third = self.third_row[0:]

                second.insert(0,third[0])
                del third[0]
                result.append(Atoi(first,second,third))
        
        return result


    def __eq__(self, tatoi):
        return self.first_row == tatoi[0].first_row and self.second_row == tatoi[0].second_row
                

    def __str__(self):
        for i in self.first_row:
            print(i*'*')
        print('-------')
        for i in self.second_row:
            print(i*'*')
        print('-------')
        for i in self.third_row:
            print(i*'*')
        return '-----------------\n'
    

    def isFinal(self):
        return self.first_row == [] and self.second_row == []


#main
first = [1,2,3,4,5]
second = []
third = []
tatoi = Atoi(first,second,third)

#BFS
i = 0
queue = [(tatoi,0)]
while not queue[i][0].isFinal():
    children = queue[i][0].getChildren()
    for child in children:
        if child not in queue:
            queue.append((child,i))
    i += 1

path = []
while queue[i][1] != 0:
    path.insert(0,queue[i][0])
    i = queue[i][1]
path.insert(0,queue[0][0])

for tatoi in path:
    print(tatoi)
