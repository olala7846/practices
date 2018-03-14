
class TreeNode(object):
    def __init__(self, val, depth):
        self.val = val
        self.children = dict()
        self.depth = depth


def longest_common_prefix(words):
    longest_common_prefix = ''

    root = TreeNode(None, 0)
    for word in words:
        common_prefix = build_tree(root, word)
        if len(common_prefix) > len(longest_common_prefix):
            longest_common_prefix = common_prefix

    return longest_common_prefix


def build_tree(root, word):
    depth = 0
    current = root

    for c in word:
        try:
            current = current.children[c]
            depth = current.depth
        except KeyError:
            n = TreeNode(c, current.depth + 1)
            current.children[c] = n

    return word[:depth]


print longest_common_prefix(['abcd', 'abce', 'axy'])
assert longest_common_prefix(['abcd', 'abce', 'axy']) == 'abc'
