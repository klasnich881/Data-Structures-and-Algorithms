"""
-------------------------------------------------------
Linked version of the Sorted_List ADT.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2024-03-03"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy


class _SL_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a sorted list node.
        Use: node = _SL_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            next_ - another sorted list node (_SL_Node)
        Returns:
            Initializes a list node that contains a copy of value
            and a link to the next node in the list.
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_
        return


class Sorted_List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Sorted_List.
        Use: sl = Sorted_List()
        -------------------------------------------------------
        Returns:
            a Sorted_List object (Sorted_List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = sl.is_empty()
        -------------------------------------------------------
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """

        # your code here

        return

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the list.
        Use: n = len(l)
        -------------------------------------------------------
        Returns:
            Returns the number of values in the list.
        -------------------------------------------------------
        """

        # your code here

        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts value at the proper place in the sorted list.
        Must be a stable insertion, i.e., consecutive insertions
        of the same value must keep their order preserved.
        Use: sl.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        new_node = _SL_Node(value, None)

        # Handle an empty list
        if self._front is None:
            self._front = self._rear = new_node
            self._count += 1
            return

        # Handle insertion at the beginning
        if value <= self._front._value:
            new_node._next = self._front
            self._front = new_node
            self._count += 1
            return

        # Handle insertion at the end
        if value >= self._rear._value:
            self._rear._next = new_node
            self._rear = new_node
            self._count += 1
            return

        # Handle insertion in the middle
        previous = None
        current = self._front

        while current is not None and current._value < value:
            previous = current
            current = current._next

        new_node._next = current
        previous._next = new_node
        self._count += 1

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the sorted list.
        Private helper method - used only by other ADT methods.
        Use: p, c, i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_SL_Node)
            current - pointer to the node containing key (_SL_Node)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """
        previous = None
        current = self._front
        index = 0

        while current is not None and current._value < key:
            previous = current
            current = current._next
            index += 1

        if current is not None and current._value == key:
            return previous, current, index
        else:
            return previous, current, -1

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in the sorted list that matches key.
        Use: value = sl.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        previous = None
        current = self._front

        while current is not None and current._value != key:
            previous = current
            current = current._next

        if current is None:
            # Key not found
            return None

        value = current._value

        if previous is None:
            # Removing the first node
            self._front = current._next
            if self._front is None:
                # The list is now empty
                self._rear = None
        else:
            # Removing a node that is not the first one
            previous._next = current._next
            if previous._next is None:
                # Updating _rear since the last node was removed
                self._rear = previous

        self._count -= 1
        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list and returns its value.
        Use: value = lst.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"

        value = self._front._value
        self._front = self._front._next

        if self._front is None:
            # The list is now empty
            self._rear = None

        self._count -= 1
        return value

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: l.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            All values matching key are removed from the list.
        -------------------------------------------------------
        """

        # your code here

        return

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in the list that matches key.
        Use: value = l.find( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        _, current, _ = self._linear_search(key)

        if current is not None:
            return deepcopy(current._value)
        else:
            return None

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in the list.
        Use: value = l.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        if self._front is not None:
            return deepcopy(self._front._value)
        return None

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = l.index( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of the location of key in the list, -1 if
              key is not in the list.
        -------------------------------------------------------
        """

        # your code here

        return

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(list) to len(list) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """

        # your code here

        return

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = sl[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of the list (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"
        current = self._front

        for _ in range(i):
            current = current._next

        return deepcopy(current._value)

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in sl
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """
        _, _, index = self._linear_search(key)
        return index != -1

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in the sorted list.
        Use: value = sl.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the sorted list (?)
        -------------------------------------------------------
        """
        if self._front is not None:
            return deepcopy(self._rear._value)
        return None

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in the sorted list.
        Use: value = sl.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the sorted list (?)
        -------------------------------------------------------
        """
        if self._front is not None:
            return deepcopy(self._front._value)
        return None

    def count(self, key):
        """
        -------------------------------------------------------
        Determines the number of times key appears in the sorted list.
        Use: n = sl.count(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            number - the number of times key appears in the sorted list (int)
        -------------------------------------------------------
        """
        count = 0
        current = self._front

        while current is not None:
            if current._value == key:
                count += 1
            elif current._value > key:
                break  # Since the list is sorted, no need to search further
            current = current._next

        return count

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the sorted list.
        Use: sl.clean()
        -------------------------------------------------------
        Returns:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """
        current = self._front
        previous = None
        unique_values = set()

        while current is not None:
            if current._value not in unique_values:
                unique_values.add(current._value)
                previous = current
                current = current._next
            else:
                # Duplicate value, remove the node
                if previous is None:
                    # Removing the first node
                    self._front = current._next
                else:
                    previous._next = current._next
                self._count -= 1
                current = current._next

        # Update rear if the list is not empty
        if self._front is not None:
            self._rear = previous
        else:
            self._rear = None
        return

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = lst.pop()
        Use: value = lst.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
            args[0], if it exists, is the index i
        Returns:
            value - if args exists, the value at position args[0], 
                otherwise the last value in the list, value is 
                removed from the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        previous = None
        current = self._front

        if len(args) == 1:
            i = args[0]

            if i < 0:
                # index is negative
                i = self._count + i
            j = 0

            while j < i:
                previous = current
                current = current._next
                j += 1
        else:
            # find and pop the last element
            j = 0

            while j < (self._count - 1):
                previous = current
                current = current._next
                j += 1

        value = current._value

        if previous is None:
            # Update the front
            self._front = current._next
        else:
            # Update any other node
            previous._next = current._next
        self._count -= 1
        return value

    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        (iterative algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        current1 = source1._front
        current2 = source2._front

        while current1 is not None and current2 is not None:
            if current1._value < current2._value:
                current1 = current1._next
            elif current2._value < current1._value:
                current2 = current2._next
            else:
                # Values are equal, insert into target and move both pointers
                self.insert(current1._value)
                current1 = current1._next
                current2 = current2._next

        return

    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (iterative algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (Sorted_List)
            source2 - an linked list (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        current1 = source1._front
        current2 = source2._front

        while current1 is not None and current2 is not None:
            value1 = current1._value
            value2 = current2._value

            if value1 < value2:
                self.insert(value1)
                current1 = current1._next
            elif value1 > value2:
                self.insert(value2)
                current2 = current2._next
            else:
                # Values are equal, insert only once
                self.insert(value1)
                current1 = current1._next
                current2 = current2._next

        # Insert any remaining values from source1
        while current1 is not None:
            self.insert(current1._value)
            current1 = current1._next

        # Insert any remaining values from source2
        while current2 is not None:
            self.insert(current2._value)
            current2 = current2._next
        return

    def split_th(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. At finish self is empty.
        Uses Tortoise/Hare algorithm.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """

        # your code here

        return

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits list so that target1 contains all values <= key,
        and target2 contains all values > key. At finish self is empty.
        Use: target1, target2 = lst.split_key()
        -------------------------------------------------------
        Returns:
            target1 - a new List of values <= key (List)
            target2 - a new List of values > key (List)
        -------------------------------------------------------
        """

        # your code here

        return

    def split_alt(self):
        """
        -------------------------------------------------------
        Split a List into two parts. even contains the even indexed
        elements, odd contains the odd indexed elements. At finish
        self is empty. Order of even and odd is not significant.
        (iterative version)
        Use: even, odd = l.split_alt()
        -------------------------------------------------------
        Returns:
            even - the even indexed elements of the list (Sorted_List)
            odd - the odd indexed elements of the list (Sorted_List)
                The List is empty.
        -------------------------------------------------------
        """

        # your code here

        return

    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. At finish self is empty.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """

        # your code here

        return

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two Sorted_Lists are equal.
        Values in self and target are compared, and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        -------------------------------------------------------
        Parameters:
            target - a sorted list (Sorted_List)
        Returns:
            equals - True if self contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        equals = True
        current_self = self._front
        current_target = target._front

        while current_self is not None and current_target is not None:
            if current_self._value != current_target._value:
                equals = False
            current_self = current_self._next
            current_target = current_target._next

        return equals

    def copy(self):
        """
        -------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (iterative version)
        Use: new_list = l.copy()
        -------------------------------------------------------
        Returns:
            new_list - a copy of self (Sorted_List)
        -------------------------------------------------------
        """

        # your code here

        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        At finish, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """

        # your code here

        return

    def _linear_search_r(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper methods - used only by other ADT methods.
        (recursive version)
        Use: p, c, i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_SL_Node)
            current - pointer to the node containing key (_SL_Node)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """

        # your code here

        return

    def clean_r(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the sorted list.
        Use: sl.clean_r()
        -------------------------------------------------------
        Returns:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """

        # your code here

        return

    def identical_r(self, rs):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. (recursive version)
        Use: b = l.identical_r(rs)
        -------------------------------------------------------
        Parameters:
            rs - another list (Sorted_List)
        Returns:
            identical - True if this list contains the same values as rs
                in the same order, otherwise False.
        -------------------------------------------------------
        """

        # your code here

        return

    def intersection_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        (recursive algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """

        # your code here

        return

    def copy_r(self):
        """
        -----------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (recursive verstion)
        Use: new_list = l.copy()
        -----------------------------------------------------------
        Returns:
            new_list - a copy of self (Sorted_List)
        -----------------------------------------------------------
        """

        # your code here

        return

    def combine_r(self, rs):
        """
        -------------------------------------------------------
        Combines contents of two lists into a third.
        Use: new_list = l1.combine(rs)
        -------------------------------------------------------
        Parameters:
            rs- an linked-based List (Sorted_List)
        Returns:
            new_list - the contents of the current Sorted_List and rs
            are interlaced into new_list - current Sorted_List and rs
            are empty (Sorted_List)
        -------------------------------------------------------
        """

        # your code here

        return

    def union_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        (recursive algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """

        # your code here

        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
