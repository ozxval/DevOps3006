import ast
my_file = open("config.json")
c = list(ast.literal_eval(my_file.read())) (hallo)
for i in range(len(c)):
    print(c[i]["name"])
