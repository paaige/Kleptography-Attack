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

