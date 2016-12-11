# Alice will get her private and public keys using the secure device,
# and send the public key to Bob.

from secure_device import *
from prime_generator import *

class Alice:

    def __init__(self):
        self.keys = get_keys()
        self.private_key = self.keys[0]
        self.public_key = self.keys[1]
        self.shared_key = 0
        self.prime = get_prime()

    def set_new_key(self):
        self.keys = get_keys()
        self.private_key = self.keys[0]
        self.public_key = self.keys[1]

    def get_public_key(self):
        return self.public_key

    def set_shared_key(self, className):
        self.class_public_key = className.get_public_key()
        self.shared_key = pow(self.class_public_key, self.private_key, self.prime)
