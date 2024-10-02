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
from Sorted_List_array import Sorted_List
SEP = '-' * 40
class Hash_Set_sorted:
    """
    Array-based list version of the Hash Set ADT.
    """

    _LOAD_FACTOR = 20

    def __init__(self, capacity):
        """
        Initializes an empty Hash_Set with the given capacity.
        """
        self._capacity = capacity
        self._slots = []
        self._count = 0

        # Initialize the table with empty slots.
        for _ in range(self._capacity):
            self._slots.append(Sorted_List())

    def __len__(self):
        """
        Returns the number of values in the Hash_Set.
        """
        return self._count

    def is_empty(self):
        """
        Determines if the Hash_Set is empty.
        """
        return self._count == 0

    def _find_slot(self, key):
        """
        Returns the slot for a given key.
        """
        # Compute the hash value of the key and find the slot.
        hash_value = hash(key)
        slot_index = hash_value % self._capacity
        return self._slots[slot_index]

    def __contains__(self, key):
        """
        Determines if the Hash_Set contains a given key.
        """
        # Find the slot for the key and check if it's present.
        slot = self._find_slot(key)
        return key in slot

    def insert(self, value):
        """
        Inserts a value into the Hash_Set, allowing only one copy of the value.
        Calls _rehash if the Hash_Set _LOAD_FACTOR is exceeded.
        """
        # Find the slot for the value.
        slot = self._find_slot(value)

        # If the value is not already present, insert it.
        if value not in slot:
            slot.insert(value)
            self._count += 1
            # Check if rehashing is needed.
            if self._count > self._LOAD_FACTOR * self._capacity:
                self._rehash()
            return True
        else:
            return False

    def find(self, key):
        """
        Returns the value identified by a given key.
        """
        # Find the slot for the key and return the value.
        slot = self._find_slot(key)
        return slot.find(key)

    def remove(self, key):
        """
        Removes the value matching the given key from the Hash_Set, if it exists.
        """
        # Find the slot for the key and remove the value.
        slot = self._find_slot(key)
        if key in slot:
            slot.remove(key)
            self._count -= 1
            return key
        else:
            return None

    def _rehash(self):
        """
        Increases the number of slots in the Hash_Set and reallocates the
        existing data within the Hash_Set to the new table.
        """
        # Double the capacity and create a new table with the updated capacity.
        new_capacity = self._capacity * 2 + 1
        new_slots = [Sorted_List() for _ in range(new_capacity)]

        # Rehash the existing data into the new table.
        for slot in self._slots:
            for item in slot:
                hash_value = hash(item)
                new_slot_index = hash_value % new_capacity
                new_slots[new_slot_index].insert(item)

        # Update the table and capacity.
        self._slots = new_slots
        self._capacity = new_capacity

    def __eq__(self, other_set):
        """
        Determines whether two Hash_Sets are equal.
        """
        # Check if the other set is the same size.
        if len(self) != len(other_set):
            return False

        # Check if all values in self are present in other_set.
        for value in self:
            if value not in other_set:
                return False

        return True

    def debug(self):
        """
        Prints the contents of the Hash_Set starting at slot 0,
        showing the slot currently being printed. Used for
        debugging purposes.
        """
        # Print the number of slots.
        print(f"Number of Slots: {self._capacity}")

        # Print the contents of each slot.
        for i, slot in enumerate(self._slots):
            print(SEP)
            print(f"Slot {i}:")
            for item in slot:
                print(item)
            print(SEP)

    def __iter__(self):
        """
        Generates a Python iterator. Iterates through the hash set
        from first to last slots. Assumes slot has own iterator.
        """
        for slot in self._slots:
            for item in slot:
                yield item