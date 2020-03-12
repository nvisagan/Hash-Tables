# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
 

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.size = 0


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
        '''
        index = self._hash_mod(key)
        node = self.storage[index]
        #Make while loop to keep checking our LL
        while node is not None and node.key !=key:
            #if not, make a copy of current pointer
            temp = node
            # current pointer  will point to the current's next node
            node = node.next
        
        #also check if its empty 
        if node is not None:
            node.value = value
        else:
            new_node = LinkedPair(key, value)
            new_node.next = self.storage[index]
            self.storage[index] = new_node
            #increase size by 1 
            self.size +=1

      



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a Warning if the key is not found.

        '''
        index = self._hash_mod(key)
        node = self.storage[index]
        #first check if the current place is not empty
        temp = None
        while node.key !=key:
            temp = node
            node = temp.next
        if node is None:
            return None
        else:
            if temp is None:
                result = node.value
                self.storage[index] = node.next
                return result
            else:
                self.size -=1
                temp.next = node.next
                return node.value



    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next
        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        '''
        old_storage = self.storage[:]
        self.capacity *= 2
        self.storage = [None] * self.capacity

        for bucket_item in old_storage:
            if bucket_item is not None:
                node = bucket_item
                while node:
                    self.insert(node.key, node.value)
                    node = node.next


        



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

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
