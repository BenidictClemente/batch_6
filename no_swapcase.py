def swap_case(s):
    return ''.join(char.lower() if char.isupper() else char.upper() for char in s)

# User inputs the word
word = input("Enter a word or phrase: ")
print(swap_case(word))  # Print the swapped case version

