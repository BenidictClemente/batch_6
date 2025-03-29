#enter a word 
# remove the prefixes that means "not"
#print the word without the prefix
def remove_prefix(string, prefix):
    if string.startswith(prefix):
        return string[len(prefix):]  
    return string  


text = input("Enter a word that stars with In: ")
prefix = "In,un,"
result = remove_prefix(text, prefix)
print("Original String:", text)
print("After Removing Prefix:", result)
