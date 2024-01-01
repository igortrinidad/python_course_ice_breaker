import hashlib

def hash_string(string):
    hash_object = hashlib.sha256(string.encode())
    return hash_object.hexdigest()