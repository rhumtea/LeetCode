class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for elem in asteroids:
            while stack and elem < 0 < stack[-1]:
                if stack[-1] < -elem:
                    stack.pop()
                    continue
                elif stack[-1] == -elem:
                    stack.pop()
                break
            else:
                stack.append(elem)
        return stack