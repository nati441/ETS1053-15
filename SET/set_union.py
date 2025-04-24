a = {1, 2, 3}
b = {3, 4, 5}

result = a.union(b)
print(result)


a = {10, 20}
b = {30, 40}
c = {20, 50}

result = a | b | c
print(result)


a = {"apple", "banana"}
b = {"banana", "cherry"}

print(a.union(b))


a = {1, 2}
b = {2, 3}
c = {3, 4}
d = {4, 5}

print(a.union(b, c, d))
