import os
print("######################################")
print("#      file handeling               #")
print("######################################")
def ins():
    print("1.create new file")
    print("2.write text in the file")
    print("3.list the files ")
    print("4.delete the file")
    print("5.rename the file")
    print("6.stop the porgram")
ins()
c=int(input('enter u r choice:')) 
def create_file():
    name=input ('enter the file name :')
    with open(name+".txt","w")as file:
        file.write("welcome")
        print(name+".txt","created sucessfully......")
def write_file():
    name=input ('enter the file nameto write:')
    text=input('type the content:')
    with open(name+".txt","a")as file:
        file.write(text)
        print(name+".txt","created sucessfully......")
while(True):
    ins()
    match c:
        case 1:
            print("creating file")
            create_file()
        case 2:
            print("edit")
            write_file()
        case 3:
            print("list file")
            files_list=os.listdir(".")
            print(files_list)     
        case 4:
            print("delete file")
            n=input("type the file name to delete")
            os.remove(n+".txt")
        case 5:
            print("rename")
        case 6:
            print("stop the program")
            print(name+".txt","created sucessfully......")