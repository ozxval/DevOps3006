my_file = "names.txt"

def set_Name(name_to_save):
    try:
        file = open(my_file, "a")
        file.write(name_to_save + "\n")
        file.close()
    except PermissionError as e:
        print(str(e.args) + " this file is for read only")
    finally:
        file.close()

def get_Name():
    try:
        file = open(my_file)
        for new_name in file.readlines():
             print(f"hello {new_name}", end='')
    except FileNotFoundError as e:
        print(f'unable to find the file "{my_file}", error name: {e.args}')
    finally:
        file.close()


name = input("enter new name: ")
while name != "0":
    set_Name(name)
    name = input("enter new name: ")
get_Name()
