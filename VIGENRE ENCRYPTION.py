import random
import string

def generate_key(length=4):
    print (''.join(random.choices(string.ascii_uppercase, k=length)))


generate_key()

def preprocess(text):
    """Remove non-alphabetic characters and convert to uppercase."""
    return ''.join(filter(str.isalpha, text.upper()))
"""
    vigenere_decrypt(ciphertext, key):
Decrypt ciphertext using the Vigenère cipher with the given key
    ciphertext = preprocess(ciphertext)
    key = preprocess(key)
    key = (key * ((len(ciphertext) // len(key)) + 1))[:len(ciphertext)]

    plaintext = ''
    for c, k in zip(ciphertext, key):
        shift = (ord(c) - ord(k) + 26) % 26
        plaintext += chr(shift + ord('A'))
    return plaintext

# Example usage
ciphertext_input = input("Enter the ciphertext: ")
key_input = input("Enter the key: ")

decrypted_message = vigenere_decrypt(ciphertext_input, key_input)
print("\nDecrypted Message:", decrypted_message)
"""
class Victor_decrypt:
    def _init_(self):
        self.ccipher={
        'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16, 'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
        self.lcipher= { i:chr(i+65) for i in range (26) }
    def capitalize(self,text):
        return ''.join(filter(str.isalpha, text.upper()))

    def vigengre_decrypt(self,cipher,key):#this function is to capitalize each words
        cipher=self.capitalize(cipher)
        key=self.capitalize(key) 
        key = (key*(len(cipher)//len(key)+1))[:len(cipher)] 
       
        plaintext = " "
        for c,k in zip(cipher,key):
             c_code = self.ccipher[c]
             k_code = self.ccipher[k]
             p_letter= ((c_code-k_code)+26)%26
             plaintext += self.lcipher[p_letter]
        print (plaintext)            
    """ This would repeat the key until it becomes the length of the cipher"""

c= input("Enter the cipher key")
k=input("Enter the key")

vigengre_decrypt(c,k)
"""
def decrypt():
    ccipher={
        'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'0':14,'P':15,'Q':16, 'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
    lcipher={ i:chr(i+65) for i in range (26) }
    plaintext = " "
    for c,k in zip(cipher,key){
        c_code = ccipher[c]
        k_code = ccipher[k]
        p_letter= ((c_code-k_code)+26)%26
        plaintext += lcipher(p_letter)
                
    }

    }"""


