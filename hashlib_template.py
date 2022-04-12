import hashlib

string_to_hash = "something"
# change .md5 to whatever hash type it is

my_hash = hashlib.md5(string_to_hash.encode("ascii"))

# may need to .upper or .lower to check if hashes the same
# quick note: hex isn't case sensitive, strings are!
hash_2 = "h4h46464h44447334".upper()
print(my_hash.hexdigest().upper() == hash_2)

print(my_hash.hexdigest())