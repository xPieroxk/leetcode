# Keyboard Row

Given an array of strings `words`, return the words that can be typed using letters of the alphabet on only **one row** of the American keyboard (as shown below).

Note that the strings are **case-insensitive** — both lowercase and uppercase versions of a letter are treated as if they belong to the same keyboard row.

### American Keyboard Rows:

- **First row**: `"qwertyuiop"`
- **Second row**: `"asdfghjkl"`
- **Third row**: `"zxcvbnm"`

---

### Example 1:

**Input:**  
`words = ["Hello","Alaska","Dad","Peace"]`  
**Output:**  
`["Alaska","Dad"]`

**Explanation:**  
"Alaska" and "Dad" use only characters from the second row of the keyboard.

---

### Example 2:

**Input:**  
`words = ["omk"]`  
**Output:**  
`[]`

---

### Example 3:

**Input:**  
`words = ["adsdf","sfd"]`  
**Output:**  
`["adsdf","sfd"]`

---

### Constraints:

- `1 <= words.length <= 20`
- `1 <= words[i].length <= 100`
- `words[i]` consists of **English letters** (both lowercase and uppercase).