def ljust(text, width):
    return text + ' ' * (width - len(text))  # Add spaces at the end

# User input
word = input("Enter a word or phrase: ")
width = int(input("Enter total width: "))

print(ljust(word, width))  # Print the left-justified text
