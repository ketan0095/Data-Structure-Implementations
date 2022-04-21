# https://www.geeksforgeeks.org/queue-using-stacks/


# Method 1 (By making enQueue operation costly) :

# enQueue: O(n)
# While stack1 is not empty, push everything from stack1 to stack2.
# Push x to stack1 (assuming size of stacks is unlimited).
# Push everything back to stack1.


# deQueue(q): O(1)
# If stack1 is empty then error
# Pop an item from stack1 and return it


class queue:
    # create two stacks
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enQueue(self, ele):
        # Move all elements from stack1 to stack2 in reverse order
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1[-1])
            self.stack1.pop()

        # Push current element into stack1
        self.stack1.append(ele)
        print("Stack 2 :", self.stack2)

        # Push everything back to stack1 from stack2
        # which will maitain the Fist come , Fist go Order
        while len(self.stack2) != 0:
            self.stack1.append(self.stack2[-1])
            self.stack2.pop()

        print("Stack 1 :", self.stack1)

    def deQueue(self):

        if len(self.stack1) == 0:
            print("Queue is Empty!")
        # Return top of stack1
        top = self.stack1[-1]
        self.stack1.pop()
        return top


# Method 2 (By making deQueue operation costly)

# enQueue : O(1)
#   1) Push x to stack1 (assuming size of stacks is unlimited).

# deQueue : O(n)
#   1) If both stacks are empty then error.
#   2) If stack2 is empty
#        While stack1 is not empty, push everything from stack1 to stack2.
#   3) Pop the element from stack2 and return it.


class queue2:
    def __init__(self) -> None:
        self.stack1 = []
        self.stack2 = []

    def enQueue(self, x):
        self.stack1.append(x)

    def deQueue(self):
        print("Stack1 : ", self.stack1)
        print("Stack2 : ", self.stack2)
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            print("Queue is Empty!")
            return
        elif len(self.stack1) > 0 and len(self.stack2) == 0:
            while len(self.stack1):
                temp = self.stack1.pop()
                self.stack2.append(temp)
            return self.stack2.pop()

        else:
            return self.stack2.pop()


if __name__ == "__main__":

    print("Method 1 :")
    q = queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)

    q.deQueue()
    q.deQueue()
    q.deQueue()

    print()
    print("Method 2 :")
    q = queue2()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)

    q.deQueue()
    q.deQueue()
    q.deQueue()
