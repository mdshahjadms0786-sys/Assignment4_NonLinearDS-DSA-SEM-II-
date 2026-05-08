# Simple Bloom Filter demo (toy version)

import hashlib

class BloomFilter:
    def __init__(self, size=20):
        self.size = size
        self.bit_array = [0]*size

    def _hashes(self, item):
        h1 = int(hashlib.md5(item.encode()).hexdigest(), 16) % self.size
        h2 = int(hashlib.sha1(item.encode()).hexdigest(), 16) % self.size
        return [h1, h2]

    def add(self, item):
        for h in self._hashes(item):
            self.bit_array[h] = 1

    def check(self, item):
        return all(self.bit_array[h] == 1 for h in self._hashes(item))

if __name__ == "__main__":
    bf = BloomFilter()
    bf.add("apple")
    print("Check apple:", bf.check("apple"))
    print("Check banana:", bf.check("banana"))



# Check apple: True
# Check banana: False   (or True sometimes, due to false positives)
