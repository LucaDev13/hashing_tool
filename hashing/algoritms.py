import hashlib


def sha1_encryption(string):
    encoded_string = string.encode('utf-8')
    encrypted_string = hashlib.sha1(encoded_string).hexdigest()
    print('\n' + '=> Encrypted with sha1 algorithm: ' + encrypted_string + '\n')
    return encrypted_string


def sha224_encryption(string):
    encoded_string = string.encode('utf-8')
    encrypted_string = hashlib.sha224(encoded_string).hexdigest()
    print('\n' + '=> Encrypted with sha224 algorithm: ' + encrypted_string + '\n')
    return encrypted_string


def sha256_encryption(string):
    encoded_string = string.encode('utf-8')
    encrypted_string = hashlib.sha256(encoded_string).hexdigest()
    print('\n' + '=> Encrypted with sha256 algorithm: ' + encrypted_string + '\n')
    return encrypted_string


def sha512_encryption(string):
    encoded_string = string.encode('utf-8')
    encrypted_string = hashlib.sha512(encoded_string).hexdigest()
    print('\n' + '=> Encrypted with sha512 algorithm: ' + encrypted_string + '\n')
    return encrypted_string


def sha3_224_encryption(string):
    encoded_string = string.encode('utf-8')
    encrypted_string = hashlib.sha3_224(encoded_string).hexdigest()
    print('\n' + '=> Encrypted with sha3_224 algorithm: ' + encrypted_string + '\n')
    return encrypted_string


def md5_encryption(string):
    encoded_string = string.encode('utf-8')
    encrypted_string = hashlib.md5(encoded_string).hexdigest()
    print('\n' + '=> Encrypted with md5 algorithm: ' + encrypted_string + '\n')
    return encrypted_string
