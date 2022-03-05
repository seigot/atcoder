n = int(input())

a_list = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0] # 11
b_list = [0] * 11

# 桁数分回す(4桁だったら3回for loop回す)
for i in range(n - 1):
    # 数値分回す(1-9まで回す)
    for i in range(1, 10):
        b_list[i] = (a_list[i - 1] + a_list[i] + a_list[i + 1]) % 998244353
    # 更新
    for i in range(1, 10):
        a_list[i] = b_list[i]
 
print(sum(b_list) % 998244353)
