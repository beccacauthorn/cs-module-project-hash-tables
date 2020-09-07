class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """ 

    def __init__(self, capacity):
        self.hash_table = [None] * capacity 
        self.num_items = 0
        self.capacity = capacity  

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.hash_table)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """

        return self.num_items / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here

    def utf(self, key):
        string_utf = key.encode()

        total = 0

        for char in string_utf:
            total += char
            total &= 0xffffffff #limit total to 32 bits 
        return total 

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        #return self.djb2(key) % self.capacity
        return self.utf(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        i = self.hash_index(key)

        #find the start of the linked list using the index
        self.hash_table[i]

        #insert into this linked list a new hash table entry
        if self.hash_table[i] is None:
            e = HashTableEntry(key, value)
            self.hash_table[i] = e
            self.num_items =  self.num_items + 1

        else:
            # iterate over linked list and search to see if key already exists  
            cur_node = self.hash_table[i]
            while cur_node != None:
                if cur_node.key == key:
                    cur_node.value = value 
                    break
                else:
                    cur_node = cur_node.next 

            # we are at the end of the list, which means we ahve not found the key in the list
            if cur_node == None:

                # we need to create a new entry
                e = HashTableEntry(key, value)

                # now we need to choose where to add the new
                e.next = self.hash_table[i]
                self.hash_table[i] = e

                self.num_items =  self.num_items + 1
    
    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        #hash the key and get an index
        i = self.hash_index(key)
        # self.hash_table[i] = None

        #search through the linked list for the matching key
        cur_node = self.hash_table[i]
        prev_node = None
        while cur_node != None:
            if cur_node.key == key:
                # DELETE HERE: previous to point to next
                if prev_node != None:
                    prev_node.next = cur_node.next
                else:
                    self.hash_table[i] = cur_node.next

                # keep track of nmber of items
                self.num_items = self.num_items -1

                # RETURN THE DELETE VALUE  
                return cur_node.value

            else:
                prev_node = cur_node
                cur_node = cur_node.next

        return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        #hash the key and get index
        i = self.hash_index(key)
        #get the linked list at the computed index
        cur_node = self.hash_table[i]
        #search through the linked list for the key, compare keys until you find the right one
        #if it exists, return the value
        #else, return None 
        while cur_node != None:
            if cur_node.key == key:
                return cur_node.value
            else:
                cur_node = cur_node.next
        return None  


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        #make a new arrary that doubles the current size (duplicate array)
        old_capacity = self.capacity
        self.capacity = new_capacity

        old_table = self.hash_table
        self.hash_table = [None] * self.capacity

        #go through each linked list in the array
        
        for i in range(old_capacity):
            #go through each item and rehash it b/c with bigger array the index will be different
            cur_node = old_table[i]
            while cur_node != None:
                self.put(cur_node.key, cur_node.value)
                cur_node = cur_node.next



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
