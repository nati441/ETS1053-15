text = "Nati, abel"
print(text.endswith("Nati")) 
print(text.endswith("abel"))  



text = "Python programming"
print(text.endswith("programming", 0, 18)) 
print(text.endswith("Python", 0, 6))  
print(text.endswith("Python", 0, 10))


text = "football is enjoying"
print(text.endswith("is", 0, 14))  
print(text.endswith("football", 0, 6))