# Hash Table with separate chaining

class HashTable:
    def __init__(self, size=5):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return key % self.size

    def insert(self, key, value):
        h = self._hash(key)
        self.table[h].append((key, value))

    def get(self, key):
        h = self._hash(key)
        for k, v in self.table[h]:
            if k == key:
                return v
        return None

    def delete(self, key):
        h = self._hash(key)
        self.table[h] = [(k, v) for k, v in self.table[h] if k != key]

if __name__ == "__main__":
    ht = HashTable()
    ht.insert(1, "A")
    ht.insert(6, "B")  # collision with 1
    print("Table:", ht.table)
    print("Get 6:", ht.get(6))
    ht.delete(1)
    print("After delete 1:", ht.table)


# Table: [[(1, 'A'), (6, 'B')], [], [], [], []]
# Get 6: B
# After delete 1: [[(6, 'B')], [], [], [], []]
