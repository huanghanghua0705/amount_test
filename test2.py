a = int(input("输入我们球队的实力："))
b = int(input("输入对手球队1的实力："))
c = int(input("输入对手球队2的实力："))
d = int(input("输入对手球队3的实力："))

avsb = 3*(a>b)+(a==b)
avsc = 3*(a>c)+(a==c)
avsd = 3*(a>d)+(a==d)

score = avsb+avsc+avsd

print("小组赛球队可以得到%d分。"%(score))