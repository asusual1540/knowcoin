import hashlib
import json

def crypto_hash(*args):
    str_args = sorted(map(lambda data: json.dumps(data), args))
    joined_data = ''.join(str_args)
    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    print(f"crypto_hash('foo') : {crypto_hash('bar', 'foo')}")
    print(f"crypto_hash('foo') : {crypto_hash('foo', 'bar')}")

if __name__ == '__main__':
    main()