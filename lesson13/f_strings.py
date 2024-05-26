person = "dave"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left.")

message = "\n%s has %s coins left" % (person, coins)

message = "\n{} has {} coins left".format(person, coins)

message = "\n{person} has {coins} coins left".format(
    coins=coins, person=person)

player = {'person': 'Dave', 'coins': 3}

message = "\n{person} has {coins} coins left".format(**player)


message = f"\n{person} has {coins} left."

message = f"\n{person} has {2 * 5} left."

message = f"\n{person.lower()} has {2 * 5} left."

message = f"\n{player['person']} has {2 * 5} left."

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}")

for num in range(1, 11):
    print(f"\n2.25 times {num} is {2.25 * num:.2f}")

for num in range(1, 11):
    print(f"\n2.25 times {num} is {2.25 * num:.2%}")
