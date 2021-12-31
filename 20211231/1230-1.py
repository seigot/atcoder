# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import sys
import copy

def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stdout)

H, W, N = map(int, input().split())
#error(H, W, N)
STR=[0]*H
for i in range(H):
    STR[i] = str(input())
STRING = str(input())
#print(STRING)

def Dilation(IN, H, W): #膨張

    OUT=copy.deepcopy(IN)
    #print(OUT)
    #print(OUT[0][1])
    #print(OUT)

    for i in range(H):
        OUT_STR=""
        for j in range(W):

            if IN[i][j] == '#':
                OUT_STR = OUT_STR + '#'
                continue
            if IN[i][j] == '.':
                if IN[i][max(j-1,0)] == '#' or IN[max(i-1,0)][j] == '#' or IN[i][min(j+1,W-1)] == '#' or IN[min(i+1,H-1)][j] == '#':
                    OUT_STR = OUT_STR + '#'
                else:
                    OUT_STR = OUT_STR + '.'
        OUT[i]=OUT_STR
    return OUT

def Erosion(IN, H, W): #収縮

    OUT=copy.deepcopy(IN)
    OUT_STR=""

    for i in range(H):
        OUT_STR=""
        for j in range(W):
            if IN[i][j] == '.':
                OUT_STR = OUT_STR + '.'
            elif IN[i][j] == '#':
                if IN[i][max(j-1,0)] == '.' or IN[max(i-1,0)][j] == '.' or IN[i][min(j+1,W-1)] == '.' or IN[min(i+1,H-1)][j] == '.':
                    OUT_STR = OUT_STR + '.'
                else:
                    OUT_STR = OUT_STR + '#'
        OUT[i]=OUT_STR
    return OUT


LEN=len(STRING)
for i in range(LEN):
    if STRING[i] == 'D':
        STR=Dilation(STR,H,W)
    if STRING[i] == 'E':
        STR=Erosion(STR,H,W)

for i in range(H):
    print(STR[i])
