def remove_prefix(string, prefix):
    if string.startswith(prefix):
        return string[len(prefix):]  
    return string  


text = input("Enter a word that stars with In: ")
prefix = "In"
result = remove_prefix(text, prefix)
print("Original String:", text)
print("After Removing Prefix:", result)
