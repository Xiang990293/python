"""
Type the numbers like your car license plate, but saperated by a space, e.g. 1 2 3 4 or 5 6 7 8.
And then enter the numbers you aim to by space after the numbers above, e.g. 1 2 3 4 10.
and the program will tell you how to calculate those numbers to get the aimming number like 1+2+3+4=10.
"""
from itertools import permutations, product, combinations

def string_to_expression(expression):
    """
    Convert a string expression to a list of tokens.
    """
    
    return expression.split()

def if_prefix_valid(expression):
    """
    Check if the prefix notation expression is valid.
    """
    
    stack = []
    
    for token in reversed(expression):
        if token in "+-*/":
            if len(stack) < 2:
                return False
            stack.pop()  # Pop two operands
            stack.pop()  # Pop two operands
            stack.append("result")  # Push a result placeholder
        elif token.isdigit():
            stack.append(token)  # Push operand
        else:
            return False
    return len(stack) == 1

def prefix_notation_to_infix(expression):
    """
    Convert a prefix notation expression to infix notation.
    """
    if if_prefix_valid(expression) is False:
        return "-1"
    
    stack = []
    
    for token in reversed(expression):
        try:
            if token in "+-*/":
                left_operand = stack.pop()
                right_operand = stack.pop()
                new_expr = f"({left_operand} {token} {right_operand})"
                stack.append(new_expr)
            else:
                stack.append(token)
        except:
            return "-1"
    
    # print(expression, stack[0] if stack else "")
    # print(stack[0], eval(stack[0]))
    return stack[0] if stack else ""


def all_combinations_in_different_operators_and_order(numbers, target):
    """
    Find all combinations of numbers that can be combined with different operators to reach a target number in prefix notation.
    """
    number_of_numbers = len(numbers)
    operators = ['+', '-', '*', '/']
    
    for perm in product(*[operators]*(number_of_numbers-1)):
        expression_row = list(numbers)
        expression_row.extend(perm)
        
        for full_perm in reversed(list(permutations(expression_row))):
            full_perm = list(full_perm)
            if if_prefix_valid(full_perm):
                try:
                    if float(eval(prefix_notation_to_infix(full_perm))) == float(target):
                        return prefix_notation_to_infix(full_perm)
                except ZeroDivisionError:
                    continue
    
    
    
if __name__ == "__main__":
    print("""
Type the numbers like your car license plate, but saperated by a space, e.g. 1 2 3 4 or 5 6 7 8.
And then enter the numbers you aim to by space after the numbers above, e.g. 1 2 3 4 10.
and the program will tell you how to calculate those numbers to get the aimming number like 1+2+3+4=10.
    """)
    # print(eval(prefix_notation_to_infix(string_to_expression("+ + + 1 2 3 4"))) == 10)
    while True:
        numbers = input("")

        numbers_list = list(numbers.split())
        aim = numbers_list[-1]
        numbers_list.pop()  # Remove the last number which is the aim

        found = False
        results = all_combinations_in_different_operators_and_order(numbers_list, aim)
        print(results)