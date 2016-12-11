#This is where the protocol will play out, we will call all relevant functions here and simulate Alice/Bob communication and attacker interception in this script

import math
import random
import hashlib
from prime_generator import *
from Mallory import *

class setup_device:
	
	def __init__(self):
            Mal = Mallory()
            self.Y = 1
            self.prev_key = -1
            self.a, self.b, self.W = Mal.get_constants()
            self.prg = random.SystemRandom()
            self.generator = get_generator()
            self.prime = get_prime()

	def get_new_keys(self):
	    if self.prev_key < 0:
	            self.c = self.prg.randrange(self.prime-1)+1;
	            self.prev_key = self.c;
	            self.m = pow(self.generator, self.c, self.prime);
	            return self.c, self.m
	    else:
	            self.c1 = self.prev_key
	            self.t = self.prg.randrange(2);
	            self.z = pow(self.generator,((self.c1-self.W*self.t)%(self.prime-1)),self.prime)*pow(self.Y,((-self.a*self.c1-self.b)%(self.prime-1)), self.prime);
	            H = hashlib.sha256()
	            H.update(bytes(str(z),'ascii'));
	            self.c = H.hexdigest();
	            self.prev_key = self.c;
	            self.m = pow(self.generator, int(self.c, 16), self.prime);
	            return self.c, self.m
