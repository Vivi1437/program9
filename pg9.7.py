f=open("D:\Viswa PYTHON LAB\sample.txt",'r')
print("The file pointer is at byte:",f.tell())
f.seek(10)
print("After reading, The file pointer is at:",f.tell())
