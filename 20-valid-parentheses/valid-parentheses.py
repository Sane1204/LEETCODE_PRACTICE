class Solution:
    def isValid(self, s: str) -> bool:
        dic={"]":"[",")":"(","}":"{"}
        stack=[]

        for i in s:
            if i in dic:
                if not stack:
                    return False
                if stack[-1] != dic[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return not stack








        