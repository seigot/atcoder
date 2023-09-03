
def len_without_empty_set(l):
    num = 0
    for ii in range(len(l)):
        if l[ii]:
            num += 1
    return num

sl = [set() for _ in range(10+1)]
print(len(sl)) # 11
print(len_without_empty_set(sl)) # 0
sl[0].add(1)
sl[2].add(1)
print(len_without_empty_set(sl)) # 2
sl[2].add(2)
print(len_without_empty_set(sl)) # 2

def test_is_empty_set(s):
    if s: print("not empty_set")
    if not s: print("empty_set")
s = set()
test_is_empty_set(s) # empty_set
s.add(1)
test_is_empty_set(s) # not empty_set
