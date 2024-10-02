"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Nicholas Klassen
ID:      169062164
Email:   klas2164@mylaurier.ca
__updated__ = "2024-01-26"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
# Constants


def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for item in source:
        queue.insert(item)

    source.clear()


def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not queue.is_empty():
        a = queue.remove()
        target.append(a)


def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
  Tests the methods of Queue are tested for both empty and
  non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()

    # tests for the queue methods go here

    # Empty

    first_empty = f"Check Empty: {q.is_empty()}"  # Return true
    first_rem = f'Check Remove: {q.remove()} '  # Error
    first_peek = f'Check Peek: {q.peek()}'  # Error
    for i in a:
        q.insert(i)
    print("Items in Queue")
    for i in q:
        print(i)

    # Non_empty
    sec_empty = f'Check Empty: {q.is_empty()}'
    sec_remove = f'Check Remove: {q.remove()}'
    sec_peek = f'Check Peek: {q.peek()}'
    # print the results of the method calls and verify by hand
    print("Empty Queue Tests:")
    print(first_empty)
    print(first_rem)
    print(first_peek)
    print("\nNon-Empty Queue Tests:")
    print(sec_empty)
    print(sec_remove)
    print(sec_peek)

    return


def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while source:
        pq.insert(source.pop(0))
    return


def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not pq.is_empty():
        a = pq.remove()
        target.append(a)
    return


def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()
    print("Testing is_empty() on an empty priority queue:", pq.is_empty())  # True

    for value in a:
        pq.insert(value)
        print(
            f"Inserted {value}, is_empty: {pq.is_empty()}, peek: {pq.peek()}")

    print("Testing is_empty() on a non-empty priority queue:",
          pq.is_empty())  # False

    print("Testing peek() on a non-empty priority queue:",
          pq.peek())  # Should show the highest priority value

    while not pq.is_empty():
        value = pq.remove()
        print(f"Removed {value}, is_empty: {pq.is_empty()}, peek: {pq.peek()}")

    print("Testing is_empty() on an empty priority queue after removals:",
          pq.is_empty())  # True
    return
