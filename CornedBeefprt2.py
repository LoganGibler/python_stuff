import sys
# Import 'sha512' function from 'hashlib' module
from hashlib import sha512

# Import the hash from the command line
flag_hash = sys.argv[1]

# Iterate over numbers 0 - FFF
for num in range(4096):    # 4095 is FFF in decimal, so we will loop to 4096

    # Get the hex number and zero pad it to three characters
    hex_num = f'{num:03x}'

    # format the flag string with each padded num
    flag_upper = "FS{hash-I_had_corned_beef_and_hash_" + hex_num.upper() + "}"
    flag_lower = "FS{hash-I_had_corned_beef_and_hash_" + hex_num.lower() + "}"

    # calculate the hash of the flag string
    guess_upper = sha512(flag_upper.encode())
    guess_lower = sha512(flag_lower.encode())

    # test both upper and lower to see if either the hashes match
    if guess_upper.hexdigest() == flag_hash:
        print(flag_upper)
        break
    elif guess_lower.hexdigest() == flag_hash:
        print(flag_lower)
        break