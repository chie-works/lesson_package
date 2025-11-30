a = 1
b = 2

a == b
print(a == b)

a != b
print(a != b)

a < b
print(a < b)

a > b
print(a > b)

a <= b
print(a <= b)

a >= b
print(a >= b)

a > 0 and b > 0
print(a > 0 and b > 0)

a > 0 or b > 0
print(a > 0 or b > 0)
# -------------------------
y = [1, 2, 3]

x = 1
if x in y:
    print('in')

x = 4
if x not in y:
    print('not in')


a = 1
b = 2
if not a == b:
    print('not equal')

if a != b:
    print('not equal')

is_ok = True
if is_ok:
    print('hello')

if not is_ok:
    print('hello')
# \-------------------------\
is_ok = 'True'
if is_ok:
    print('True')
else:
    print('False')

is_ok = ''
if is_ok:
    print('True')
else:
    print('False')
 
is_ok = 1
if is_ok:
    print('OK!')
else:
    print('NO!')

is_ok = 0
if is_ok:
    print('OK!')
else:
    print('NO!')

is_ok = 10
if is_ok:
    print('OK!')
else:
    print('NO!')

is_ok = ''
if is_ok:
    print('True')
else:
    print('False')

is_ok = []
if is_ok:
    print('True')
else:
    print('False')

is_ok = [1, 2, 3, 4]
if is_ok:
    print('True')
else:
    print('False')


is_ok = {}
if is_ok:
    print('True')
else:
    print('False')
# ----------------------
is_empty = None
# print(is_empty)
# print(help(is_empty))

if is_empty == None:
    print('None!')

if is_empty is None:
    print('None!')
if is_empty is not None:
    print('None!')

print(1 == True)
print(1 is True)
print(None is None)

