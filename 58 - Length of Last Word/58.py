class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_list = s.split(" ")
        # Get last non-whitespace item in list
        last_word = [i for i in word_list if i][-1]
        return len(last_word)