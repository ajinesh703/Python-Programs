hash_map = {}

hash_map['apple'] = 1
hash_map['banana'] = 2
hash_map['cherry'] = 3

print("Value for 'apple':", hash_map['apple'])

hash_map['apple'] = 10
print("Update value for 'apple':", hash_map['apple'])

del hash_map['banana']
print("After deletion:", hash_map)