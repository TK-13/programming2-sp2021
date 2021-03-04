"""
Dictionary extraction - extract the values out of the slogans dict which have keys that appear in keys_to_extract

If you complete that, try to make a new dictionary out of the keys and values you extract, and remove them from
the slogans dictionary.
"""

slogans = {
    "Nike": "Just Do It",
    "Wheaties": "Breakfast of Champions",
    "Dunkin' Donuts": "America Runs on Dunkin'",
    "McDonald's": "I’m Lovin’ It",
    "Skittles": "Taste the rainbow",
    "Capital One": "What's in your wallet?",
    "Subway": "Eat Fresh",
    "Goldfish": "The snack that smiles back",
    "Toyota": "Let's go places",
    "Rice Krispies": "Snap! Crackle! Pop!",
}

keys_to_extract = ["McDonald's", "Nike", "Toyota"]
extracted = {}

# insert your code here :)

for key in slogans.keys():
    if key in keys_to_extract:
        print(key)
        extracted[key] = slogans[key]
        # slogans.pop(key)

print(extracted)
print(slogans)
