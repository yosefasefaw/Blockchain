# STEP1: I imported the necessary librairies

import time
import hashlib


# STEP2: I created a class of Block

# in this first function,I took 4 parameters,
# index=being the index of the Block in Blockchain list
# proof= this is a number which will be generated during mining,if the mining was good,a Block will be created using this Proof
# previous_hash= this contains the information(hashes) of the previous block in the blockchain.
# transaction= this is a list which contains all transation records

class Block(object):
    def __init__(self, index, proof, previous_hash, transactions):
        self.index = index
        self.proof = proof
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp =time.time()

    # here, I add a functionality to the objet above without modifying its structure with the help of the decorator @property
    # this functionality is the following function "get_block_hash"
    # It will calculate an hash based on the above parameters.
    # How? it will take the parameters above and put it into a string with the help of the in-build function .format()
    # hashlib. = hashing function taking variable length of bytes and converts it into a fixed length sequence
    # sha256= an authentication and encryption algorithm (bitcoin use it as well)
    # encode()=Converts the string into bytes to be acceptable by hash function.
    # hexdigest()=Returns the encoded data in hexadecimal format.

    @property
    def get_block_hash(self):
        block_string = "{}{}{}{}{}".format(self.index, self.proof, self.previous_hash, self.transactions,
                                           self.timestamp)
        return hashlib.sha256(block_string.encode()).hexdigest()

    # __repr__ is a built-in function used to compute the "official" string of an object
    # whereas __str__ is a built-in function that computes the "informal" string representation
    def __repr__(self):
        return "{} - {} - {} - {} - {}".format(self.index, self.proof, self.previous_hash, self.transactions, self.timestamp)

# STEP3: I created a class of blockchain


# self.chain= this will contain all the blocks
# self.current_node_transactions= It's the list of all transactions which will be then inserted to the block
# self.create_genesis_block= this is the first block, the so-called genesis block

class BlockChain(object):
    def __init__(self):
        self.chain = []
        self.current_node_transactions = []
        self.create_genesis_block()

    # I created the genesis block, with arbitrary values for proof and previous hash.

    def create_genesis_block(self):
        self.create_new_block(proof=0, previous_hash=0)

    # I created the function which will enables us to create new block
    # The function takes as element the proof ( the number which will be generated while mining), and the previous hash

    def create_new_block(self, proof, previous_hash):
        block = Block(
            index=len(self.chain),
            proof=proof,
            previous_hash=previous_hash,
            transactions=self.current_node_transactions
        )
        # here, I reset the transaction List,in order to have new information in it for the new block
        self.current_node_transactions = []
        # here, I added the block to the chain in order to have a blockchain
        self.chain.append(block)
        return block

    # Here, I created a function which will contain the transaction of the blockchain,
    # In order to do, I take the node (list of transaction which has been reset) and append a dicitionary of information

    def create_new_transaction(self, sender, recipient, amount):
        self.current_node_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

        # Here , I returned the new block's index where this transaction will be stored
        # get_last_block.index will be explain afterwards
        return self.get_last_block.index + 1

    # here by using the static method and the function, i created a proof of work
    # what is a proof of work?  this is an algorithm used to confirm transactions and produce new blocks to the chain
    # what is a static method?
    # Static methods, much like class methods, are methods that are bound to a class rather than its object.
    @staticmethod
    def create_proof_of_work(previous_proof):
        proof = previous_proof + 1
        while (proof + previous_proof) % 7 != 0:
            proof += 1

        return proof
    # this Last method enables me to get the last block of the chain
    @property
    def get_last_block(self):
        return self.chain[-1]

# STEP4: Let's test our Blockchain

blockchain = BlockChain()
print("""

The output should be as follow: the index - the proof - the previous hash - [the transaction] - the associated timestamp, - NEXT BLOCK 

""")
print("""

    Before Mining
    
    """)
print(blockchain.chain)

last_block = blockchain.get_last_block
last_proof = last_block.proof
proof = blockchain.create_proof_of_work(last_proof)


blockchain.create_new_transaction(
    sender="Satoshi Nakamoto",
    recipient="Yosef Asefaw",
    amount=1000000000,
)

last_hash = last_block.get_block_hash
block1= blockchain.create_new_block(proof, last_hash)

print("""

    After Mining
    
    """ )
print(blockchain.chain)

last_block = blockchain.get_last_block
last_proof = last_block.proof
proof = blockchain.create_proof_of_work(last_proof)


blockchain.create_new_transaction(
    sender="Yosef Asefaw",
    recipient="UNICEF",
    amount=1000000000,
)

last_hash = last_block.get_block_hash
block2= blockchain.create_new_block(proof, last_hash)
print(blockchain.chain)


