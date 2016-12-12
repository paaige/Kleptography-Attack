#This is where the protocol will play out, we will call all relevant functions here and simulate Alice/Bob communication and attacker interception in this script

from Attacker import *
from User import *
from secure_device import *
from setup_device import *

def main():
    g = get_generator()
    p = get_prime()
    secure_dh = secure_device()
    Alice = User()
    Alice.set_new_key(secure_dh)
    Mallory = Attacker(0,1,3)
    Mallory.set_new_key(secure_dh)
    setup_dh = setup_device(Mallory)
    Bob = User()
    Bob.set_new_key(setup_dh)

	#Alice generates keys, sends public key to Bob over public channel
	#Bob generates keys, sends public key to Alice over public channel
	#Mallory computes keys, sends shared key out over shared channel

    m1 = Bob.get_public_key();
    for i in range(4):
        Alice.set_new_key(secure_dh)
        Bob.set_new_key(setup_dh)
        m2 = Bob.get_public_key();
        c2 = Mallory.compute_key(m1,m2,g,p)
        m1 = m2
        


if __name__ == "__main__":
	main()
