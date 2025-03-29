#input words or phrases.
#print the swapcase version

def swap_case(s):
    return ''.join(char.lower() if char.isupper() else char.upper() for char in s)

word = input("Enter a word or phrase: ")
print(swap_case(word))  

