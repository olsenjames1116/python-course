# Dictionaries

band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

# Access items
band["vocals"]
band.get("guitar")

band.keys()

band.values()

band.items()

"guitar" in band

band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

band.pop("bass")
band["drums"] = "Bonham"

band.popitem()

del band["drums"]

band.clear()

# del band

band2 = band

band2 = band.copy()

band3 = dict(band)

member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}
band = {
    "member1": member1,
    "member2": member2
}

band["member1"]["name"]

nums = {1, 2, 3, 4}
num2 = set((1, 2, 3, 4))

2 in nums

nums.add(8)

morenums = {5, 6, 7}
nums.update(morenums)

one = {1, 2, 3}
two = {5, 6, 7}

mynewset = one.union(two)

one.intersection_update(two)

one.symmetric_difference_update(two)
