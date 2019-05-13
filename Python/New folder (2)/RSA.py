from Crypto import RSA
from Crypto import Random 

random_generator = Random.new().read 
key = RSA.generate(1024, random_generator) 
exportedKey = key.exportKey('PEM', 'my secret', pkcs=1) 
