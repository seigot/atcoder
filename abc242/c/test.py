n = int(input())

current_list = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0] # 11
next_list = [0] * 11

# 桁数分回す(4桁だったら3回for loop回す)
for i in range(n - 1):
    # 数値分回す(1-9まで回す)
    for i in range(1, 10):
        next_list[i] = (current_list[i - 1] + current_list[i] + current_list[i + 1]) % 998244353
    # 更新
    for i in range(1, 10):
        current_list[i] = next_list[i]
 
print(sum(current_list) % 998244353)
