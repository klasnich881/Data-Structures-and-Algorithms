"""
-------------------------------------------------------
Linked versions of various sorts. Implemented on linked Lists.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-04-04"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from math import log10, floor
from List_linked import List


class Sorts:
    """
    -------------------------------------------------------
    Defines a number of linked sort operations.
    Uses class attribute 'swaps' to determine how many times
    elements are swapped by the class.
    Use: print(Sorts.swaps)
    Use: Sorts.swaps = 0
    -------------------------------------------------------
    """
    swaps = 0  # Tracks swaps performed.

    # The Sorts

    @staticmethod
    def selection_sort(a):
        """
        -------------------------------------------------------
        Sorts a linked list using the Selection Sort algorithm.
        Finds maximum value each pass.
        Use: selection_sort(a)
        -------------------------------------------------------
        Parameters:
            a - a linked list of comparable elements (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # Split the list into the sorted (_front) and unsorted parts.
        unsorted = a._front
        a._front = None
        # Go through each node in the unsorted list and find the max value
        # node.
        while unsorted is not None:
            max_prev = None
            max_node = unsorted
            prev = unsorted
            curr = max_node._next

            while curr is not None:
                if curr._value > max_node._value:
                    max_prev = prev
                    max_node = curr
                prev = curr
                curr = curr._next
            # Remove the max node from the unsorted list.
            Sorts.swaps += 1

            if max_prev is None:
                unsorted = max_node._next
            else:
                max_prev._next = max_node._next
            # Move the next max node to the front of the sorted list.
            if a._front is None:
                a._rear = max_node
            max_node._next = a._front
            a._front = max_node
        return

    @staticmethod
    def bubble_sort(a):
        """
        -------------------------------------------------------
        Sorts a linked list using the Bubble Sort algorithm.
        Use: bubble_sort(a)
        -------------------------------------------------------
        Parameters:
            a - a linked list of comparable elements (?)
        Returns:
            None
        -------------------------------------------------------
        """
        done = False
        last = None

        while not done:
            # if no elements have been swapped, then the list is sorted
            done = True
            # Get the front of the list.
            prev = None
            curr = a._front
            swapped = a._front

            while curr is not last and curr._next is not None:

                if curr._value > curr._next._value:
                    # If you swapped you need another pass.
                    done = False
                    # The pair curr, curr._next is out of order.
                    Sorts.swaps += 1
                    a._swap(prev, curr)
                    # Keep track of last node swapped
                    swapped = curr
                    # curr is unchanged - update prev
                    if prev is None:
                        prev = a._front
                    else:
                        prev = prev._next
                else:
                    # Move to next node.
                    prev = curr
                    curr = curr._next
            last = swapped
        # done == True iff no pair of keys was swapped on the last pass.
        return

    @staticmethod
    def comb_sort(a):
        """
        -------------------------------------------------------
        Sorts an List using the Comb Sort algorithm.
        Use: comb_sort(a)
        -------------------------------------------------------
        Parameters:
          a - a linked list of comparable elements (?)
        Returns:
          None
        -------------------------------------------------------
        """
        n = len(a)

        if n > 0:
            gap = n
            done = False

            while gap > 1 or not done:
                done = True
                prev = None
                curr = a._front
                gap = int(gap / 1.3)

                if gap < 1:
                    gap = 1

                i = 0
                prev_far = curr
                far = curr._next
                # Move to the far node for comparison.
                while i < gap - 1 and far is not None:
                    prev_far = far
                    far = far._next
                    i += 1

                while curr is not None and far is not None:
                    if curr._value > far._value:
                        Sorts.swaps += 1
                        a._swap(prev, prev_far)
                        done = False
                    # Increment all nodes.
                    prev_far = far
                    far = far._next
                    prev = curr
                    curr = curr._next
        return

    @staticmethod
    def insertion_sort(a):
        """
        -------------------------------------------------------
        Sorts a linked list using the Insertion Sort algorithm.
        Use: insertion_sort(a)
        -------------------------------------------------------
        Parameters:
            a - a linked list of comparable elements (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # Split the list into the sorted (_front) and unsorted parts.
        unsorted = a._front
        a._front = None

        # Go through each key_node in the unsorted list and insert it into the
        # proper position in the sorted list.
        while unsorted is not None:
            # Isolate the first key_node of the unsorted list.
            key_node = unsorted
            unsorted = unsorted._next
            # Find the proper place for the new key_node in the sorted list.
            # (Very similar to Priority Queue insertion.)
            prev = None
            curr = a._front

            while curr is not None and curr._value < key_node._value:
                prev = curr
                curr = curr._next

            # Insert key_node into the proper place in the sorted list.
            Sorts.swaps += 1

            if prev is None:
                key_node._next = a._front
                a._front = key_node
            else:
                key_node._next = curr
                prev._next = key_node

            if key_node._next is None:
                # Update the _rear link.
                a._rear = key_node
        # if a._rear is not None:
        #     print(f"Rear: {a._rear._value}")
        return

    @staticmethod
    def merge_sort(a):
        if a._count >= 2:
            # Split the list only if there are at least two elements.
            # Generate the left and right lists.
            left, right = Sorts._merge_split(a)
            # Sort the left list.
            Sorts.merge_sort(left)
            # Sort the right list.
            Sorts.merge_sort(right)
            # Merge the left and right lists back into a.
            Sorts._merge(a, left, right)
        return

    @staticmethod
    def _merge_split(source):
        # Split the list by count.
        count = source._count // 2
        curr = source._front

        for _ in range(count - 1):
            curr = curr._next

        # Define the left list.
        left = List()
        left._front = source._front
        left._rear = curr
        left._count = count
        # Define the right list.
        right = List()
        right._front = curr._next
        right._rear = source._rear
        right._count = source._count - count
        # Break the link between the two lists.
        left._rear._next = None
        # Empty the source list.
        source.clear()
        return left, right

    @staticmethod
    def _merge(target, left, right):
        # Traverse left and right appending larger value to rear of target.
        while left._front is not None and right._front is not None:

            if left._front._value <= right._front._value:
                target._move_front_to_rear(left)
            else:
                target._move_front_to_rear(right)

        # Append the remaining list - O(1) operation.
        if left._front is not None:
            target._append_list(left)
        elif right._front is not None:
            target._append_list(right)
        return

    # Sort Utilities

    @staticmethod
    def to_array(a):
        """
        -------------------------------------------------------
        Copies list values to a Python list.
        Use: values = to_array(a)
        -------------------------------------------------------
        Parameters:
            a - a linked list of comparable elements (?)
        Returns:
            values - the contents of a in a Python list.= (list of ?)
        -------------------------------------------------------
        """
        values = []
        curr = a._front

        while curr is not None:
            values.append(curr._value)
            curr = curr._next
        return values

    @staticmethod
    def is_sorted(a):
        """
        -------------------------------------------------------
        Determines whether an array is sorted or not.
        Use: srtd = Sorts.is_sorted(a)
        -------------------------------------------------------
        Parameters:
            a - an array of comparable elements (?)
        Returns:
            srtd - True if contents of a are sorted,
                False otherwise (boolean)
       -------------------------------------------------------
        """
        srtd = True
        curr = a._front

        while srtd and curr is not None and \
                curr._next is not None:

            if curr._value <= curr._next._value:
                curr = curr._next
            else:
                srtd = False
        return srtd

    @staticmethod
    def bucket_sort(a):
        if len(a) > 0:
            # Find the largest value in a and set up a counting
            # array with a size of the value range.
            buckets = []
            for _ in range(a.max() + 1):
                buckets.append(List())

            while a._front is not None:
                # Move nodes to the appropriate bucket.
                v = a._front._value
                buckets[v]._move_front_to_rear(a)

            # Move nodes back to the original list in order.
            for bucket in buckets:
                if not bucket.is_empty():
                    a._append_list(bucket)
        return

    @staticmethod
    def pr(a):
        print(a._count, "-", [v for v in a], "-",
              a._front._value, "-", a._rear._value)
        return

    @staticmethod
    def quick_sort(a):
        if a._front is not None:
            # Partition the list into three with respect to pivot value.
            lesser, equals, greater = Sorts._partition(a)
            Sorts.quick_sort(lesser)
            Sorts.quick_sort(greater)
            # Put all three lists back together in order.
            if lesser._front is not None:
                a._append_list(lesser)
            # equals list contains at least the pivot value.
            a._append_list(equals)
            if greater._front is not None:
                a._append_list(greater)
        return
    @staticmethod
    def radix_sort(a):
        """
        -------------------------------------------------------
        Performs a base 10 radix sort.
        Use: Sorts.radix_sort(a)
        -------------------------------------------------------
        Parameters:
            a - an array of base 10 integers (list)
        Returns:
            None
        -------------------------------------------------------
        """
        # Find the maximum number of digits in the array.
        max_digits = 0
        for num in a:
            num_digits = int(log10(num)) + 1
            if num_digits > max_digits:
                max_digits = num_digits
    
        # Perform counting sort for each digit, starting from the least significant digit.
        for digit in range(max_digits):
            # Initialize count array for digits 0-9.
            count = [0] * 10
    
            # Count the occurrences of each digit at the current position.
            for num in a:
                digit_value = (num // 10 ** digit) % 10
                count[digit_value] += 1
    
            # Update count array to store cumulative counts.
            for i in range(1, 10):
                count[i] += count[i - 1]
    
            # Create a temporary array to store sorted elements.
            temp = [0] * len(a)
    
            # Build the sorted array based on the current digit.
            for num in reversed(a):
                digit_value = (num // 10 ** digit) % 10
                temp[count[digit_value] - 1] = num
                count[digit_value] -= 1
    
            # Copy the sorted array back to the original array.
            for i in range(len(a)):
                a[i] = temp[i]
        
        return
    
    @staticmethod
    def radix_sort(a):
        """
        Performs a base 10 radix sort on a linked list.
        Use: Sorts.radix_sort(a)
        """
        if a.is_empty():
            return
        
        # Find the maximum number of digits in the list.
        max_digits = Sorts._find_max_digits(a)

        # Perform counting sort for each digit, starting from the least significant digit.
        for digit in range(max_digits):
            Sorts._radix_sort_digit(a, digit)

    @staticmethod
    def _find_max_digits(a):
        max_digits = 0
        curr = a._front
        
        while curr is not None:
            num_digits = int(log10(curr._value)) + 1
            if num_digits > max_digits:
                max_digits = num_digits
            curr = curr._next
            
        return max_digits
    
    @staticmethod
    def _radix_sort_digit(a, digit):
        """
        Performs counting sort on the specified digit of the numbers in the linked list.
        """
        # Initialize count array for digits 0-9.
        count = [0] * 10
        temp = [None] * a._count
        divisor = 10 ** digit
        
        # Count the occurrences of each digit at the current position.
        curr = a._front
        while curr is not None:
            digit_value = (curr._value // divisor) % 10
            count[digit_value] += 1
            curr = curr._next

        # Update count array to store cumulative counts.
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the sorted list based on the current digit.
        curr = a._front
        while curr is not None:
            digit_value = (curr._value // divisor) % 10
            temp[count[digit_value] - 1] = curr._value
            count[digit_value] -= 1
            curr = curr._next

        # Copy the sorted list back to the original list.
        curr = a._front
        for i in range(a._count):
            curr._value = temp[i]
            curr = curr._next
    @staticmethod
    def _partition(source):
        lesser = List()
        greater = List()
        equals = List()
        # Move source front node to the equals list.
        equals._move_front_to_rear(source)
        pivot = equals._front

        while source._front is not None:
            # Process the remaining nodes with respect to the pivot node.
            if pivot._value > source._front._value:
                lesser._move_front_to_rear(source)
            elif pivot._value < source._front._value:
                greater._move_front_to_rear(source)
            else:
                equals._move_front_to_rear(source)
        return lesser, equals, greater
