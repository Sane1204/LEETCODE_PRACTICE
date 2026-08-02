class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for tok in tokens:
            if self.isoperand(tok):
                op1= st.pop()
                op2 = st.pop()

                result = self.eval(tok,op2,op1)
                st.append(result)
            else:
                st.append(int(tok))
        return st[-1]
    
    def isoperand(self , token):
        return token == "+" or token == "-" or token == "/" or token =="*"
    
    def eval(self, operator, op1, op2):
        if operator=="+":
            return op1 + op2
        elif operator=="-":
            return op1 - op2
        elif operator=="*":
            return op1 * op2
        elif operator=="/":
            return int(op1 / op2)
        else:
            return 0
        