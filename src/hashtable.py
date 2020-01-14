# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next

    def __getitem__(self, key):
        if key == self.key:
            return self.value
        else:
            if self.next is not None:
                return self.next[key]
            else:
                return None

    def remove(self, key, parent=None):
        if key == self.key:
            if parent:
                parent.next = self.next
                return parent
            else:
                return self.next
        else:
            self.next.remove(key)
            return self

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.keys = set()
        self.filled = 0

    def __repr__(self):
        pairs = []
        for key in self.keys:
            value = self.retrieve(key)
            pairs.append(f'{key}:{value}')
        return '\n'.join([str(self.capacity), str(self.filled)] + pairs)
        

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is None:
            self.storage[index] = LinkedPair(key, value)
            self.filled += 1
            self.keys.add(key)
            if self.filled == self.capacity:
                self.resize()
        else:
            new_entry = LinkedPair(key, value, self.storage[index])
            self.storage[index] = new_entry
            self.keys.add(key)


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        if self.storage is None:
            raise RuntimeError('remove')
        index = self._hash_mod(key)
        runner = self.storage[index]
        if runner is None:
            raise KeyError
        if runner.key == key:
            self.storage[index] = runner.next
        else:
            prev = runner
            runner = runner.next
            while runner is not None:
                if runner.key == key:
                    prev.next = runner.next
                    self.filled -= 1
                    return
                else:
                    prev = runner
                    runner = runner.next
            raise KeyError
            


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is None:
            return None
        else:
            return self.storage[index][key]


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        old_capacity = self.capacity
        self.capacity *= 2
        self.storage = [None] * self.capacity
        self.filled = 0
        for key in self.keys:
            index = self._hash(key) % old_capacity
            value = old_storage[index][key]
            self.insert(key, value)


        



if __name__ == "__main__":
    ht = HashTable(1)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")
    print(ht.keys)

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")