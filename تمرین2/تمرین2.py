

def count_occurrences(A, x):
    count = 0

    for i in range(len(A)):
        if A[i] == x:
            count += 1

    return count


A = [2, 5, 2, 7, 2, 9]
x = 2

print(count_occurrences(A, x))
