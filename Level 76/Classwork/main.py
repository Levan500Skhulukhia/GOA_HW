def find_missing(sequence):
    n = len(sequence) + 1
    total_sum = (n * (sequence[0] + sequence[-1])) // 2
    given_sum = sum(sequence)
    return total_sum - given_sum
