from hashlib import md5

flag_hash = "588817b2edc115d4f59da72057d995e5"

for num in range(1000):

    # Zero pad the number, check out: https://docs.python.org/3/library/string.html#formatstrings
    padded_num = f'{num:03}'

    # format the flag string with each padded num
    flag = "FS{cabbage-wait_that's_not_right_" + padded_num + "}"

    # calculate the hash of the flag string
    guess = md5(flag.encode())

    # test to see if the hashes match
    if guess.hexdigest() == flag_hash:
        print(flag)
