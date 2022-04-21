# Infix  : operand1 <operator> operand2 , eg. 2 * 2
# Not easy to evaluate for machine


# prefix : <operator> operand1 , operand, eg. * 2,2
# postfix : operand1 , operand <operator> eg. 2,2 *


# convert x - y*z ?

# prefix : -x*yz
# postfix : yz*x-


# --------------------------------------
# Convert Infix expression to Postfix
# --------------------------------------
# https://www.youtube.com/watch?v=ysDharaQXkw&list=PLqM7alHXFySF7Lap-wi5qlaD8OEBx9RMV
# Step 1 : Scan the infix expression from left to right.
# Step 2 : if scanned character is operand, output it.
# Step 3 : Else :
#   1. if precedence of the scanned operator > operator in stack ( or stack is empty ) , push it in stack
#   2. else pop operator from stack , until higher or equal precedence operator is found residing at top of stack , & push it in stack
# Step 4 : if scanned char is '(' , push in stack
# Step 5 : if scanned char is ')' pop from stack until "(" is found
# Repeat 2-5 until infix exp is finished
# pop & output from stack until its not empty.


from lib2to3.pytree import WildcardPattern
from signal import raise_signal


class convert:
    def __init__(self, len_of_exp):

        # initialize stack top
        self.top -=1
        self.size = len_of_exp
        # create array
        self.array = []
        self.output = []
        # set precedence setting , higher prec. operator will have , higher number
        self.precedence = {"+": 1, "-": 2, "/": 2, "*": 3}

    # Empte check
    def check_if_empty(self):
        if self.top == -1:
            return True
        return False

    # Return the value of top of stack
    def peek(self):
        return self.array[-1]

    # Remove top element from stack
    def pop(self):
        # check if stack is empty
        if not self.check_if_empty():
            self.top = -1
            return self.array.pop()
        else:
            return "$"

    # Push the val in stack
    def push(self, val):
        self.top += 1  # increase the top size
        self.array.append(val)  # add value to stack

    # Check if element is Operand\
    def is_operand(self, ele):
        # check if element is alpha numeric
        return ele.isalpha()

    # Precedence level check
    def check_prec(self, operator):
        try:
            current_prec_level = self.precedence[operator]  # current level
            current_top_prec_level = self.precedence[self.peek()]  # exisitng top level

            if current_prec_level <= current_top_prec_level:
                # operator has higher precedence
                return True
            return False
        except Exception as e:
            # print("Exception :", e)
            return False

    # Convert Infix to Postfix
    def InToPost(self, exp):

        # Traverse thorugh expression
        for char in exp:
            if self.is_operand(char):
                # save operators in outpur array
                self.output.append(char)
            elif char == "(":
                self.push(char)
            elif char == ")":
                while (not self.check_if_empty()) and (self.peek() != "("):
                    # remove everything and save to output until find "("
                    removed_item = self.pop()
                    self.output.append(removed_item)

                if (not self.check_if_empty()) and (self.peek() != "("):
                    return -1
                else:
                    # after removing evrything , top element should be "(", if not return -1
                    self.pop()
            else:
                # Operator is found
                # if stack not empty & precedence is not higher
                while (not self.check_if_empty()) and (self.check_prec(char)):
                    # if char == ^ , it has to kept last
                    if char == "^" and self.array[-1] == char:
                        break
                    self.output.append(self.pop())
                self.push(char)

        # if after traversing all elements are not removed from stack
        while not self.check_if_empty():
            self.output.append(self.pop())

        print("".join(self.output))


# Driver program to test above function
exp = "a+b*(c^d-e)^(f+g*h)-i"
obj = convert(len(exp))
obj.InToPost(exp)
