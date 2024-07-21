# 回分判定
# s:入力文字列
# return: 
#   True:回分である
#   False:回分でない
def is_palindrome(s):
    for ii in range(len(s)//2):
        if s[ii] != s[-ii-1]:
            return False
    return True
