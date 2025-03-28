def custom_title(text):
    result = ""
    capitalize = True  
    
    for char in text:
        if char.isalpha():
            if capitalize:
                result += char.upper()
            else:
                result += char.lower()
            capitalize = False  
        else:
            result += char 
            capitalize = True  
    
    return result

word = input("Enter a word or phrase: ")
print(custom_title(word))
