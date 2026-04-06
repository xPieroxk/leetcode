class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            self.time_map[key].append((value, timestamp))
        else:
            self.time_map[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        if key not in self.time_map:
            return ans

        values = self.time_map[key]
        l, r = 0, len(values) - 1
        while l <= r:
            m = (r + l) // 2
            v, t = values[m]
            if t <= timestamp:
                l = m + 1
                ans = v
            else:
                r = m - 1

        return ans

