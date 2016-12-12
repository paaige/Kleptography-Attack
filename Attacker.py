# This program simulates the attack on the Discrete Log Attack
import sys
import hashlib
from secure_device import *
class Attacker:

    def __init__(self,a,b,W):
        self.a = a
        self.b = b
        self.W = W
        self.private_key = 0
        self.public_key = 1

    def get_constants(self):
        return self.a, self.b, self.W

    def set_new_key(self,device):
        self.private_key, self.public_key = device.get_keys()

    def get_public_key(self):
        return self.public_key

    def compute_key(self,m1,m2,g,p):
        r = pow(m1,self.a,p)*pow(g,self.b,p)
        z1 = (m1*pow(r,((-self.private_key)%(p-1)),p))%p
        h1 = hashlib.sha256()
        h1.update(bytes(str(z1),'ascii'))
        k1 = int(h1.hexdigest(),16)
        if m2 == pow(g,k1,p):
            return k1
        z2 = (z1*pow(g,((-1*self.W)%(p-1)),p))%p
        h2 = hashlib.sha256()
        h2.update(bytes(str(z2),'ascii'))
        k2 = int(h2.hexdigest(),16)
        if m2 == pow(g,k2,p):
            return k2
        else:
            return -1



