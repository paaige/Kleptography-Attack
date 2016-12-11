#This is where the protocol will play out, we will call all relevant functions here and simulate Alice/Bob communication and attacker interception in this script

import math
import random
import hashlib
from prime_generator import *
from Mallory import *

generator = get_generator();
prime = get_prime();

print "--------------------------------------------------"
print "Public large prime p ", prime, " and generator ", generator, " generated."
print "--------------------------------------------------"


prg = random.SystemRandom()

class setup_device:
	
	def __init__(self):
			Mal = Mallory()
			self.Y = 1
			self.prev_key = -1
			self.a, self.b, self.W = Mal.get_constants()

	def get_new_keys(self):
	    if prev_key < 0:
	            c = prg.randrange(p-1)+1;
	            prev_key = c;
	            m = pow(generator,c1,prime);
	            return c,m
	    else:
	            c1 = prev_key
	            t = prg.randrange(2);
	            z = pow(generator,((c1-W*t)%(prime-1)),prime)*pow(Y,((-a*c1-b)%(prime-1)),prime);
	            H = hashlib.sha256()
	            H.update(bytes(str(z),'ascii'));
	            c = H.hexdigest();
	            prev_key = c;
	            m = pow(generator, int(c, 16),prime);
	            return c, m
