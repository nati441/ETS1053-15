a = {1, 2, 3}
b = {3, 4, 5}

a.update(b)
print(a)


a = {1, 2}
b = [2, 3, 4]

a.update(b)
print(a)

a = {"x", "y"}
a.update("abc")

print(a)

a = {1}
a.update([2, 3], {4, 5}, (6, 7))

print(a)
