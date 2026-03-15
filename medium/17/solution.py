class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dig_to_let = {"2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]}
        ans =[]
        def bt(i,curr):
            if i== len(digits):
                ans.append("".join(curr))
                return
            for l in dig_to_let[digits[i]]:
                curr.append(l)
                bt(i+1,curr)
                curr.pop()

        bt(0,[])
        return ans