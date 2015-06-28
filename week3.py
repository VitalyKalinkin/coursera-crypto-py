from Crypto.Hash import SHA256
import binascii

def programming_assignment():
    test_file_name = '/Users/lattyf/Downloads/6 - 2 - Generic birthday attack (16 min).mp4'
    print("Resulting hash of of file '%s': \t'%s'" % (test_file_name, hash_file(test_file_name)))
    
    task_file_name = '/Users/lattyf/Downloads/6 - 1 - Introduction (11 min).mp4'
    print("Resulting hash of of file '%s': \t\t\t\t'%s'" % (task_file_name, hash_file(task_file_name)))

def hash_file(filename):
    fh = open(filename, "rb")

    content = fh.read()
    n = len(content) // 1024
    
    sha = SHA256.new()
    sha.update(content[n * 1024:])
    cur_hash = sha.digest()

    for i in range(n, 0, -1):
        block = content[(i - 1) * 1024 : i * 1024]
        block_and_hash = block + cur_hash
        
        sha_in = SHA256.new()
        sha_in.update(block_and_hash)

        cur_hash = sha_in.digest()

    fh.close()

    return binascii.b2a_hex(cur_hash)
