

# جست‌وجوی خطی
def linear_search(A, x):
    for i in range(len(A)):
        if A[i] == x:
            return i
    return -1


# جست‌وجوی دودویی
def binary_search(A, x):
    left = 0
    right = len(A) - 1

    while left <= right:
        mid = (left + right) // 2

        if A[mid] == x:
            return mid
        elif A[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1


#   جست وجو
A = [10, 20, 30, 40, 50, 60, 70]
x = 50

print("Linear Search:", linear_search(A, x))
print("Binary Search:", binary_search(A, x))
