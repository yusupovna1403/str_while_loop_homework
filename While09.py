def main(s):
    """
    A string of numbers is given. Find the sum of all the digits and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    sum = 0
    while i < len(s):
        if s[i] >= '0' and s[i] <= '9':
                sum+=int(s[i])
        i+=1
    return sum
print(main('python 20221178'))