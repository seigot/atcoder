#for i in range(3, 5): # 3, 4
#for i in range(5):    # 0, 1, 2, 3, 4
#for i in s:           # 集合sの要素, 'a', 'b', 'c'...
#for i in l:           # リストlの要素, 'a', 'b', 'c'...
#for i in dq:          # キューdqの要素 'a', 'b', 'c'...
#for i in d:           # 辞書dの要素(idx) '0', '1', '2'...
#for i in t:           # タプルtの要素 'あ', 'お', 'ま', 'き', 'が',...                                                                                                             

print("---")
for i in range(3, 5): # 3, 4
    print(i)
print("---")
for i in range(5):    # 0, 1, 2, 3, 4
    print(i)

print("--- list")
l = ["a", "b", "c"]
while l:           # リストlの要素, 'a', 'b', 'c'...
    print(l.pop(0))
    
#    l.append("d")

print("--- pop")
s = set()
s.add("a")
s.add("b")
s.add("c")

while s:           # 集合sの要素, 'a', 'b', 'c'...
    print(s.pop())
    
#    s.add("d")

print("--- deque")
import collections
dq = collections.deque(["a", "b", "c"])
while dq:          # キューdqの要素 'a', 'b', 'c'...
    print(dq.popleft())
#    dq.append("d")

print("--- dict")
d = collections.defaultdict(int)
d[0] = 0
d[1] = 111
d[2] = 222
print(d)
cnt = 0
while d:           # 辞書dの要素(idx) '0', '1', '2'...
    print(d.pop(cnt))
    cnt += 1
#    d[3] = 333
print("---")
teststr = "あおまきがみ" 
t = tuple(teststr) 
for i in t:           # タプルtの要素 'あ', 'お', 'ま', 'き', 'が',...
    print(i)
    t = t + tuple("き")
