#!/usr/bin/python3

# Rachel Leone
# October 21st 2022

import os

def main():
    
    file = input("Enter a file you want to make a shortcut for: ") # asks the user for a file

    file_exists = os.path.exists(file) # checks to see if it exists or not
    file.find(str(file_exists)) # tries to find it

    if(file_exists == True): # if the file is found
        print("\033[92mFile Exists\033[0m") # text is green indicating it is good
    else: # if the file is not found
        print("\033[93mFile Does Not Exist\033[0m") # text is yellow indicating there is a warning
    
    if(file_exists == False): # if the file is not found
        new_file = input('Enter a file you want to create: ') # lets the user enter in a file they want to create
        with open(new_file, "w") as file: # opens the file
            file.close() # closes the file
        print("")
         
    print(os.getcwd()) # prints out the current directory they are in
    print("         1 - Make a symbolic link")
    print("         2 - Delete a symbolic link")
    print("         3 - Run a report")
    print("         quit - Exit the script")
    value = int(input("Select Option: ")) # asks the user to pick an option

    if(value == 1): # when the user enters in a 1
        source = '/usr/bin/python' # the source path
        destination = '/tmp/python' # the destination path
        os.symlink(source, destination) # this creates a symbolic link 

        print("symbolic link has been created!")
    
    if(value == 2): # when the user enters in a 2
        os.remove(file) # this removes the file that was created previously

    if(value == 3): # when the user enters in a 3
        source = '/usr/bin/python'
        destination = '/tmp/python'
        path = os.readlink(destination) # reads the symbolic link 
        print(path) # prints it out

if __name__ == "__main__":
    main()