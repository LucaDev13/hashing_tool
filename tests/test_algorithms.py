from hashing.algoritms import sha1_encryption, sha224_encryption, sha256_encryption, sha512_encryption, md5_encryption, sha3_224_encryption

def test_sha1_algorithm():
    string = 'Python'
    test_sha1 = sha1_encryption(string)

    assert test_sha1 == '6e3604888c4b4ec08e2837913d012fe2834ffa83'

def test_sha224_algorithm():
    string = 'Python'
    test_sha224 = sha224_encryption(string)

    assert test_sha224 == 'f8fef02326b9f70d67c68faefc4d41b3fd039d77e11643bccab9d47a'
    
def test_sha256_algorithm():
    string = 'Python'
    test_sha256 = sha256_encryption(string)
    
    assert test_sha256 == '18885f27b5af9012df19e496460f9294d5ab76128824c6f993787004f6d9a7db'


def test_sha512_algorithm():
    string = 'Python'
    test_sha512 = sha512_encryption(string)

    assert test_sha512 == 'fd9d4d5b7a8a8fae6b1bc099b799110f7e4338606e2610f5d9506a4346e0c3bfbc525f4eed1e05aa8c6f46b8efff526ec48b500928a1b341ade5a7855f533932'

def test_sha3_224_algorithm():
    string = 'Python'
    test_sha3_224 = sha3_224_encryption(string)
    
    assert test_sha3_224 == 'fc702ae5a7c56e60a880a5bcfe45d1e763682ddb39d531c38820bb00'

def test_md5_algorithm():
    string = 'Python'
    test_md5 = md5_encryption(string)

    assert test_md5 == 'a7f5f35426b927411fc9231b56382173'
