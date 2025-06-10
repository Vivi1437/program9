file_path="sample.txt"
with open(file_path,"w")as file:
    file.write("Hello World\n")
    file.write("That's True")
print("Content written to",file_path)
