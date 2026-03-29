class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(reverse=True)

        stack = []
        for p, s in cars:
            t = (target - p) / s
            if len(stack) < 1 or t > stack[-1]:
                stack.append(t)

        return len(stack)