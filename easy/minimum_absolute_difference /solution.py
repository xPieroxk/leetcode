class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        result = []
        min_abs_diff = float('inf')
        arr.sort()
        for i in range(1, len(arr)):
            current_abs_diff = arr[i] - arr[i - 1]
            if current_abs_diff < min_abs_diff:
                min_abs_diff = current_abs_diff
                result = [[arr[i - 1], arr[i]]]
            elif current_abs_diff == min_abs_diff:
                result.append([arr[i - 1], arr[i]])

        return result
