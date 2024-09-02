import os

while True:
    print("""1.create new file and write content
2.delete file
3.view list of files
4.exit""")
    prior = int(input("enter respective number to do the task."))
    
    
    if prior == 1:
        try:
            file_name = input("enter filename or enter n to exit:")
            file_name += ".txt"
            f = open(file_name, "x")
            f.close()
        except FileExistsError:
            print("File already exist so enter different filename\n")
    
        content = input("\nenter the content of the file: ")

        with open(file_name, 'w') as f:
            f.write(content)

        with open(file_name) as f:
            print("\nContent of your file:"+f.read()+"\n")


    elif prior == 3:
        files = [f for f in os.listdir(".") if f.endswith(".txt")]
        for file in files:
            print(file)

            
    elif prior == 2:
        input1 = input("enter filename you want to delete")
        input1 += '.txt'
        if os.path.exists(input1):
            os.remove(input1)
            print(f"{input}File deleted!\n")
        else:
            print("file doesnt exist.\n")
            
            
    elif prior == 4:
        exit()       
    else:
        print("Wrong input. Enter again\n")
