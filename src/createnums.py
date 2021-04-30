from src.score import getValidHistoryDict
def createNums(info,indexPool):
    validHistoryDict = getValidHistoryDict(info)
    scorePerPoint = []
    future = []
    future_tmp = []

    for i in range(0,6):
        future_tmp.append([])
        sumScores = 0
        M = validHistoryDict[i][list(validHistoryDict[i].keys())[0]]
        scorePerPoint.append(int(len(info)/M))
        for j in range(0,len(validHistoryDict[i])):
            scorepoint = int(validHistoryDict[i][list(validHistoryDict[i].keys())[j]] * scorePerPoint[i])
            if len(future_tmp[i]) > 0:
                if scorepoint <= 80 and scorepoint >= 50:
                    future_tmp[i].append(list(validHistoryDict[i].keys())[j])
            else:
                future_tmp[i].append(list(validHistoryDict[i].keys())[0])
        future.append(future_tmp[i][(indexPool)%len(future_tmp[i])])
    return future