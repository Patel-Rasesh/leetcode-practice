class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        mathStack = []
        def Operation(operand1, operand2, operator):
            if operator == '*':
                return int(operand2) * int(operand1)
            elif operator == '/':
                return int(int(operand2) / int(operand1))
            elif operator == '+':
                return int(operand2) + int(operand1)
            elif operator == '-':
                return int(operand2) - int(operand1)
            
        # 1. Push values (from tokens) to the stack
        for eachToken in tokens:
            
            # 2. Until encountering an operator
            if eachToken in ['*', '/', '+', '-']:
                mathStack.append(Operation(mathStack.pop(-1), mathStack.pop(-1), eachToken))
            else:
                mathStack.append(int(eachToken))
        
        print(mathStack)
        return mathStack[0]