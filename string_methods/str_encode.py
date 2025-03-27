text = "Hello, world!"
encoded_text = text.encode() 
print(encoded_text)


encoded_text = "Café".encode("utf-8")
decoded_text = encoded_text.decode("utf-8")
print(decoded_text) 
