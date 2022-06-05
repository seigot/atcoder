s = str(input())

# dream dreamer erase eraser
s = s.replace("eraser", "-")
s = s.replace("erase", "-")
s = s.replace("dreamer", "-")
s = s.replace("dream", "-")
if s.count('-') == len(s):
    print("YES")
else:
    print("NO")
