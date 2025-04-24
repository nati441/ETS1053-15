a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a.symmetric_difference_update(b)

print(a)


x = {10, 20, 30}
y = {20, 40, 50}

x.symmetric_difference_update(y)

print(x)


x = {1, 2, 3}
y = set()

x.symmetric_difference_update(y)

print(x)


x = {1, 2}
y = {1, 2}

x.symmetric_difference_update(y)

print(x)
