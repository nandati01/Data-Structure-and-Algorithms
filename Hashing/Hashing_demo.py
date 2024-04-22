#Declaration of hash map
hash_map = {}

#Initializing
hash_map = {1:2, 5:3, 7:2}

#Checking to see if a key exists
print(1 in hash_map)
print(9 in hash_map)

#Accessing a value
print(hash_map[5])

#Adding a key
#If the key already exists, the value will be updated
hash_map[5] = 6

#If the key doesn't exist, the key value pair will be inserted
hash_map[15] = 9

#Deleting a key
del hash_map[15]

#Get size
len(hash_map)

#Get keys and values
for key, value in hash_map.items():
    print(f"{key}: {value}")
