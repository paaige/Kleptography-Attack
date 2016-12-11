#This is where the protocol will play out, we will call all relevant functions here and simulate Alice/Bob communication and attacker interception in this script

from Attacker import *
from User import *

def main():
    Alice = User()
    Bob = User()
    Mallory = Attacker(0,1,3)
	
	#Alice generates keys, sends public key to Bob over public channel
	#Bob generates keys, sends public key to Alice over public channel
	#Mallory computes keys, sends shared key out over shared channel

if __name__ == "__main__":
	main()
