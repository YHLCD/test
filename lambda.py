# lambda匿名函式
# 匿名函式不需要定義名稱，一般函式需定義名稱。
# 匿名函式只能有一行運算式，一般函式可以有多行運算式。
# 匿名函式執行完成後自動回傳結果，一般函式加上 return 關鍵字才能回傳結果。


"""ex1"""
# 一般函式：
def greeting(n):
    print(n, 'row10')

greeting('Hello!!')

# lambda函式：
(lambda n1: print(n1, 'row15'))('Hello!!') 
#or
a = (lambda n2: n2)('Hello!!')
print(a, 'row18')

"""ex2(多參數)"""
# 一般函式：
def plus(x, y):
    return x + y

a1 = plus(1, 2)
print(a1, 'row26')

# lambda函式：
(lambda x1, y1: print(x1+y1, 'row29'))(1, 2)
#or
a2 = (lambda x2, y2: x2+y2)(1, 2)
print(a2, 'row32')
#or
a3 = lambda x3, y3: x3+y3
print(a3(1, 2), 'row35')

"""ex3(搭配for loop)"""
#一般函式：
def f(n3):
    a4 = list(range(n3))
    return a4

print(f(5), 'row43')

#lambda函式：
a5 = lambda n4: [i for i in range(n4)]
print(a5(5), 'row47')
#or
(lambda n5: print([i for i in range(n5)], 'row49'))(5)

"""ex4(搭配if)"""
#一般函式：
def f1(n6):
    if n6 < 10:
        return True
    else:
        return False
print(f1(5), 'row58')

#lambda函式：
(lambda n7: print(True if n7<10 else False, 'row61'))(5)
#or
a6 = lambda n8: True if n8<10 else False
print(a6(5), 'row64')

"""ex5(搭配map方法)"""
#一般函式：
def f(n9):
    return n9 + 9
a7 = map(f, [1, 2, 3, 4, 5, 6])
print(list(a7), 'row71')

#lambda函式：
a8 = map(lambda n10: n10+9, [1, 2, 3, 4, 5, 6])
print(list(a8), 'row75')

"""ex6(搭配fliter方法)"""
#一般函式：
def f(a9):
    return a9>6

a10 = filter(f, range(15))
print(list(a10))

#lambda函式：
a11 = filter(lambda n11: n11>6, range(15))
print(list(a11))

"""ex7(搭配sorted方法)"""
#一般函式：
a12 = [[1, 8], [2, 1], [5, 2], [3, 5], [9, 3]]
def f1(n12):
    return n12[0]
b1 = sorted(a12, key=f1)
print(b1, 'row95')

#lambda函式：
a13 = [[1, 8], [2, 1], [5, 2], [3, 5], [9, 3]]
b2 = sorted(a13, key=lambda n13: n13[0])
print(b2, 'row100')

a14 = [[1, 8], [2, 1], [5, 2], [3, 5], [9, 3]]
b3 = sorted(a14, key=lambda n: n[0])
print(b3, 'row104')


