def remove_duplicates_and_sort(numbers):
    """
    Takes a list of numbers and returns a sorted list with duplicates removed.
    """
    return sorted(set(numbers))


def cumulative_sum(numbers):
    """
    Takes a list of numbers and returns a new list where each element
    is the cumulative sum up to that index.
    """
    result = []
    total = 0

    for num in numbers:
        total += num
        result.append(total)

    return result


def every_nth_element(lst, n):
    """
    Returns every nth element from the list.
    """
    return lst[::n]


def dot_product(list1, list2):
    """
    Returns the dot product of two lists of equal length.
    """
    return sum(a * b for a, b in zip(list1, list2))


def matrix_multiply(A, B):
    """
    Multiplies two matrices A and B (2D lists).
    """
    # number of rows in A, columns in B
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    # result matrix filled with 0s
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result