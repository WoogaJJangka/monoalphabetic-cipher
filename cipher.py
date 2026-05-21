from collections import deque

class Cipher:
    def __init__(self):
        self._key = ""
        self._cipher_alphabets = ""
        self._alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    def setKey(self, key : str):
        self._key = key

    def getCipherAlphabets(self):
        print(f"Key : {self._key}")
        return self._cipher_alphabets

    def generate_cipher_alphabet(self, key):
        self._key = key
        used = []
        cipher = ""
        for char in key:
            if char not in used:
                used.append(char)
                cipher += char
            else:
                continue

        alphabets_d = deque(self._alphabets)
        alphabets_d.rotate(-alphabets_d.index(cipher[-1]))

        for char in list(alphabets_d):
            if char not in used:
                cipher += char
            else:
                continue

        self._cipher_alphabets = cipher
        

    def encrypt(self, plaintext : str, key : str):
        self.generate_cipher_alphabet(key)
        ciphertext = ""

        for plainchar in plaintext:
            for alphabet in self._alphabets:
                if plainchar == alphabet:
                    ciphertext += self._cipher_alphabets[self._alphabets.index(alphabet)]
                else:
                    continue
                
        print(f"ciphertext : {ciphertext}")
        return ciphertext

    def decrypt(self, ciphertext, key : str):
        self.generate_cipher_alphabet(key)
        plaintext = ""

        for cipherchar in ciphertext:
            for cipher_alphabet in self._cipher_alphabets:
                if cipherchar == cipher_alphabet:
                    plaintext += self._alphabets[self._cipher_alphabets.index(cipher_alphabet)]
                else:
                    continue
        
        print(f"plaintext : {plaintext}")
        return plaintext


if __name__ == "__main__":
    c = Cipher()
    c.encrypt("monoalphabeticsubstitution", "month")
    c.decrypt("telxsehvthvmgpsiwhn", "value")