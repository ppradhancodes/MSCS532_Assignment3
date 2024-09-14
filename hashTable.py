class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size=1000):
        self.size = size
        self.table = [None] * size
        self.count = 0

    def _hash(self, key):
        # Simple hash function
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        if not self.table[index]:
            self.table[index] = HashNode(key, value)
            self.count += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value 
                    return
                if not current.next:
                    current.next = HashNode(key, value)
                    self.count += 1
                    break
                current = current.next
        
        # Resize if load factor exceeds 0.7
        if self.count / self.size > 0.7:
            self._resize()

    def search(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        index = self._hash(key)
        if not self.table[index]:
            return
        if self.table[index].key == key:
            self.table[index] = self.table[index].next
            self.count -= 1
            return
        current = self.table[index]
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                self.count -= 1
                return
            current = current.next

    def _resize(self):
        new_size = self.size * 2
        new_table = [None] * new_size
        for i in range(self.size):
            current = self.table[i]
            while current:
                index = hash(current.key) % new_size
                if not new_table[index]:
                    new_table[index] = HashNode(current.key, current.value)
                else:
                    node = new_table[index]
                    while node.next:
                        node = node.next
                    node.next = HashNode(current.key, current.value)
                current = current.next
        self.table = new_table
        self.size = new_size