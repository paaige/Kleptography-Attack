import math
import random
import hashlib

# This generates the "random" public and private key for Bob. This is the algorithm that contains
# a backdoor and will be attacked.


#Follows kleptography paper

#Define constants
p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF
g = 2;
W = 1;
a = 1;
b = 1;
Y = 1;

#Get assistive functions
prg = random.SystemRandom();
H = hashlib.sha256();

#Algorithm
c1 = prg.randrange(p-1)+1;
#m1 = pow(g,c1)%p; #Need to implement fast modular exponentiation
t = prg.randrange(2);
z = 3; #pow(g,((c1-W*t)%(p-1)))*pow(Y,((-a*c1-b)%(p-1))); #Need to implement fast modular exponentiation\
H.update(b'ttt');
c2 = H.hexdigest();
#m2 = pow(g, c2)%p;
print(c2);