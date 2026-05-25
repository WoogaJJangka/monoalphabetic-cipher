from collections import deque
import time as t
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

    def crack_cipher_random(self, ciphertext = "kotcihndotmivhonucswthvaifcnsa"):
        start_time = t.time()
        key = ["a", "a", "a", "a", "a"]
        count = 1
        for a1 in self._alphabets:
            key[0] = a1
            for a2 in self._alphabets:
                key[1] = a2
                for a3 in self._alphabets:
                    key[2] = a3
                    for a4 in self._alphabets:
                        key[3] = a4
                        for a5 in self._alphabets:
                            key[4] = a5
                            
                            print(f"count: {count} ", end="")
                            self.decrypt(ciphertext, "".join(key))
                            count += 1


        end_time = t.time()
        total_time = end_time - start_time
        print(f"totla time : {total_time}")

    def crack_cipher_dictionary(self, ciphertext = "kotcihndotmivhonucswthvaifcnsa"):
        start_time = t.time()
        count = 1
        with open('dictionary.txt', 'r', encoding='utf-8') as f:
            for key in f:
                key = key.rstrip('\r\n')
                print(f"count: {count} ", end="")
                count += 1
                self.decrypt(ciphertext, key)
        end_time = t.time()
        total_time = end_time - start_time
        print(f"total time : {total_time}")

        
if __name__ == "__main__":
    c = Cipher()
    c.encrypt("monoalphabeticsubstitution", "month")
    c.decrypt("telxsehvthvmgpsiwhn", "value")
    c.crack_cipher_dictionary()