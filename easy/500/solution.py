class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        firstRow = set('qwertyuiop')
        secondRow = set('asdfghjkl')
        thirdRow = set('zxcvbnm')
        rows = [firstRow, secondRow, thirdRow]
        for w in words:
            if any(set(w.lower()) <= row for row in rows):
                ans.append(w)
        return ans
