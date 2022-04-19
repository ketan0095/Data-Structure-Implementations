# -------------------------------------------------------------------------
# Code for checking if Parenthesis are perfectly balanced in an expression
# -------------------------------------------------------------------------


open_brackets = ["(", "[", "{"]
closed_brackets = [")", "]", "}"]


def check_exp(exp):
    stack = []
    for char_ in exp:
        if char_ in open_brackets:
            stack.append(char_)
        if char_ in closed_brackets:
            # when found closing bracket 2 conditions must satisfy
            # 1. length of stack should not be 0
            # 2. last element pushed inside the stack must be the opening bracket
            get_ind = closed_brackets.index(char_)
            actual_opening_bracket = open_brackets[get_ind]
            if (len(stack) > 0) and (actual_opening_bracket == stack[len(stack) - 1]):
                stack.pop()
            else:
                print("Expression is Unbalanced ! Thanos Disapproves XD!")
                break

    if not len(stack):
        print("Expression is Perfectly balanced as all things should be !")
    else:
        print("Expression is Unbalanced ! Thanos Disapproves XD!")


check_exp("({}")
