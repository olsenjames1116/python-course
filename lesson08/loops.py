value = 1
while value < 10:
    print(value)
    if value == 5:
        break
    value += 1

while value <= 10:
    value += 1
    if value == 5:
        continue
    print(value)
else:
    print()

names = ['Dave', 'Sarah', 'John']
for x in names:
    if x == 'Sara':
        break
    print(x)

for x in range(2, 4):
    print(x)

for x in range(0, 100, 5):
    print(x)

names = ['Dave', 'Sara', 'John']
actions = ['codes', 'eats', 'sleeps']

for name in names:
    for action in actions:
        print(name + " " + action + ".")
