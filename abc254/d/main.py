from collections import defaultdict
N = int(input())

#d = defaultdict(int)
l = [0] * (N+1)

for i in range(1, N+1):
    val = i
    d = 2
    # valを素因数分解した時に、偶数乗にするための片割れを見つけたい
    while True:
        # d**2で割り続ける
        dd = d*d
        if val >= dd:
            mod_val = val % dd
            if mod_val == 0:
                # d**2の余りが0であれば割る
                val = val // dd
            else:
                d += 1
        else:
            break
    l[val] = l[val] + 1

ans = 0
for i in range(len(l)):
    ans += l[i]**2
print(ans)