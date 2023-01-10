import string
def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    count = 0
    while i < len(s):
        if s[i] in string.punctuation:
            count+=1
        i+=1
    return count
print(main("#hashtag@$"))