def strstr(haystack, needle):
    if not needle:
        return 0

    # Implement Rabin Karp
    PRIME = 104743

    # calculate needle signature
    n_sig = 0
    n = len(needle)
    x = 1
    for c in needle:
        x = (x * 128) % PRIME
        n_sig *= 128
        n_sig += ord(c)
        n_sig %= PRIME

    h_sig = 0
    for i, c in enumerate(haystack):
        h_sig *= 128
        h_sig += ord(c)
        if (i-n) >= 0:
            h_sig -= x * ord(haystack[i-n])
        h_sig %= PRIME

        if h_sig == n_sig and i-n+1 >= 0 and haystack[i-n+1:i+1] == needle:
            return i-n+1


    return -1

assert strstr("hello", "ll") == 2
assert strstr("aaaaaa", "bba") == -1
assert strstr("hotdog", "dog") == 3
assert strstr("hotdog", "hot") == 0
assert strstr("hotdog", "") == 0
print('All test passed')
