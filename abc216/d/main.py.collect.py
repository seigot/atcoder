from collections import deque

def main():
    N, M = map(int, input().split())
    cylinders = []  # list 
    top_ball_indexes = [[] for _ in range(N)]
    query = deque()

    print(top_ball_indexes)

    def AppendTopBallIdx(ball_number: int, cylinder_idx: int):
        top_ball_indexes[ball_number].append(cylinder_idx)
        val = top_ball_indexes[ball_number]
        if len(val) == 2:
            # indexを格納
            query.append(val)

    for i in range(M):
        _ = int(input())
        cylinders.append(deque(map(int, input().split())))
        AppendTopBallIdx(cylinders[i][0] - 1, i)

    action_count = 0
    while query:
        # 2つペアがあるqueryのidxを探索する
        top_idx, top_idx2 = query.popleft()
        # idxを取得
        cylinders[top_idx].popleft()
        if cylinders[top_idx]:
            # NULLでない場合
            AppendTopBallIdx(cylinders[top_idx][0] - 1, top_idx)
        cylinders[top_idx2].popleft()
        if cylinders[top_idx]:
            # NULLでない場合
            AppendTopBallIdx(cylinders[top_idx2][0] - 1, top_idx2)

        action_count += 1

    if action_count == N:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()

