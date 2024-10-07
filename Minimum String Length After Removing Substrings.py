class Solution:
    def minLength(self, s: str) -> int:
        my_stack=[]
        for char in s:
            if not my_stack:
                my_stack.append(char)
                continue
            if char=='B' and my_stack[-1]=='A':
                my_stack.pop()
            elif char=='D' and my_stack[-1]=='C':
                my_stack.pop()
            else:
              my_stack.append(char)
        return len(my_stack)
