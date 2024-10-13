# rotate grid by +90 degrees 
# if rotate -90 degrees, rotate 3 times
# 1 2    2 4 6
# 3 4 -> 1 3 5
# 5 6 
def rot(grid):
    h,w = n,n
    new = [['']*h for i in range(w)]
    for i in range(w):
        for j in range(h):
            new[i][j] = grid[j][w-1-i]
    h, w = w, h
    return new

