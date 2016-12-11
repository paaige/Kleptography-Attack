# Generates a private and public key. Will be used for Mallory.py and Alice.py

from prime_generator import *
from random import SystemRandom

class secure_device:

    def __init__(self):
        self.generator = get_generator()
        self.prime = get_prime()

    def get_keys(self):
        find_num = SystemRandom()
        self.private_key = find_num.randrange(self.prime)

        self.public_key = pow(self.generator, self.private_key, self.prime)
        return self.private_key, self.public_key
