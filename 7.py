n = 100
for i in range(n):
    if i % 7 == 0 or "7" in str(i):
        continue
    print(i)
else:
    ("loop end")
