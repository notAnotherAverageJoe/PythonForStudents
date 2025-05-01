
#write to a file
with open("first.txt", 'w') as file:
    file.write("Howdy, this is from our program!\n")
    file.write("Added a second lineWOO!\n")
    
    
#append to a file

with open("first.txt", 'a') as file:
    file.write("Another line! appended\n")
    

#append to a file

with open("first.txt", 'a') as file:
    file.write("Another line! appended * 2\n")
    
#reading from files

with open("first.txt", 'r') as file:
    data = file.read()
    print(data)