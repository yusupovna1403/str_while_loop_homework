def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    sum = 0
    while i < len(s):
        if s[i].isalpha():
            sum+=1
        i+=1
    return sum

print(main("python 2022"))
print(main("yusupovna1403"))
