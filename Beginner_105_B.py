#nを入力として受け取る
n = int(input())

#最高の個数はn//4で組み合わせをcakelistに入れていく
num = n//4
cakelist = []

for i in range(0,num+1):
    cake4 = 4*i
    for j in range(0,num+1):
        cake7 = 7*j
        cakelist.append(cake4+cake7)

#cakelistに入っていたらok
if n in cakelist:
    print("Yes")
else:
    print("No")