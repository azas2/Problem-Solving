class Solution:
    def minSwaps(self, s: str) -> int:
        stack=deque()
        unbalanced=0
        for char in s:
            if char=='[':
                stack.append(char)
            else:
                if stack:
                    stack.pop()
                else:
                    unbalanced += 1
        return (unbalanced+1)//2

