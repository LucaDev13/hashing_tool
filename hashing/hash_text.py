from algoritms import sha1_encryption, sha224_encryption, sha256_encryption, sha512_encryption, md5_encryption, \
    sha3_224_encryption

print("This program works with hashlib library. It support the following algorithms: \n"
      "sha1, sha224, sha256, sha512, md5, sha3_224\n")

print("In order to use this program choose an algorithm from the above list \n"
      "and then insert the string to be hashed with the chosen algorithm. \n")

print('When done press q + Enter to stop the program. \n')

while True:
    chosen_algorithm = input("Choose the encryption algorithm to be used: \n")
    print('\n' + f'Enter string to hash in {chosen_algorithm} algorithm: ' + '\n')
    string = input()
    if string == "q":
        print('See you next time!')
        break

    else:
        if chosen_algorithm == 'sha1':
            sha1_encryption(string)
        if chosen_algorithm == 'sha224':
            sha224_encryption(string)
        if chosen_algorithm == 'sha256':
            sha256_encryption(string)
        if chosen_algorithm == 'sha512':
            sha512_encryption(string)
        if chosen_algorithm == 'sha3_224':
            sha3_224_encryption(string)
        if chosen_algorithm == 'md5':
            md5_encryption(string)


