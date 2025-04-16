a = {1, 2, 3, 4}
b = {3, 4, 5}

a.difference_update(b)
print(a)  


a = {1, 2, 3, 4, 5}
b = {2, 3}
c = {1, 6}

a.difference_update(b, c)
print(a) 

