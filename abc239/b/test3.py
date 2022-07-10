#import math
x = int(input())

#x2 = x/10
#ans = math.floor(x2)
def floor(x):
    y = x - int(x)
    if x >= 0:
        result = int(x)
    elif y == 0:
        result = int(x)
    else:
        result = int(x)-1
    return (result)


ans = floor(x/10)
print(ans)
