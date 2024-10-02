"""
-------------------------------------------------------
Linked version of the list ADT.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2024-03-03"
-------------------------------------------------------
"""
from copy import deepcopy


class _List_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a list node that contains a copy of value
        and a link to the next node in the list.
        Use: node = _List_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value for node (?)
            next_ - another list node (_List_Node)
        Returns:
            a new _List_Node object (_List_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_


class List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: lst = List()
        -------------------------------------------------------
        Returns:
            a new List object (List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two Lists are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a list (List)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        equals = True
        if self._count != len(target):
            equals = False

        current_self = self._front
        current_target = target._front

        while current_self is not None:
            if current_self._value != current_target._value:
                equals = False
            current_self = current_self._next
            current_target = current_target._next

        return equals

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        _, current, _ = self._linear_search(key)

        return current is not None

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
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        c1 = source1._front
        c2 = source2._front

        while c1 is not None or c2 is not None:
            if c1 is not None:
                self._interlace(c1)
                c1 = c1._next
            if c2 is not None:
                self._interlace(c2)
                c2 = c2._next
        source1._front = source1._rear = None
        source2._front = source2._rear = None
        source1._count = source2._count = 0

        return

    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
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

        self._front = None
        self._rear = None
        self._count = 0

        seen_values = set()

        c1 = source1._front
        while c1 is not None:
            seen_values.add(c1._value)
            c1 = c1._next

        c2 = source2._front
        while c2 is not None:
            if c2._value in seen_values and not self.__contains__(c2._value):
                self._interlace(c2)

            c2 = c2._next
        return

    def _interlace(self, node):
        """
        Inserts a copy of the given node at the end of the current list.
        ---------------------------------------------------
        Returns:
            None
        """
        new_node = _List_Node(node._value, None)
        if self._rear is None:
            self._front = new_node
        else:
            self._rear._next = new_node
        self._rear = new_node
        self._count += 1

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
        target1 = List()
        target2 = List()

        current = self._front
        count = 0

        while current is not None:
            # Append the current node to target1 or target2 based on count
            if count % 2 == 0:
                if target1._rear is None:
                    target1._front = target1._rear = _List_Node(
                        current._value, None)
                else:
                    target1._rear._next = _List_Node(current._value, None)
                    target1._rear = target1._rear._next
            else:
                if target2._rear is None:
                    target2._front = target2._rear = _List_Node(
                        current._value, None)
                else:
                    target2._rear._next = _List_Node(current._value, None)
                    target2._rear = target2._rear._next

            current = current._next
            count += 1

        # Ensure the rear pointers are set to None for empty lists
        if target1._front is None:
            target1._rear = None
        if target2._front is None:
            target2._rear = None

        # Set self attributes to empty state
        self._front = self._rear = None
        self._count = 0

        return target1, target2

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source list into separate target lists with values 
        alternating into the targets. At finish source self is empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (List)
            target2 - contains other alternating values from source (List)
        -------------------------------------------------------
        """
        # your code here
        target1 = List()
        target2 = List()

        current = self._front
        count = 0

        while current is not None:
            if count % 2 == 0:
                target1._interlace(current)
            else:
                target2._interlace(current)

            current = current._next
            count += 1

        # Set self attributes to empty state
        self._front = self._rear = None
        self._count = 0

        return target1, target2

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = lst.is_empty()
        -------------------------------------------------------
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(lst)
        -------------------------------------------------------
        Returns:
            the number of values in the list.
        -------------------------------------------------------
        """
        return self._count

    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source List to the rear
        of the current List. Private helper method.
        Use: self._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            source - a non-empty linked List (List)
        Returns:
            The current List contains the old front of the source List and
            its count is updated. The source List front and count are updated.
        -------------------------------------------------------
        """
        assert source._front is not None, \
            "Cannot move the front of an empty List"

        node = source._front
        source._count -= 1
        source._front = source._front._next

        if self._rear is None:
            self._front = node
        else:
            self._rear._next = node

        node._next = None
        self._rear = node
        self._count += 1
        # Update source list's rear to None if it becomes empty
        if source._front is None:
            source._rear = None

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
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        seen_values = set()

        # Traverse source1 and insert unique values into the current list
        current1 = source1._front
        while current1 is not None:
            if current1._value not in seen_values:
                self._interlace(current1)
                seen_values.add(current1._value)
            current1 = current1._next

        # Traverse source2 and insert unique values into the current list
        current2 = source2._front
        while current2 is not None:
            if current2._value not in seen_values:
                self._interlace(current2)
                seen_values.add(current2._value)
            current2 = current2._next

        return

    def prepend(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the front of the List.
        Use: lst.prepend(value)
        -------------------------------------------------------
        Parameters:
            value - a data element. (?)
        Returns:
            None
        -------------------------------------------------------
        """
        new_node = _List_Node(value, self._front)
        self._front = new_node
        if self._rear is None:
            self._rear = new_node
        self._count += 1

    def append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the end of the List.
        Use: lst.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        new_node = _List_Node(value, None)
        if self._rear is None:
            self._front = new_node
        else:
            self._rear._next = new_node
        self._rear = new_node
        self._count += 1

    def insert(self, i, value):
        """
        -------------------------------------------------------
        A copy of value is added to index i, following values are pushed right.
        If i outside of range of -len(list) to len(list) - 1, the value is 
        prepended or appended as appropriate.
        Use: lst.insert(i, value)
        -------------------------------------------------------
        Parameters:
            i - index value (int)
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        if i < 0:
            i = self._count + i
        if i < 0:
            i = 0
        elif i > self._count:
            i = self._count

        if i == 0:
            self.prepend(value)
        elif i == self._count:
            self.append(value)
        else:
            current = self._front
            for _ in range(i - 1):
                current = current._next
            new_node = _List_Node(value, current._next)
            current._next = new_node
            self._count += 1

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in list.
        Private helper method.
        (iterative algorithm)
        Use: previous, current, index = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key, -1 if key is not found (int)
        -------------------------------------------------------
        """
        previous = None
        current = self._front
        index = 0

        while current is not None and current._value != key:
            previous = current
            current = current._next
            index += 1

        if current is None:
            index = -1

        return previous, current, index

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the first value in list that matches key.
        Use: value = lst.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        previous, current, index = self._linear_search(key)

        if index == -1:
            value = None
        else:
            value = current._value
            if previous is None:
                self._front = current._next
                if self._front is None:
                    self._rear = None
            else:
                previous._next = current._next
                if previous._next is None:
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
        self._count -= 1

        if self._front is None:
            self._rear = None

        return value

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: lst.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        while self._linear_search(key)[2] != -1:
            self.remove(key)

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of the first value in list that matches key.
        Use: value = lst.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        _, current, _ = self._linear_search(key)
        if current is not None:
            value = deepcopy(current._value)
        else:
            value = None
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = lst.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty list"
        return deepcopy(self._front._value)

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = lst.index(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            i - index value of key in the list, -1 if key not found (int)
        -------------------------------------------------------
        """
        _, _, index = self._linear_search(key)
        return index

    def _is_valid_index(self, i):
        """
        ---------------------------------------------------------
        Determines whether an index is valid for the current list.
        Use: b = lst._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if the index is valid, False otherwise (boolean)
        -------------------------------------------------------
        """
        n = self._count
        return -n <= i < n

    def __getitem__(self, i):
        """
        -------------------------------------------------------
        Returns a copy of the i-th value in the list.
        Use: value = lst[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - a copy of the i-th value in the list (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"
        if i < 0:
            i = self._count + i
        current = self._front
        for _ in range(i):
            current = current._next
        return deepcopy(current._value)

    def __setitem__(self, i, value):
        """
        -------------------------------------------------------
        The i-th element of the list contains a copy of value.
        Use: lst[i] = value
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"
        if i < 0:
            i = self._count + i
        current = self._front
        for _ in range(i):
            current = current._next
        current._value = deepcopy(value)

        return

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in the list.
        Use: value = lst.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"
        max_data = self._front._value
        current = self._front._next
        while current is not None:
            if current._value > max_data:
                max_data = current._value
            current = current._next
        return deepcopy(max_data)

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in the list.
        Use: value = lst.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find minimum of an empty list"
        min_data = self._front._value
        current = self._front._next
        while current is not None:
            if current._value < min_data:
                min_data = current._value
            current = current._next
        return deepcopy(min_data)

    def count(self, key):
        """
        -------------------------------------------------------
        Counts the number of times key appears in list.
        Use: n = lst.count(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            number - the number of times key appears in list (int)
        -------------------------------------------------------
        """
        count = 0
        current = self._front
        while current is not None:
            if current._value == key:
                count += 1
            current = current._next
        return count

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        Use: lst.reverse()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        previous = None
        current = self._front
        while current is not None:
            next_node = current._next
            current._next = previous
            previous = current
            current = next_node
        self._front = previous

    def reverse_r(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list using recursion.
        Use: lst.reverse_r()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        def _reverse_r(node):
            if node is None or node._next is None:
                self._front = node
            else:
                next_node = _reverse_r(node._next)
                next_node._next, node._next = node, None

            return node

        # Call the helper function and update _rear
        self._rear = _reverse_r(self._front)
        self._rear._next = None

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the sorted list.
        Use: lst.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        values_set = set()
        previous = None
        current = self._front
        while current is not None:
            if current._value in values_set:
                previous._next = current._next
                if previous._next is None:
                    self._rear = previous
                self._count -= 1
            else:
                values_set.add(current._value)
                previous = current
            current = current._next

        return

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the last value in list.
        Use: value = lst.pop()
        -------------------------------------------------------
        Returns:
            value - the last value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        previous = None
        current = self._front

        if len(args) == 1:
            if args[0] < 0:
                n = self._count + args[0]
            else:
                n = args[0]
            j = 0

            while j < n:
                previous = current
                current = current._next
                j += 1
        else:
            j = 0

            while j < (self._count - 1):
                previous = current
                current = current._next
                j += 1

        value = current._value
        self._count -= 1

        if previous is None:
            self._front = self._front._next
            if self._front is None:
                self._rear = None
        else:
            previous._next = current._next
            if previous._next is None:
                self._rear = previous

        return value

    def __str__(self):
        """
        -------------------------------------------------------
        Generates a formatted string of list contents.
        Use: print(lst)
        Use: s = str(lst)
        -------------------------------------------------------
        Returns:
            string - a formatted string of list contents (str)
        -------------------------------------------------------
        """
        current = self._front
        string_list = []

        while current is not None:
            string_list.append(str(current._value))
            current = current._next

        return '[' + ', '.join(string_list) + ']'
