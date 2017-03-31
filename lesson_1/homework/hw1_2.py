import hashlib
import os


def get_hash(what, hash_algo):
    """
    Get hash-sum
    :param what: input string
    :param hash_algo: hash algorithm
    :return: hexdigest

    >>> get_hash_summ("I'ts work", 'sha1')  # doctest: +NORMALIZE_WHITESPACE
    'c3f4ebc6302d45264c46fd7d994b6bb8e3f0f4bd'

    """

    hash_algo_dict = dict(md5=hashlib.md5,
                          sha1=hashlib.sha1,
                          sha224=hashlib.sha224,
                          sha256=hashlib.sha256,
                          sha384=hashlib.sha384,
                          sha512=hashlib.sha512
                          )

    if hash_algo not in hash_algo_dict.keys():
        raise ValueError('Неправильный алгоритм хэширования')

    hash_object = hash_algo_dict[hash_algo]()
    hash_object.update(what.encode('utf-8'))

    return hash_object.hexdigest()


def main():
    file_name = os.path.abspath(input('Enter path to file.csv:\n'))
    tmp_file_name = file_name + 'bak'

    file_handler = open(file_name, 'r');
    write_to = open(tmp_file_name, 'w')

    for line in file_handler:
        (string_data, algorithm, *hash_sum) = list(line.split(';'))
        try:
            hash_sum = get_hash(string_data, algorithm)
        except ValueError:
            hash_sum = 'error'
        finally:
            write_to.write(';'.join((string_data, algorithm, hash_sum)) + '\n')

    write_to.close()
    file_handler.close()

    os.rename(tmp_file_name, file_name)


if __name__ == '__main__':
    main()
