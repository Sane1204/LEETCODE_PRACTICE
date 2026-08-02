class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for ch in s:
            if (self.isopen(ch)):
                st.append(ch)
            else:
                if (len(st)==0):
                    return False
                else:
                    if (self.doesmatch(st[-1],ch)):
                        st.pop()
                    else:
                        return False
        if len(st)==0:
            return True
        else:
            return False

    def isopen(self, ch):
        return ch == '(' or ch=='[' or ch=='{'
    def doesmatch(self , op,cl):
        return (op == '(' and cl == ')') or (op == '[' and cl == ']') or (op == '{' and cl == '}')