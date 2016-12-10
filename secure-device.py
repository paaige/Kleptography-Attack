# Generates a private and public key. Will be used for Mallory.py and Alice.py

import sys
import os
from prime_generator import *
from random import SystemRandom

generator = get_generator()
prime = get_prime()

def get_keys():
    find_num = SystemRandom()
    private_key = find_num.randrange(prime)

    public_key = pow(generator, private_key, prime)
    return private_key, public_key
