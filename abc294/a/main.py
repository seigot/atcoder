N=int(input())                     # (1)数字が1つ 入力例:N
A=list(map(int, input().split()))  # (5)リストで受け取り 入力例:A1 A2 ... An
ans = [a for a in A if a%2==0]
print(*ans)
