a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

result = a.symmetric_difference(b)
print(result)  # Output: {1, 2, 5, 6}


x = {"apple", "banana", "cherry"}
y = {"banana", "dragonfruit", "cherry"}

result = x ^ y
print(result)  # Output: {'apple', 'dragonfruit'}


a = {1, 2, 3}
b = {3, 4, 5}

a.symmetric_difference_update(b)
print(a)  # Output: {1, 2, 4, 5}
