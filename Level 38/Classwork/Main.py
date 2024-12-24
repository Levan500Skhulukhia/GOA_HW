def check_exam(arr1, arr2):
    result = 0
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            result += 4
        elif arr2[i] == "":
            result += 0
        else:
            result -= 1
    return max(result, 0)  # Ensure the result is not negative



def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def backwards_prime(start, end):
    result = []
    for num in range(start, end + 1):
        reversed_num = int(str(num)[::-1])
        if num != reversed_num and is_prime(num) and is_prime(reversed_num):
            result.append(num)
    return result
