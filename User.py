# Diffie-Hellman user will get his/her private and public keys using a devicedevice
# and send the public key to other user

class User:

    def __init__(self):
        self.private_key = 0
        self.public_key = 1
        self.shared_key = 1

    def set_new_key(self,device):
        self.private_key, self.public_key = device.get_keys()

    def get_public_key(self):
        return self.public_key

    def set_shared_key(self, className):
        self.class_public_key = className.get_public_key()
        self.shared_key = pow(self.class_public_key, self.private_key, self.prime)

