# Exampe 1:
# Input: s = "1 + 1"
# Output: 2
# Example 2:
# Input: s = " 2-1 + 2 "
# Output: 3
# Example 3:
# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23

def calculate(s: str) -> int:
    stack = []
    num = 0
    sign = 1
    result = 0
    
    for i in range(len(s)):
        char = s[i]
        
        # If character is a digit
        if char.isdigit():
            num = num * 10 + int(char)
            
        # If character is +
        elif char == '+':
            result += sign * num
            num = 0
            sign = 1
            
        # If character is -
        elif char == '-':
            result += sign * num
            num = 0
            sign = -1
            
        # If character is opening parenthesis
        elif char == '(':
            # Push the result and sign onto the stack
            stack.append(result)
            stack.append(sign)
            # Reset result and sign
            result = 0
            sign = 1
            
        # If character is closing parenthesis
        elif char == ')':
            result += sign * num
            num = 0
            # Multiply with sign on top of stack
            result *= stack.pop()
            # Add the previous result from stack
            result += stack.pop()
            
    # Add the last number if exists
    if num != 0:
        result += sign * num
        
    return result

# Test cases
test_cases = [
    "1 + 1",
    " 2-1 + 2 ",
    "(1+(4+5+2)-3)+(6+8)"
]

for test in test_cases:
    print(f"Input: {test}")
    print(f"Output: {calculate(test)}\n")
