my_dict = {'b': 2, 'a': 3, 'c': 1}
sorted_by_keys = dict(sorted(my_dict.items()))

print(sorted_by_keys)



my_dict = {'b': 2, 'a': 3, 'c': 1}
sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))

print(sorted_by_values)

