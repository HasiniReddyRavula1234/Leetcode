class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        s = 0
        for ch in operations:
            if ch == 'C':
                stack.pop()
            elif ch == 'D':
                top = stack[-1]
                stack.append(top * 2)
            elif ch == '+':
                s = stack[-1] + stack[-2]
                stack.append(s)
            else:
                stack.append(int(ch))
        return sum(stack)

