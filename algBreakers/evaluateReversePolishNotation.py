# attempt 2: 3-25-20
def evalRPN(self, tokens: List[str]) -> int:
        # declare MT array
        operandsStack = []
        
        # create the functions to respond to operators
        def operation(str, a, b):
            a = int(a)
            b = int(b)
            
            if str == "+":
                return (a + b)
            if str == "-":
                return (a - b)
            if str == "*":
                return (a * b)
            if str == "/":
                if a > b:
                    if b == 0:
                        return 0
                    return (a / b)
                return (b/ a)

        # iterate through list pushing items on to stack as numbers
        for operand in tokens:
            # when we arrive at an operator we take the two numbers on the stack and compute them using operator logic
            if operand == '+' or operand == '-' or operand == '/' or operand == '*':
                operandsToPopA = operandsStack.pop()
                operandsToPopB = operandsStack.pop()
                # then pop evaluation of operator on to stack
                operandsStack.append(operation(operand, operandsToPopA, operandsToPopB))
            else:
              operandsStack.append(operand)
            
        # we return the first element of the stack --> the only one
        return operandsStack.pop() 

testinputA = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

print(evalRPN(testinputA))

# Solution: The questions is solved using a stack data structure. We move through our list pushing elements on to the stack and when we come by an operator we take the top two elements and complete the operation on them.

# test cases failed: ["4","3","-"] | output -1 | expected 1

# Space: O(N) operation 
# Time: 
#     T = operands
#     O(T)