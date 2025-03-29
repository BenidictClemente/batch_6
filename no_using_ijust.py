#input a word or phrases.
#enter the width.
#print the left-justified text.

def ljust(text, width):
    return text + ' ' * (width - len(text))  

word = input("Enter a word or phrase: ")
width = int(input("Enter total width: "))

print(ljust(word, width)) 
