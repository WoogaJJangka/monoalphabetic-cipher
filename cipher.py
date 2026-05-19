class Ciper:
    def __init__(self):
        self._key = ""
        self._cipher_alphabet = ""
        self._alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    def getKey(self):
        print(f"Key : {self._key}")
        return self._cipher_alphabet

    def generate_cipher_alphabet(self, key):
        self._key = key
        used_alphabets = set()
        unused_alphabets = self._alphabets
        temp_cipher_alphabet = ""
        for char in self._key:
            if char in used_alphabets:
                continue
            else:
                temp_cipher_alphabet += char
                used_alphabets.add(char)
                unused_alphabets.remove(char)
        
        for char in unused_alphabets:
            temp_cipher_alphabet += char

        self._cipher_alphabet = temp_cipher_alphabet

    def encrypt(self, plaintext, key = None):
        key = self._key if key is None else key
        ciphertext = ""

        for plainchar in plaintext:
            ciphertext += self._cipher_alphabet[self._alphabets.index(plainchar)]
        
        print(f"ciphertext : {ciphertext}")
        return ciphertext

    def decrypt(self, ciphertext, key = None):
        key = self._key if key is None else key
        plaintext = ""

        for cipherchar in ciphertext:
            plaintext += self._alphabets[self._cipher_alphabet.index(cipherchar)]
        
        print(f"plaintext : {plaintext}")
        return plaintext


if __name__ == "__main__":
    test = Ciper()

    test.generate_cipher_alphabet("halloword")
    test.getKey()