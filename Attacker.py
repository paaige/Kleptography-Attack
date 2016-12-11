# This program simulates the attack on the Discrete Log Attack
import sys
from secure_device import *
class Attacker:

    def __init__(self,a,b,W):
        self.a = a
        self.b = b
        self.W = W
        self.private_key = 0
        self.public_key = 1

    def get_constants(self):
        return self.a, self.b, self.W, self.public_key

    def set_new_key(self,device):
        self.private_key, self.public_key = device.get_new_keys()

    def get_public_key(self):
        return self.public_key

    def compute_key(m1,m2,g,p):
        H = hashlib.sha256();
        r = pow(m1,a,p)*pow(g,b,p);
        z1 = m1*pow(r,-X,p);
        if m2 == pow(g,H,z1):
            return z1;
        z2 = z1*pow(g,-W,p);
        if m2 == pow(g,H,z2):
            return z2;



