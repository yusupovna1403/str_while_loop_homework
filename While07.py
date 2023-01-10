def main(s):
    """
    A string of numbers is given. Find how many even digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    count = 0
    while i < len(s):
        if s[i] >= '0' and s[i] <= '9':
            if int(s[i]) % 2 == 0:
                count+=1
        i+=1
    return count
print(main('python 20221178'))