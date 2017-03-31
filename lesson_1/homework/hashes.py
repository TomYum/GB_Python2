import hashlib


def make_hash(data, algo):
    if algo == 'md5':
        hash_algo = hashlib.md5(bytearray(data, 'utf-8'))
    elif algo == 'sha1':
        hash_algo = hashlib.sha1(bytearray(data, 'utf-8'))
    elif algo == 'sha512':
        hash_algo = hashlib.sha512(bytearray(data, 'utf-8'))
    else:
        raise ValueError('Неправильный алгоритм хэширования')
    return hash_algo.hexdigest()


print (make_hash('asdasd','md5'))
print (make_hash('asdasd','sha1'))
print (make_hash('asdasd','sha512'))