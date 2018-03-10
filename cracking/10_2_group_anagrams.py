def anagram_hash(s):
    return sorted(s)

def group_anagrams(strings):
    return sorted(strings, key=anagram_hash)

print(group_anagrams(['abc', 'xx', 'yb', 'bac', 'xx', 'by', 'c']))
