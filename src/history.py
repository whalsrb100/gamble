def getHistory():
    # All History Return
    return historyList

def getHistory(info):
    history = []
    for i in range(0,6): history.append({i:0 for i in range(1,46)})
    for i in range(0, len(info)):
        for j in range(0,6): history[j][info[i][j]] += 1
    return history

def printHistory(history):
    print('#############################')
    for i in range(0,6):
        print("{}번째숫자의 출현빈도".format(i+1))
        print(history[i])
    print('#############################')