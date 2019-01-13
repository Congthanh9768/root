import time
import crypt
class Block:
    id, timestamp, previous_hash, data, block_hash
    def __init__(self,id, timestamp, previous_hash, data, block_hash):
        self.id = 0
        self.timestamp = ""
        self.previous_hash = ""
        self.block_hash = ""
        self.data= ""
        self.nonce = ""
    def Genesis(self,id, timestamp, previous_hash, data, block_hash):
        self.id = 0;
        self.timestamp = time.time()
        self.previous_hash =""
        self.data = "Nguyen van B co 12$"
        self.nonce
        str = str(self.id) + str(self.timestamp) + self.previous_hash + data + nonce
        self.block_hash = = crypt.METHOD_SHA256(str)
    def CreatBlock(self,id, timestamp, previous_hash, data, block_hash):
        
        self.id = id
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.data = data
        self.nonce = nonce
        self.block_hash = block_hash
class BlockChain:
    blockchain = list()
    def Check_chain(self):
        for block in blockchain:
            if(blockchain[i].previous_hash != blockchain[i-1].previous_hash):
                return false

    def Verify_Block(self):
        str = str(self.id) + str(self.timestamp) + (self.previous_hash) + self.data
        hash= crypt.METHOD_SHA256(str)
        if (hash == self.block_hash):
            return true
        else:
            return false


    def Mining_Block(self):
        str = str(self.id) + str(self.timestamp) + self.previous_hash + data + nonce
        nonce = 1
        while(str.METHOD_SHA256(str+ str(nonce)) < "00000000111111111111111111111111"):
























         

    
