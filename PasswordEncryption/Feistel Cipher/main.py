'''Feistel Cipher is as follows
1. Create a list of all plain text characters
2. Convert plain text to ASCII then 8-bit binary
3. Divide binary plain text string into two halves (L1 and R1)
4. Generate random binary keys (K1 and K2) of length equal to halves of plain text
5. Each round, XOR right half against against K1 or K2, and set L2 to previous right half
6. Encryption and Decryption should be same algorithm'''
import secrets

class feistel:
    def __init__(self):
        with open("plainTextCharacters.txt", "r") as file:
            self.plainText = file.read() #grab characters from file
            print(self.plainText)
            
    def round(self):    #iterate rounds of feistel encryption
        print("haha")
        
    def convertToAscii(self):   #convert from plain text to Ascii text
        self.ascii_text = [ord(char) for char in self.plainText]
        print(self.ascii_text)
    
    def convertTo8Bit(self):    #convert from Ascii text to 8 Bit Binary text
        self.binaryText = [format(val, '08b') for val in self.ascii_text]
        print(self.binaryText)
    
    def split(self):    #split the binary text into two halves
        q, r = divmod(len(self.binaryText), 2)
        self.R1, self.L1 = self.binaryText[:q + r], self.binaryText[q + r:]
        print(self.R1, self.L1)
        
    def generateKey(self):  #generate a random key using secrets library
        length = len(self.L1) * 8   #set length to 8 times size of halves (each letter is 8 bits)
        self.K1 = f'{secrets.randbits(length):0{length}b}'  #format randbits to n length binary values where n is size of halves in bits
        self.K2 = f'{secrets.randbits(length):0{length}b}'
        print(self.K1, self.K2)

obj1 = feistel()
obj1.convertToAscii()
obj1.convertTo8Bit()
obj1.split()
obj1.generateKey()