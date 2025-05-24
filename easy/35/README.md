## Search Insert Position

Given a **sorted** array of **distinct** integers `nums` and an integer `target`, return **the index of `target`** if it is present.  
If `target` is **not** in `nums`, return **the index where it would be if it were inserted in order**.

You must design an algorithm with **`O(log n)` runtime complexity**.

---

### Examples

| # | Input | Output |
|---|-------|--------|
| 1 | `nums = [1, 3, 5, 6]`, `target = 5` | `2` |
| 2 | `nums = [1, 3, 5, 6]`, `target = 2` | `1` |
| 3 | `nums = [1, 3, 5, 6]`, `target = 7` | `4` |

---

### Constraints

* `1 ≤ nums.length ≤ 10⁴`
* `−10⁴ ≤ nums[i] ≤ 10⁴`
* All `nums[i]` are **distinct** and `nums` is sorted in **ascending** order.
* `−10⁴ ≤ target ≤ 10⁴`