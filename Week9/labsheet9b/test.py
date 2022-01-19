with open("test.txt", "r") as f:
    x = f.readline()

print(type(x))
print(x.rstrip())