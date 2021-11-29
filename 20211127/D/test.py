#!/bin/python3

def print_max_num():
    S = input()
    K = int(input())
    length_S = len(S)
    #print(S)
    #print(K)
    #print(length_S)
    #print("---")

    # 累積和
    DotSum = 0
    DotSum_S = [0] * length_S
    for i in range(length_S) :
        if S[i] == '.':
            DotSum += 1
        DotSum_S[i] = DotSum

    #for i in range(length_S) :
    #    print(DotSum_S[i])

    # 探索(しゃくとり法)
    answer = 0
    for i in range(length_S) :
        Xcnt = 0
        Dotcnt = 0
        DotNum = 0
        for j in range(length_S) :
            idx = i+j
            # idxが配列の最大値を超えてる場合は探索終了
            if idx >= length_S:
                break

            # Dotの出現数を取得する(累積和の差分を利用)
            # DotNumの出現数が最大値Kを超えてる場合は探索終了
            if i == 0:
                DotNum = DotSum_S[idx]
            else:
                DotNum = DotSum_S[idx] - DotSum_S[i-1]
            if DotNum > K:
                break
            Xcnt += 1
        answer = max(answer, Xcnt)

    print(answer)

# main
print_max_num()

