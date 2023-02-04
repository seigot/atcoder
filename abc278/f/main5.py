import sys
from functools import lru_cache

sys.setrecursionlimit(1 << 24)

N = int(input())
L = []
for i in range(N):
    L.append(input())


@lru_cache(maxsize=None)
def is_win(status, prev):
    res = False

    # 次に指す手を全探索
    for next_word in range(N):
        # 次に使用する手のbitが立っている＝その単語もう使ってるやで
        if (status >> next_word) & 1:
            continue
        # 最後の単語と、次に使用する単語がしりとりできない＝それ使えんやで
        if L[prev][-1] != L[next_word][0]:
            continue

        # もし、この手を指したら、次に相手の手番で次の状態の時、相手の負け確定する?
        # →するなら、今の状態で、この手を指したら勝てるよ！
        # →この状態を貰った人は勝ち！
        if not is_win(status | 1 << next_word, next_word):
            res = True
    return res


for i in range(N):
    # 勝ち確定ルートを探して、なければ敗北？
    if not is_win(1 << i, i):
        print('First')
        exit()
print('Second')
