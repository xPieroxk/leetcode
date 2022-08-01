import java.util.HashMap;
import java.util.stream.IntStream;

class Solution {
    
    // O(n) time and O(1) space
    public int lengthOfLongestSubstring(String s) {
        var characters = new HashMap<Character, Integer>();
        int left = 0, right = 0, maxLen = 0;
        while (right < s.length()) {
            var c = s.charAt(right);
            if (characters.containsKey(c)) {
                // remove all characters from the left to the repeated character
                IntStream.range(left, characters.get(c)).forEach(i -> characters.remove(s.charAt(i)));
                // update the left pointer
                left = characters.get(c) + 1;
            }
            characters.put(c, right);
            maxLen = Math.max(maxLen, right - left + 1);
            right++;
        }
        return maxLen;
    }
}
