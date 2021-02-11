#nを入力として受け取る
n = int(input())
def solve(n):
    if n == 0: return "0"
    s = ""
    while n != 0:
        #1の位を見て2で割り切れるか判断
        if n%2 == 1 or n%2 == -1:
            n -= 1
            s += "1"
        else:
            s += "0"
        #nを-2で割る
        n = n//-2
    s = "".join(list(reversed(s)))
    return s
print(solve(n))
