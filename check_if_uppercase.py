def is_all_uppercase(s):
    return all(not ('a' <= char <= 'z') for char in s) and bool(s)  # Check all characters

# Example usage
name = input("Enter your name: ")
if is_all_uppercase(name):
    print("Your name is in uppercase.")
else:
    print("Your name is not in uppercase.")
