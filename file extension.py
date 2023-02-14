# To find the file extension
filename = input("Input the Filename: ")
file_extension = filename.split(".")
print("The extension of the file is: " + repr(file_extension[-1]))