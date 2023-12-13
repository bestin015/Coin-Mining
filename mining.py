from hashlib import sha256
import time
def SHA256(text):
    return sha256(text.encode('ascii')).hexdigest()

def mine(block_number,transactions,previous_hash,prefix_zeroes):
    prefix_str='0'*prefix_zeroes
    for nonce  in range(1000000000000000000):
        text=str(block_number)+transactions+previous_hash+str(nonce)
        new_hash=SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"successfully mined one bitcoin with nonce value {nonce}")
            return new_hash
    raise BaseException(f"couldnt find any nonce at {nonce}")
if __name__=='__main__':
    transactions='''
    dreamer->dreams->21 
    wisher->wishs->21
    '''
    difficulty=6
    previous_hash='e46240714b5db3a23eee60479a623efba4d633d27fe4f03c904b9e219a7fbe60'
    start=time.time()
    print("Start mining")
    new_hash=mine(5,transactions,previous_hash,difficulty)
    total_time=str(time.time()-start)
    print(f"found coin at {total_time}")
    print(new_hash)