

def sum_even(A):
    total = 0

    for i in range(len(A)):
        if A[i] % 2 == 0:
            total += A[i]

    return total


A = [1, 4, 7, 2, 6, 9]
print(sum_even(A))
