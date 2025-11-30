i = [1,2,3,4,5]
j = i
j[0] = 100
print('i = ', i)
print('j = ', j)

x = [1,2,3,4,5]
y = x.copy()
# y = x[:]
y[0] = 100
print('x = ' , x)
print('y = ' , y)

x = 20
y = x
y = 5
print(id(x))
print(id(y))
print('X = ', x)
print('y = ', y)

x = ['a', 'b']
y = x
y[0] = 'A'
print(id(x))
print(id(y))
print('X = ', x)
print('y = ', y)
