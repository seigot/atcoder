

s = set([2,3,4,5])
s2 = set([2,3])
# s.issubset(s2)   : 部分集合
# s.issuperset(s2) : 超集合
print(s.issubset(s2))   # False
print(s.issuperset(s2)) # True
print(s2.issubset(s))   # True
print(s2.issuperset(s)) # False
print(s.issubset(s))    # True (同じ場合はTrue)
print(s.issuperset(s))  # True (同じ場合はTrue)
print(s < s2) # False (sはs2の部分集合である --> False)
print(s > s2) # True  (sはs2の超集合である --> True)


