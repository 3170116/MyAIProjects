def isFinished(triliza):
    for i in range(1,10):
        if str(i) in triliza:
            return False
    return True

def display():
    print(triliza[0],' | ',triliza[1],' | ',triliza[2])
    print('-------------')
    print(triliza[3],' | ',triliza[4],' | ',triliza[5])
    print('-------------')
    print(triliza[6],' | ',triliza[7],' | ',triliza[8])



def playerWins(triliza):
    #horizontal
    if triliza[0] + triliza[1] + triliza[2] == 'XXX':
        return True
    if triliza[3] + triliza[4] + triliza[5] == 'XXX':
        return True
    if triliza[6] + triliza[7] + triliza[8] == 'XXX':
        return True
    #vertical
    if triliza[0] + triliza[3] + triliza[6] == 'XXX':
        return True
    if triliza[1] + triliza[4] + triliza[7] == 'XXX':
        return True
    if triliza[2] + triliza[5] + triliza[8] == 'XXX':
        return True
    if triliza[0] + triliza[3] + triliza[6] == 'XXX':
        return True
    if triliza[0] + triliza[3] + triliza[6] == 'XXX':
        return True
    #diagonal
    if triliza[0] + triliza[4] + triliza[8] == 'XXX':
        return True
    if triliza[2] + triliza[4] + triliza[6] == 'XXX':
        return True

    return False

def AIWins(triliza):
    #horizontal
    if triliza[0] + triliza[1] + triliza[2] == 'OOO':
        return True
    if triliza[3] + triliza[4] + triliza[5] == 'OOO':
        return True
    if triliza[6] + triliza[7] + triliza[8] == 'OOO':
        return True
    #vertical
    if triliza[0] + triliza[3] + triliza[6] == 'OOO':
        return True
    if triliza[1] + triliza[4] + triliza[7] == 'OOO':
        return True
    if triliza[2] + triliza[5] + triliza[8] == 'OOO':
        return True
    if triliza[0] + triliza[3] + triliza[6] == 'OOO':
        return True
    if triliza[0] + triliza[3] + triliza[6] == 'OOO':
        return True
    #diagonal
    if triliza[0] + triliza[4] + triliza[8] == 'OOO':
        return True
    if triliza[2] + triliza[4] + triliza[6] == 'OOO':
        return True

    return False


def AIPlays(triliza):
    def isDeadlock(triliza):
        if playerWins(triliza):
            return True
        elif isFinished(triliza):
            return False
        else:
            nextStates = []
            for i in range(9):
                if triliza[i] == str(i + 1):
                    state = triliza[0:]
                    if triliza.count('X') > triliza.count('O'):
                        state[i] = 'O'
                        if AIWins(state):
                            return False
                    else:
                        state[i] = 'X'
                    if playerWins(state):
                        return True
                    nextStates.append(state)
            
            answears = [isDeadlock(state) for state in nextStates]
            return not (False in answears)

    nextSteps = []
    for i in range(9):
        if triliza[i] == str(i + 1):
            state = triliza[0:]
            if triliza.count('X') > triliza.count('O'):
                state[i] = 'O'
                if AIWins(state):
                    return state
            else:
                state[i] = 'X'
                if playerWins(state):
                    return state
            nextSteps.append(state)

    for step in nextSteps:
        if not isDeadlock(step):
            return step
    return nextSteps[0]
    


global triliza
triliza = ['1','2','3','4','5','6','7','8','9']
display()

while not isFinished(triliza):
    place = int(input('Σε ποια θέση θα παίξεις X >_'))
    if place > 0 and place < 10 and triliza[place - 1] == str(place):
        triliza[place - 1] = 'X'
        if playerWins(triliza):
            display()
            print('Μπράβο κέρδισες!')
            break
        elif isFinished(triliza) and not AIWins(triliza):
            display()
            print('Ισοπαλία!')
            break
        elif isFinished(triliza) and AIWins(triliza):
            display()
            print('Λυπάμαι έχασες...')
            break
        else:
            triliza = AIPlays(triliza)
    display()
    if AIWins(triliza):
        print('Λυπάμε έχασες...')
        break
    elif isFinished(triliza):
        print('Ισοπαλία!')
