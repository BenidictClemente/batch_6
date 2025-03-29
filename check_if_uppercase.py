#Input word or phrases
#check if its in uppercase and print yes if uppercase

def is_all_uppercase(s):
    return all(not ('a' <= char <= 'z') for char in s) and bool(s)  # Check all characters

name = input("Enter a words or phrases : ")
if is_all_uppercase(name):
    print("Yes.")
else:
    print("Not.")
