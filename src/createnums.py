###########################################################################
# 각 자리, 숫자별 출현 빈도
###########################################################################
#from src.history import getHistory

# PRINT
#from src.history import printHistory
#printHistory(history)
###########################################################################
from src.score import getValidHistoryDict
def createNums(info,indexPool):
    # 0-1. N 회분 score 합의 허용범위설정
    validHistoryDict = getValidHistoryDict(info)
    scorePerPoint = []
    
    IsDebug = 0
    if IsDebug:
        for i in range(0,6):
            #print ( validDict[i] )
            M = validHistoryDict[i][list(validHistoryDict[i].keys())[0]]
            scorePerPoint.append(len(info)/M)
            print ( "nseq({})\tmax:{}".format( i+1, M) )
            for j in range(0,len(validHistoryDict[i])):
                if validHistoryDict[i][list(validHistoryDict[i].keys())[j]] * scorePerPoint[i] > 70:
                    print ( "{}:{}".format( list(validHistoryDict[i].keys())[j], validHistoryDict[i][list(validHistoryDict[i].keys())[j]])  )
    
    
    exit()
    return future
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
    