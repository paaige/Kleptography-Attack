import math
import random
import hashlib

# This generates the "random" public and private key for Bob. This is the algorithm that contains
# a backdoor and will be attacked.


#Follows kleptography paper

#Define constants
def gen_constants():
	W = 1;
	a = 1;
	b = 1;
	Y = 1;
	print "Public:"
	print "--------------------------------------------------"
	print "Prime p: ",p
	print "--------------------------------------------------"
	print "Generator g: ",g
	print "--------------------------------------------------"
	return p, g, W, a, b, Y

t = prg.randrange(2); #this is 0.. ?
	z = pow(g,((c1-W*t)%(p-1)),p)*pow(Y,((-a*c1-b)%(p-1)),p);
	H.update(b'ttt');
	c2 = H.hexdigest(); #get hash from int to int
	m2 = pow(g, int(c2, 16),p);
	print "--------------------------------------------------"
	print "Sending message 2: m2 is :", m2
	print "--------------------------------------------------"
	return c1, m1, t, z, c2, m2
