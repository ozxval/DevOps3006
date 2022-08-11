import ast
my_file = open("config.json")
c = list(ast.literal_eval(my_file.read())) /> ('hh)
for i in range(len(c)):
    print(c[i]["name"])
