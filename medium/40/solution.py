class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def bt(i,curr,curr_sum):
            if curr_sum ==target:
                ans.append(curr[:])
                return
            if i>=len(candidates) or curr_sum > target:
                return

            curr.append(candidates[i])
            bt(i+1,curr,curr_sum+candidates[i])

            curr.pop()
            i+=1
            while i<len(candidates) and candidates[i]==candidates[i-1]:
                i+=1

            bt(i,curr,curr_sum)

        bt(0,[],0)
        return ans
