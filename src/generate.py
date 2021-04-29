def generateNum(gSeq, indexN,loopN,indexPool,history):
    nSeq = 0
    if    indexN / 130320960 > 0: nSeq = 1 # NumSeq 1
    elif indexN /     2961840 > 0: nSeq = 2 # NumSeq 2
    elif indexN /         68880 > 0: nSeq = 3 # NumSeq 3
    elif indexN /           1640 > 0: nSeq = 4 # NumSeq 4
    elif indexN /               40 > 0: nSeq = 5 # NumSeq 5
    elif indexN /                 1 > 0: nSeq = 6 # NumSeq 6
    if nSeq != gSeq: return 0
    else:
        if    nSeq == 1: divNum = 130320960
        elif nSeq == 2: divNum =     2961840
        elif nSeq == 3: divNum =         68880
        elif nSeq == 4: divNum =           1640
        elif nSeq == 5: divNum =               40
        elif nSeq == 6: divNum =                 1
        retNum = int(indexN/divNum) + nSeq
        if loopN >= 100:
            curHist = {i:0 for i in range(1, 45 + 1)}
            for i in range( loopN - 100, LoopN + 0 ):
                curHist[indexPool[i]/divNum+nSeq] += 1
            for i in range(1, 45 + 1):
                try:
                    if curHist[i] == 0: del(curHist[i])
                except KeyError: pass
            histList = list(sorted(curHist.items(), key=(lambda x: x[0]), reverse = True))
            maxNum = histList[0]
            level=[]
            level.append((float(maxNum)/100.0) * 80.0)
            level.append((float(maxNum)/100.0) * 95.0)
            # 1-1. get history ( 필요: indexPool or info ), (score 허용범위는 필요없음)
            # 1-2. Check Score => ( N 회분량의 히스토리 리스트 )
            # 1-3. 각자리별 Score 범위 설정
            # 1-4. Score 미달 history 삭제
            # 1-5. Num Dict 생성 ( 필요: indexPool or info ) <= {Nun : Score} (형식)
            # 1-6. return Num Dict
            
            curHist.clear()
            level.clear()
            histList.clear()
    return retNum

