#This is where the protocol will play out, we will call all relevant functions here and simulate Alice/Bob communication and attacker interception in this script

from Mallory import *
from Alice import *
from Bob import *

def main():
	alice = Alice()
	mal = Mallory()
	a,b, W = mal.get_constants()
	bob = Bob()
	
	#Alice generates keys, sends public key to Bob over public channel
	#Bob generates keys, sends public key to Alice over public channel
	#Mallory computes keys, sends shared key out over shared channel

if __name__ == "__main__":
	main()
