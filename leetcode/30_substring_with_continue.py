from collections import deque

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        wl = len(words[0])
        wc = len(words)
        uniq_wc = len(set(words))
        indices = []
        # print(uniq_wc)

        for start in xrange(wl):
            # initial settings for each round
            count_dict = dict()
            for word in words:
                try:
                    count_dict[word] -= 1
                except KeyError:
                    count_dict[word] = -1
            word_que = deque()
            total_words = 0

            for i in xrange(start, len(s), wl):
                new_word = s[i:i+wl]
                word_que.append(new_word)
                try:
                    count_dict[new_word] += 1
                    if count_dict[new_word] == 0:
                        total_words += 1
                except KeyError:
                    pass

                old_word = None
                if len(word_que) > wc:
                    old_word = word_que.popleft()
                    try:
                        if count_dict[old_word] == 0:
                            total_words -= 1
                        count_dict[old_word] -= 1

                    except KeyError:
                        pass

                if total_words == uniq_wc:
                    # print('append', i)
                    indices.append(i - (wc-1) * wl)
                # print(i, wl, new_word, old_word, total_words, count_dict)

        return sorted(indices)
