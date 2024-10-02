"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Nicholas Klassen
ID:      169062164
Email:   klas2164@mylaurier.ca
__updated__ = "2024-03-23"
-------------------------------------------------------
"""
from BST_linked import BST as new_slot

class Hash_Set:
    """
    Constants.
    """
    _LOAD_FACTOR = 20

    def __init__(self, capacity):
        """
        Initializes an empty Hash_Set with the given capacity.
        """
        self._capacity = capacity
        self._table = [new_slot() for _ in range(self._capacity)]
        self._count = 0

    def __len__(self):
        """
        Returns the number of values in the Hash Set.
        """
        return self._count

    def is_empty(self):
        """
        Determines if the Hash Set is empty.
        """
        return self._count == 0

    def _find_slot(self, key):
        """
        Returns the slot for a given key value.
        """
        hash_key = hash(key) % self._capacity
        return self._table[hash_key]

    def __contains__(self, key):
        """
        Determines if the Hash Set contains a specific key.
        """
        slot = self._find_slot(key)
        return key in slot

    def insert(self, value):
        """
        Inserts a value into the Hash Set, allowing only one copy of the value.
        Calls _rehash if the Hash Set _LOAD_FACTOR is exceeded.
        """
        slot = self._find_slot(value)

        if value in slot:
            inserted = False
        else:
            inserted = True
            slot.insert(value)
            self._count += 1
            if self._count > (Hash_Set._LOAD_FACTOR * self._capacity):
                self._rehash()
        return inserted

    def remove(self, key):
        """
        Removes the value matching the given key from the Hash Set, if it exists.
        """
        slot = self._find_slot(key)
        value = slot.remove(key)

        if value is not None:
            self._count -= 1
        return value

    def _rehash(self):
        """
        Increases the number of slots in the Hash Set and reallocates the
        existing data within the Hash Set to the new table.
        """
        temp_table = self._table
        self._capacity = self._capacity * 2 + 1
        self._table = [new_slot() for _ in range(self._capacity)]
    
        for old_slot in temp_table:
            for item in old_slot:
                slot = self._find_slot(item)
                slot.insert(item)

    def __iter__(self):
        """
        Generates a Python iterator. Iterates through the hash set
        from the first to the last slots. Assumes the slot has its own iterator.
        """
        for slot in self._table:
            for item in slot:
                yield item