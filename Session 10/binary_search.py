def binary_search(my_list, x):
    '''
    this function adopts bisection/binary search to find the index of a given
    number in an ordered list
    my_list: an ordered list of numbers from smallest to largest
    x: a number
    returns the index of x if x is in my_list, None if not.
    '''
    first = 0
    last = len(my_list) - 1

    while first <= last:
        mid = (first + last) / 2

        if my_list[mid] == x:
            return x=x, mid=mid
        elif my_list[mid] > x:
            last = mid - 1
        elif my_list[mid] < x:
            first = mid + 1
        else:
            return x = x        


test_list = [1, 3, 5, 235425423, 23, 6, 0, -23, 6434]
test_list.sort()

print(binary_search(test_list, -23))
print(binary_search(test_list, 0))
print(binary_search(test_list, 235425423))
print(binary_search(test_list, 30))

# expected output
# 0
# 1
# 8
# None