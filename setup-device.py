#This is where the protocol will play out, we will call all relevant functions here and simulate Alice/Bob communication and attacker interception in this script

import math
import random
import hashlib
import prime-generator

def device_protocol():

	def __init__(self):
		self.p = get_prime();
		self.g = get_generator();
		print "--------------------------------------------------"
		print "Public large prime p ",p, " and generator ",g, " generated."
		print "--------------------------------------------------"
		self.prg = random.SystemRandom()
		self.W = 3 # or 1 or something.. we can test different values
		self.Y = 1 #public key
		self.prev_key = -1;
		
	def get_new_keys():
		if self.prev_key < 0:
			c = prg.randrange(p-1)+1;
			self.prev_key = c;
			m = pow(g,c1,p);
			return c,m
		else:
			c1 = self.prev_key
			t = prg.randrange(2);
			z = pow(g,((c1-W*t)%(p-1)),p)*pow(Y,((-a*c1-b)%(p-1)),p);
			H = hashlib.sha256()
			H.update(bytes(str(z),'ascii'));
			c = H.hexdigest();
			self.prev_key = c;
			m = pow(g, int(c, 16),p);
			return c, m

	
	def get_generator():
		return self.g

	def get_prime():
		return self.p

