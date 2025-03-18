def diamond(n):
    if n % 2 == 0 or n <= 0:
        return None

    result = []
    for i in range(n):
        stars = 2 * i + 1 if i <= n // 2 else 2 * (n - i - 1) + 1
        spaces = (n - stars) // 2
        result.append(" " * spaces + "*" * stars + "\n")

    return "".join(result)