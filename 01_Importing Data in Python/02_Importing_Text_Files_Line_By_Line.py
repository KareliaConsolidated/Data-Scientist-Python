# For large files, we may not want to print all of their content to the shell: you may wish to print only the first few lines. Enter the readline() method, which allows you to do this. When a file called file is open, you can print out the first line by executing file.readline(). If you execute the same command again, the second line will print, and so on.
# Read & print the first 3 lines
with open('../Dataset/Importing Data From Dataset/moby_dick.txt') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())

# Flat Files
# Text Files containing Records
# That is, table data
# Record: Row of Fields or Attributes
# Column: Feature or Attributes
# .csv = Comma Separated Values
# .txt = Text File
