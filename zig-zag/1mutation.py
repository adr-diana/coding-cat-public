def zig_zag(s):
    '''
    Missing return statement here
    '''
    s = list(s)  # Convert string to list for pop operations
    result = ""
    for i in range(len(s)):
        if i % 2 == 0:  # Even index
            result += s.pop(0)  # Remove from the beginning
        else:  # Odd index
            result += s.pop(-1)  # Remove from the end
