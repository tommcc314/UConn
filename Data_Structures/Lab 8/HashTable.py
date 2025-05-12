from ListMapping import ListMapping

class HashTable:
    def __init__(self):
        self._htsize = 5     #initial size of hash table
        self._buckets_array = [ListMapping() for i in range(0,self._htsize)] #initialize bucket array of size _htsize
        self._n = 0         #number of items added in map

    def _get_bucket(self, key):
        """ Returns the right jth bucket depending on key. """
        return hash(key) % self._htsize

    def put(self, key, value):
        """ put the key-value pair in the right bucket. """
        self._buckets_array[self._get_bucket(key)].put(key, value)
        self._n += 1
        if self._n > self._htsize:
            self._double()
        return


    def get(self, key):
        """ Returns the value associated with key from the right bucket. """
        return self._buckets_array[self._get_bucket(key)].get(key)


    def remove(self,key):
        """ Remove the object associated with key. """
        #After removing, decrease the size of entries in map
        self._buckets_array[self._get_bucket(key)].remove(key)
        self._n -= 1
        return

    def _double(self):
        """ Doubles the size of hash table. """
        #Create a new hash table with size double the original one
        #After creating a new double-sized hash table, add the contents
        #of original hash table in it.
        old_bucket_array = self._buckets_array
        self._n = 0
        self._htsize *= 2
        self._buckets_array = [ListMapping() for i in range(0,self._htsize)]
        for bucket in old_bucket_array:
            for entry in bucket._entries:
                self.put(entry.key, entry.value)
        return

if __name__ == "__main__":
    HM = HashTable()

    HM.put(1, "one")
    HM.put(2, "two")
    HM.put(3, "three")
    HM.put(4, "four")
    HM.put(5, "five")
    HM.put(6, "six")
    HM.put("ten", 10)

    assert(HM.get(2) == "two")
    assert(HM.get(4) == "four")
    assert(HM.get("ten") == 10)
    assert(HM._htsize == 10)
    assert(HM._n == 7)
    print("PASSED")
