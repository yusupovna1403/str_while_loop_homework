def main(s):
    """
    A variable of type str is given. Find how many digits it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    sum = 0
    while i < len(s):
        if s[i].isdigit():
            sum+=1
        i+=1
    return sum

print(main("1234"))

