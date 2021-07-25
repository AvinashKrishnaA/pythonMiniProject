def binary_search(lst, n):
    lst.sort()
    first = 0
    last = len(lst) - 1
    mid = (first + last) // 2
    while first <= last:
        mid = (first + last) // 2
        if lst[mid] == n:
            print(f"found at location {mid}")
            return True
        else:
            if n < lst[mid]:
                last = mid - 1
            else:
                first = mid + 1
    print("Not found")
    return False


if __name__ == "__main__":
    print("Enter numbers of list with spaces:")
    l1 = list(map(int, input().split()))
    x = int(input("Enter number to search:"))
    print(binary_search(l1, x))
