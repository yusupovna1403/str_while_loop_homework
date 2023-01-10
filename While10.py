def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd digits.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    count = 0
    while i < len(s):
        if s[i] >= '0' and s[i] <= '9':
            if int(s[i]) % 2 == 1:
                count+=int(s[i])
        
        i+=1
    return count
print(main('python 20221178'))