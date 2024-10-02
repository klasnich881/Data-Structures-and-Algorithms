"""
-------------------------------------------------------
Linked version of the Queue ADT.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2024-02-18"
-------------------------------------------------------
"""
from copy import deepcopy


class _Queue_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a queue node that contains a copy of value
        and a link to the next node in the queue.
        Use: node = _Queue_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value for node (?)
            next_ - another Queue node (_Queue_Node)
        Returns:
            a new _Queue_Node object (_Queue_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_


class Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a Python list.
        Use: queue = Queue()
        -------------------------------------------------------
        Returns:
            a new Queue object (Queue)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: b = queue.is_empty()
        -------------------------------------------------------
        Returns:
            True if queue is empty, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        return self._count == 0

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the queue is full.
        Use: b = queue.is_full()
        -------------------------------------------------------
        Returns:
            True if queue is full, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        return False

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(queue)
        -------------------------------------------------------
        Returns:
            the number of values in queue.
        -------------------------------------------------------
        """
        # your code here
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the rear of queue.
        Use: queue.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        node = _Queue_Node(value, None)
        if self.is_empty():
            self._front = node
        else:
            self._rear._next = node
        self._rear = node
        self._count += 1

        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: value = queue.remove()
        -------------------------------------------------------
        Returns:
            value - the value at the front of the queue - the value is
            removed from queue (?)
        -------------------------------------------------------        
        """
        assert self._front is not None, "Cannot remove from an empty queue"

        # Retrieve val from front of node
        value = self._front._value
        # Move pointer to next node
        self._front = self._front._next
        # Decrease count
        self._count -= 1
        # Update empty status
        if self.is_empty():
            self._rear = None

        return deepcopy(value)

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: value = queue.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of queue -
            the value is not removed from queue (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty queue"
        if not self.is_empty():
            value = deepcopy(self._front._value)
        else:
            raise Exception("Cannot peek at an empty queue")
        # your code here
        return value

    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source queue to the rear of the target queue.
        The target queue contains the old front node of the source queue.
        The source queue front is updated.
        Use: target._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            source - a linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot move the front of an empty queue"

        # your code here
        front_node = source._front
        source._front = front_node._next

        # Insert retrieved node at rear of target queue
        if self._front is None:
            self._front = front_node
        else:
            self._rear._next = front_node

        self._rear = front_node
        front_node._next = None

        self._count += 1

        # Update rear if source is now empty
        if source.is_empty():
            source._rear = None

        self._count -= 1
        return

    def _append_queue(self, source):
        """
        -------------------------------------------------------
        Appends the entire source queue to the rear of the target queue.
        The source queue becomes empty.
        Use: target._append_queue(source)
        -------------------------------------------------------
        Parameters:
            source - an linked-based queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot append an empty queue"
        # Update the rear of the target queue to point to the front of the source queue
        if self.is_empty():
            self._front = source._front
        else:
            self._rear._next = source._front

        # Update the rear of the target queue to be the rear of the source queue
        self._rear = source._rear

        # Update the count of the target queue by adding the count of the source queue
        self._count += source._count

        # Empty the source queue by setting its front and rear to None
        source._front = None
        source._rear = None

        # Reset the count of the source queue to 0
        source._count = 0
        # your code here
        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source queues into the current target queue.
        When finished, the contents of source1 and source2 are interlaced
        into target and source1 and source2 are empty.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked queue (Queue)
            source2 - a linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        while not source1.is_empty() and not source2.is_empty():
            # Move front element from source1 to target
            if not source1.is_empty():
                self._move_front_to_rear(source1)

            # Move front element from source2 to target
            if not source2.is_empty():
                self._move_front_to_rear(source2)

        # If source1 is not empty, append the remaining elements
        if not source1.is_empty():
            self._append_queue(source1)

        # If source2 is not empty, append the remaining elements
        if not source2.is_empty():
            self._append_queue(source2)

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source queue into separate target queues with values 
        alternating into the targets. At finish source queue is empty.
        (iterative algorithm)
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Queue)
            target2 - contains other alternating values from source (Queue)
        -------------------------------------------------------
        """
        # your code here
        target1 = Queue()
        target2 = Queue()
        toggle = True

        while self._front is not None:
            # Move front element from source to target1 if toggle is True
            if toggle:
                target1._move_front_to_rear(self)
                target1._count += 1
            # Move front element from source to target2 if toggle is False
            else:
                target2._move_front_to_rear(self)
                target2._count += 1

            # Toggle the value of the toggle variable
            toggle = not toggle
        self._count = 0
        self._rear = None
        return target1, target2

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two Queues are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a queue (Queue)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        # your code here
        equals = True
        # Check if the lengths of the queues are different
        if len(self) != len(target):
            equals = False

        # Iterate through both queues and compare corresponding elements
        current1 = self._front
        current2 = target._front

        while current1 is not None:
            # If values are not equal, return False
            if current1._value != current2._value:
                equals = False
                break

            # Move to the next node in both queues
            current1 = current1._next
            current2 = current2._next

        # If the loop completes, the queues are equal
        return equals

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in q:
        -------------------------------------------------------
        Returns:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
