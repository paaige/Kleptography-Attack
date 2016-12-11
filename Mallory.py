# This program simulates the attack on the Discrete Log Attack
import sys
from secure_device import *
#intercept m1, m2 from file, a, b publically known
#make class where p,g member vars, add hash
class Mallory:

	def __init__(self):
		self.a = 1
		self.b = 1
		self.W = 3

                s = secure_device()
                self.keys = s.get_keys()
                self.private_key = self.keys[0]
                self.public_key = self.keys[1]

	def get_constants(self):
		return self.a, self.b, self.W

	def gen_attack_vars(a, b, g, p):
		#get m1 from file
		#r = pow(m1,a) * pow(g,b,p)
		#z_1 = m1/(pow(r,X))
		#get m2 from file
		#if m2 == pow(g,
		#		c2 = H(z1)
		#elif m2 == pow(g,).
		#		c2 = H(z2)
		return 


