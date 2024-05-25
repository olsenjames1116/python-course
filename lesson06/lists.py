users = ['Dave', 'John', 'Sarah']

print("Dave" in users)

print(users[0])
print(users[-1])

print(users.index('Sarah'))

print(users[0:2])
print(users[1:])

print(len(users))

users.append('Elsa')

users += ['Jason']

users.extend(['Rob', 'Jimmy'])

users.insert(0, 'Bob')

users[2:2] = ['Eddie', 'Alex']

users[1:3] = ['Robert', 'JPJ']

users.remove('Bob')

users.pop()

del users[0]

users.sort(key=str.lower)

nums = [4, 42, 78, 1, 5]
nums.reverse()

nums.sort(reverse=True)

print(sorted(nums, reverse=True))

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(mynums)
nums.sort()
print(nums)
print(mynums)

mytuple = tuple(('Dave', 42, True))
anothertuple = (1, 4, 2, 8)

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)

(one, two, *hey) = anothertuple
print(one)
print(two)
print(hey)

anothertuple.count(2)
