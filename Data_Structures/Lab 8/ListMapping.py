class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key) + " : " + str(self.value)

class ListMapping:
    def __init__(self):
        self._entries = []

    def _entry(self, key):
        """ Scan through all entries in the list. """
        #Returns the entry if the key exists.
        for entry in self._entries:
            if entry.key == key:
                return entry
        #Otherwise return None
        return None

    def put(self, key, value):
        """ Add key-value entry. """
        #If key already exist, update its value
        for entry in self._entries:
            if entry.key == key:
                entry.value = value
                return

        #else add the new key-value pair
        self._entries.append(Entry(key, value))
        return

    def get(self, key):
        """ Returns the value associated with key. """

        #scan through the list with the help of _entry() method
        # Raise KeyError if the input key does not exist
        if self._entry(key) == None:
            raise KeyError
        return self._entry(key).value

    def remove(self, key):
        """ Remove the object associated with key. """
        for entry in self._entries:
            if entry.key == key:
                self._entries.remove(entry)
        return

    def __len__(self):
        """ Returns total number of entries added in the list. """
        return len(self._entries)

    def __contains__(self, key):
        """ Returns True if key exist, else returns False. """
        if self._entry(key) is None:
            return False
        else:
            return True

    def items(self):
        """ Returns an iterator over the key-value pairs as tuples. """
        return ((e.key, e.value) for e in self._entries)

if __name__ == "__main__":
    map = ListMapping()
    map.put(1, "one")
    map.put(2, "two")
    map.put(3, "three")
    map.put(4, "four")
    print(map.get(1))
    print(map.get(3))
    print(map.get(4))
    map.remove(3)
    print(map.get(3))