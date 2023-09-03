h, w = map(int, input().split())
c = [input() for _ in range(h)]
a = [[-1 for j in range(w)] for i in range(h)]

MOJI = 26
for i in range(h):
	for j in range(w):
		a[i][j] = ord(c[i][j]) - ord('a')
row = [[0 for _ in range(MOJI)] for i in range(h)]
col = [[0 for _ in range(MOJI)] for j in range(w)]
for i in range(h):
	for j in range(w):
		row[i][a[i][j]] += 1
		col[j][a[i][j]] += 1

row_deleted = [False for _ in range(h)]
col_deleted = [False for _ in range(w)]

def to_delete(x):
	tot = 0; kind = 0
	# 該当行の文字列の数をみる
	for i in range(MOJI):
		tot += x[i] # 各文字の数
		if x[i] > 0: kind += 1
	# 削除可能ならtrue、不可能ならfalseを返す
	return (kind == 1 and tot >= 2)

def exe_delete(i, j):
	# 削除を試みる
	if row_deleted[i] or col_deleted[j]: return
	row[i][a[i][j]] -= 1 # 該当行から該当文字の出現回数を1こ減らす
	col[j][a[i][j]] -= 1 # 該当列から該当文字の出現回数を1こ減らす

while True:
	del_row = []; del_col = []

	# クッキーの縦列の削除候補チェック
	for i in range(h):
		if row_deleted[i]: 
			continue
		if to_delete(row[i]): 
			del_row.append(i)

	# クッキーの横列の削除候補チェック
	for j in range(w):
		if col_deleted[j]:
			continue
		if to_delete(col[j]): 
			del_col.append(j)

	# クッキーの縦列の削除実施
	for i in del_row:
		#i行目j列の削除
		for j in range(w): 
			exe_delete(i, j)
		row_deleted[i] = True
	
	# クッキーの横列の削除実施
	for j in del_col:
		#j行目i列の削除
		for i in range(h): 
			exe_delete(i, j)
		col_deleted[j] = True

	if len(del_row) == 0 and len(del_col) == 0:
		break
# 残ったクッキーを数える
ans = 0
for i in range(h):
	for j in range(w):
		if row_deleted[i] or col_deleted[j]: continue
		ans += 1
print(ans)