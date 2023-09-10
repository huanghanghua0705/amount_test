price={'苹果':10,'香蕉':12,'橘子':15}

print("今日水果价格；")
for fruit in price:
    print("%s %d元/斤"%(fruit,price[fruit]))
print("")

#输入购买水果的种类数量
n=int(input("请输入水果的种类数量："))

#计算总价格
sum_price = 0
for i in range(0,n):
    fruit = input("请输入购买水果%d的名称："%(i+1))
    num = int(input("请输入购买水果%d的数量："%(i+1)))
    if fruit in price:
            sum_price = sum_price + price[fruit]*num
    else:
            print("没有该水果")
print("总价格：%d"%sum_price)