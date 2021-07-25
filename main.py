"""This module contains Binary search function execution """


def binary_search(lst, numb):
    """ This function takes two parameters
    1. list of numbers in which number should be searched
    2. number to be searched
    This function returns a bool"""
    lst.sort()
    first = 0
    last = len(lst) - 1
    mid = (first + last) // 2
    result = False
    while first <= last:
        mid = (first + last) // 2
        if lst[mid] == numb:
            print(f"found at location {mid}")
            result = True
        else:
            if numb < lst[mid]:
                last = mid - 1
            else:
                first = mid + 1
    print("Not found")
    if result:
        return True
    return False


if __name__ == "__main__":
    print("Enter numbers of list with spaces:")
    l1 = list(map(int, input().split()))
    x = int(input("Enter number to search:"))
    print(binary_search(l1, x))
