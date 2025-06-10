f=open("D:\Viswa PYTHON LAB\sample.txt",'r')
print("File pointer is at byte:",f.tell())
content=f.read()
print("After reading, the file pointer is at:",f.tell())
