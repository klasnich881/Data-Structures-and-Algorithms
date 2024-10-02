"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Nicholas Klassen
ID:      169062164
Email:   klas2164@mylaurier.ca
__updated__ = "2024-02-02"
-------------------------------------------------------
"""
# Imports
from List_array import List
# Constants


def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for i in source:
        llist.append(i)
    source.clear()
    return


def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not llist.is_empty():
        item = llist.remove(llist[0])
        target.append(item)

    return


def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    # Test find on empty list
    value = source.find(42)
    print_result("find on an empty list", value is None)

    # Test count on empty list
    count = source.count(42)
    print_result("count on an empty list", count == 0)

    # Test max on empty list
    print_exception_result("max on an empty list",
                           source.max(), AssertionError)

    # Test min on empty list
    print_exception_result("min on an empty list",
                           source.min(), AssertionError)

    # Test insert on empty list
    source.insert(0, 42)
    print_result("insert on an empty list", source[0] == 42)

    # Test append on a empty list
    source.append(99)
    print_result("append on an empty list", source[1] == 99)

    # Test remove on empty list
    value = source.remove(99)
    print_result("remove on an empty list", value is None)

    # add data to list
    data = [10, 20, 30, 40, 50]
    for val in data:
        source.append(val)

        # Test is_empty on a non-empty
        print_result("is_empty on a non-empty list", not source.is_empty())

        # Test index for existing elements
        for i, val in enumerate(data):
            print_result(f"index({val}) returns {i}", source.index(val) == i)

        # Test index for a non-existing elem
        non_existing_value = 999
        print_result(f"index({non_existing_value}) returns -1 for a non-existing element",
                     source.index(non_existing_value) == -1)

    # Test is_empty on empty list
    empty_list = List()  # Make empty list
    print_result("is_empty on an empty list", empty_list.is_empty())


def print_result(test_description, result):
    """
    Prints the result of a test.
    """
    status = "Passed" if result else "Failed"
    print(f"{status}: {test_description}")


def print_exception_result(test_description, func_result, exception_type):
    """
    Prints the result of a test for an expected exception.
    """
    try:
        func_result()
        print(f"Failed: {test_description} should raise {exception_type}")
    except exception_type:
        print(f"Passed: {test_description}")
