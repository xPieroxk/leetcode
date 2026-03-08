class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for s in strs:
            encoded.append(str(len(s)))
            encoded.append("#")
            encoded.append(s)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])

            start = j + 1
            end = start + length

            decoded.append(s[start:end])

            i = end
        return decoded
