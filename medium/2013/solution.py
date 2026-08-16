from collections import defaultdict


class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        self.points[point] += 1

    def count(self, point: List[int]) -> int:
        dx, dy = point[0], point[1]
        res = 0
        for (x, y), freq in self.points.items():
            p1, p2 = (x, dy), (dx, y)
            same_point = dx == x and y == dy
            is_diagonal = abs(x - dx) == abs(y - dy)
            if not is_diagonal or same_point or p1 not in self.points or p2 not in self.points:
                continue
            res += freq * self.points[p1] * self.points[p2]
        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)