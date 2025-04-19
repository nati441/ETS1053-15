colors = {"red", "green", "blue"}

colors.remove("green")

print(colors)


colors = {"red", "green", "blue"}

colors.remove("yellow")  

numbers = {10, 20, 30, 40, 50}
numbers.remove(30)

print(numbers)  


letters = {"a", "b", "c"}
letters.discard("z")  # No error
print(letters)        # Output: {'a', 'b', 'c'}


