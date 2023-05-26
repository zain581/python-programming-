from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = word_len * len(words)
        word_count = Counter(words)
        result = []

        for i in range(word_len):
            left = i
            sub_count = Counter()
            count = 0

            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]

                if word in word_count:
                    sub_count[word] += 1
                    count += 1

                    while sub_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        sub_count[left_word] -= 1
                        count -= 1
                        left += word_len

                    if count == len(words):
                        result.append(left)
                        left_word = s[left:left + word_len]
                        sub_count[left_word] -= 1
                        count -= 1
                        left += word_len
                else:
                    sub_count.clear()
                    count = 0
                    left = j + word_len

        return result
