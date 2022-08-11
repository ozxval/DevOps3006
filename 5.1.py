isTrue = False
a = 2
b = 2.5
strOne = "one"
strThree = "Three"
names = ["david", "gil", "guy", "ziv"]
other_list = []
if a < b and b != 1 or not strOne == "oz":
    print("a is smaller then b")
elif a == b:
    print("equals")
else:
    print("a is bigger then b")
if "ariel" in names:
    print("yes")
elif "buzy" in names:
    print(names)
else:
    print("no")
if len(other_list) > 0:
    print("has vaules")
k = 5
f = 5
t = [1, 2, 3]
e = [1, 2, 3]
print(k == f)
print(k is f)
print(f == e)
print(f is e)