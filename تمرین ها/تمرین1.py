

def find_min(A):
    if len(A) == 0:
        raise ValueError("  خالی نباشد")

    minimum = A[0]

    for i in range(1, len(A)):
        if A[i] < minimum:
            minimum = A[i]

    return minimum


A = [7, 3, 9, 2, 5]
print(find_min(A))
