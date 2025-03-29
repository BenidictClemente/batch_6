#input filename and entension
#print if valid or not

def file(filename, extension):
    return filename[-len(extension):] == extension if len(extension) <= len(filename) else False

filename = input("Enter your filename here: ")
extension = input("Enter extension of your file: ")

if extension not in [".pdf", ".docx"]:
    print("Invalid file extension! Only .pdf and .docx are allowed.")
else:
    print(f"Your file '{filename}' with extension '{extension}' is valid.")


