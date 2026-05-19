class Ciper:
    def __init__(self, keyword : str):
        self._key = None
        self._used_alphabets = set(keyword.lower())
        self._alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    def getKey(self):
        print(f"Key : {self._key}")
        return self._key

    def make_key(self):
        unused_alphabets = self._alphabets
        for char in self._used_alphabets:
            unused_alphabets.remove(char)
        self._key = unused_alphabets
        print(self._key)
        

test = Ciper("abc")
print(test._alphabets)
test.getKey()
test.make_key()