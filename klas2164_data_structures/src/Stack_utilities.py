"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Nicholas Klassen
ID:      169062164
Email:   klas2164@mylaurier.ca
__updated__ = "2024-01-19"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
# Constants
#s = Stack()


def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for i in range(len(source)-1, -1, -1):
        stack.push(source[i])
    source.clear()
    return None


def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while not stack.is_empty():
        value = stack.pop()
        target.insert(0, value)

    return None


def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    # Empty Stack:
    stack = Stack()
    # Test is_empty on an empty stack
    print("Is Empty", stack.is_empty())

    # Testing on empty stacks
    empty_pop = stack.pop()
    print("Empty pop:", empty_pop)

    print("Empty peek: ", stack.peek())

    # Push element on stack
    for item in source:
        stack.push(item)

    # Test empty on a non-empty stack
    print("Is Empty?", stack.is_empty())  # Expect false

    # Test Peek on a non-empty stack
    print("Peek: ", stack.peek())

    # Test pop on a non-empty stack
    pop_val = stack.pop()
    print("Pop: ", pop_val)
