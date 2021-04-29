###########################################################################
# 각 자리, 숫자별 출현 빈도
###########################################################################
from src.history import getHistory

# PRINT
#from src.history import printHistory
#printHistory(history)
###########################################################################
from src.score import score
from src.generate import generateNum

def score(future,history):
    level=[]
    rangeList = []
    score = 0
    for i in range(0,6): rangeList.append(sorted(history[i].items(), key=(lambda x: x[0]), reverse = True))
    for i in range(0,6):
        maxNum = rangeList[i][0][1]
        level.append((float(maxNum)/100.0) * 80.0)
        level.append((float(maxNum)/100.0) * 95.0)
        if rangeList[i][future[i]-1][1]  > level[0]: score += 2
        elif rangeList[i][future[i]-1][1] > level[1]: score += 3
        else: score += 1
        level.clear()
    for i in range(0,6): rangeList[i].clear()
    rangeList.clear()
    if score >= 9 and score <= 11:
        return True
    return False

def createNums(info,indexPool):
    # 0-1. N 회분 score 합의 허용범위설정
    # 0-2. Call GenerateNum function => (허용범위)
    # - get Num Dict < = {Nun : Score} (형식)
    
    # 1-1. get history ( 필요: indexPool or info ), (score 허용범위는 필요없음)
    # 1-2. Check Score => ( N 회분량의 히스토리 리스트 )
    # 1-3. 각자리별 Score 범위 설정
    # 1-4. Score 미달 history 삭제
    # 1-5. Num Dict 생성 ( 필요: indexPool or info ) <= {Nun : Score} (형식)
    # 1-6. return Num Dict
    
    # 2-1. <6> 자리별 스코어 합 확인( 각 자리 index 0 부터 )
    # 2-2. Score 합의 범위인지 확인
    # OK : return Future
    # NOK :  goto 2-1
    history = getHistory(info)
    future = []
    scale=0.8
    for i in range(0, len(indexPool)):
        future.append([])
        scale_help = 0.000001
        index_init = indexPool[i]
        indexn = index_init * scale
        generateNum(1,indexn,i,indexPool,history[0])
        future[i].append ( int(indexn/130320960)+1 )
        indexn = indexn % 130320960
        future[i].append ( int(indexn/2961840)+2 )
        indexn = indexn % 2961840
        future[i].append ( int(indexn/68880)+3 )
        indexn = indexn % 68880
        future[i].append ( int(indexn/1640)+4 )
        indexn = indexn % 1640
        future[i].append ( int(indexn/40)+5 )
        indexn = indexn % 40
        future[i].append ( int(indexn)+6 )
        #====================================================#
        if future[i][0] < 1: future[i][0] = 1
        for j in range(0,6): future[i][j] %= 45
        while future[i][0] >= future[i][1] or future[i][1] >= future[i][2] or future[i][2] >= future[i][3] or future[i][3] >= future[i][4] or future[i][4] >= future[i][5]:
            if future[i][0] >= future[i][1]: future[i][1] += 1
            if future[i][1] >= future[i][2]: future[i][2] += 1
            if future[i][2] >= future[i][3]: future[i][3] += 1
            if future[i][3] >= future[i][4]: future[i][4] += 1
            if future[i][4] >= future[i][5]: future[i][5] += 1
    
        futuresum = future[i][0]+future[i][1]+future[i][2]+future[i][3]+future[i][4]+future[i][5]
        mymin = 60
        mymax = 90
        scale_help *= 0.1
        while True:
            scnt = 0
            while futuresum > mymax or futuresum < mymin:
                scnt += 1
                if scnt > 10000:
                    scnt = 0
                    mymax += 1
                    if scale > 0.8: scale -= 0.1
                    elif scale < 0.8: scale += 0.1
                future[i].clear()
                if futuresum < mymin: scale += scale_help
                elif futuresum > mymax: scale -= scale_help
                indexn = index_init * scale
                future[i].append ( int(indexn/130320960)+1 )
                indexn = indexn % 130320960
                future[i].append ( int(indexn/2961840)+2 )
                indexn = indexn % 2961840
                future[i].append ( int(indexn/68880)+3 )
                indexn = indexn % 68880
                future[i].append ( int(indexn/1640)+4 )
                indexn = indexn % 1640
                future[i].append ( int(indexn/40)+5 )
                indexn = indexn % 40
                future[i].append ( int(indexn)+6 )
                futuresum = future[i][0]+future[i][1]+future[i][2]+future[i][3]+future[i][4]+future[i][5]
            #print("{} score ==> {}".format( i, score(info[i],future[i],history) ) )
            if score(future[i],history): break
        print("Future{:>5}:\t{:>2}\t{:>2}\t{:>2}\t{:>2}\t{:>2}\t{:>2}".format(str(i+1),future[i][0],future[i][1],future[i][2],future[i][3],future[i][4],future[i][5]))
    for i in range(0,6): history[i].clear()
    history.clear()
    return future
