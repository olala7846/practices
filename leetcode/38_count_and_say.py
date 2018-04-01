
def count_and_say(n):
    s = "1"
    for i in xrange(1, n):
        s = get_next(s)
    return s

def get_next(s):
    name = s[0]
    count = 1
    result = ""
    for i in xrange(1, len(s)):
        if s[i] == name:
            count += 1
        else:
            result += str(count)
            result += name
            name = s[i]
            count = 1
    result += str(count)
    result += name

    return result


assert count_and_say(1) == "1"
assert count_and_say(2) == "11"
assert count_and_say(3) == "21"
assert count_and_say(4) == "1211"
assert count_and_say(5) == "111221"
assert count_and_say(6) == "312211"
assert count_and_say(7) == "13112221"
print('All tests passed')
