# This generates a random public and private key for Alice. Note that this
# will also be used to generate a random public and private key for the
# attacker.

# This program takes a file containing a prime p and a generator g as input
# Outputs a private key and a public key for Alice into a file
# "Alice-key.txt". It will output a file "attacker-key.txt" if
# "Alice-key.txt" already exists.

import sys
import os
from protocol import get_gen, gen_prime, get_exp
from random import SystemRandom

'''if len(sys.argv) < 2:
    sys.exit("Please enter a file name")
'''
generator = get_gen()
prime = get_prime()

# find private and public key
find_num = SystemRandom()
private_key = find_num.randrange(int(prime))
public_key = pow(int(generator), private_key) % int(prime)

# Alice-key.txt does exist -- create attacker-key.txt
try:
    alice = open("Alice-key.txt", 'r')

# Alice-key.txt does not exist -- create it
except:
    alice = open("Alice-key.txt", 'w')
    alice.write(str(private_key)+'\n')
    alice.write(str(public_key))
    sys.exit()

attacker = open("attacker-key.txt", 'w')
attacker.write(str(private_key)+'\n')
attacker.write(str(public_key))
