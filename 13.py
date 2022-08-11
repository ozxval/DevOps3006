def addName(file_name):
    my_file = open(file_name, "a")
    currents_name = input("enter name: ")
    my_file.write(currents_name + "\n")
    my_file.close()


def showNames(file_name):
    my_file = open(file_name, "r")
    for name in my_file.readlines():
        print(name, end="")
    my_file.close()


for i in range(5):
    addName("names.txt")
showNames("names.txt")
