def is_valid_IP(strng):
    octets = strng.split(".")
    if len(octets) != 4:
        return False
    for octet in octets:
        if not octet.isdigit():
            return False
        if octet != "0" and octet.startswith("0"):
            return False
        if not (0 <= int(octet) <= 255):
            return False
    return True





def shortest_steps_to_num(num):
    steps = 0
    while num > 1:
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1
        steps += 1
    return steps
