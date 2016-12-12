#This is where the protocol will play out, we will call all relevant functions here and simulate Alice/Bob communication and attacker interception in this script

import math
import random
import hashlib
from prime_generator import *

class setup_device:
	
    def __init__(self,attacker):
        self.generator = get_generator()
        self.prime = get_prime()
        
        self.Y = attacker.get_public_key()
        self.prev_key = -1
        self.a, self.b, self.W = attacker.get_constants()
        self.prg = random.SystemRandom()

    def get_keys(self):
        if self.prev_key < 0:
            self.c = self.prg.randrange(self.prime-1)+1;
            self.prev_key = self.c;
            self.m = pow(self.generator, self.c, self.prime);
            return self.c, self.m
        else:
            c1 = self.prev_key
            t = self.prg.randrange(2);
            z = (pow(self.generator,((c1-self.W*t)%(self.prime-1)),self.prime)*pow(self.Y,((-self.a*c1-self.b)%(self.prime-1)), self.prime))%self.prime;
            H = hashlib.sha256()
            H.update(bytes(str(z),'ascii'));
            self.c = int(H.hexdigest(),16);
            self.prev_key = self.c;
            self.m = pow(self.generator, self.c, self.prime);
            return self.c, self.m
