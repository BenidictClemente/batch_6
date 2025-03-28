def custom_center(text, width):
    spaces = (width - len(text)) // 2  
    return ' ' * spaces + text + ' ' * spaces  

word = input("Enter a word or phrase: ")
width = int(input("Enter total width: "))

print(custom_center(word, width))  
