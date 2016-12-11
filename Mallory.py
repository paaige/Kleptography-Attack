# This program simulates the attack on the Discrete Log Attack
import sys
#intercept m1, m2 from file, a, b publically known
#make class where p,g member vars, add hash

def get_constants():
	a = 1
	b = 1
	W = 3
	return a, b, W
	
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
