import os

f = open("names.txt")

f.read()

f.read(4)

f.readline()

f.close()

try:
    f = open("name_list.txt")
    print(f.read())
except:
    print("The file you were trying to read does not exist")
finally:
    f.close()

f = open("names.txt", "a")

f.write("Neil")
f.close()

f = open("context.txt", "w")
f.write("I deleted all of the context")

if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x")
    f.close()

if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("The file you wish to delete does not exist.")

with open("more_names.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)
