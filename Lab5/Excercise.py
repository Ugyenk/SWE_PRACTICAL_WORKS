# Stack Implementation
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)


# Queue Implementation Using Two Stacks
class QueueWithTwoStacks:
    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def is_empty(self):
        return self.stack_in.is_empty() and self.stack_out.is_empty()

    def enqueue(self, item):
        self.stack_in.push(item)

    def dequeue(self):
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        if not self.stack_out.is_empty():
            return self.stack_out.pop()
        else:
            raise IndexError("Queue is empty")


# Function to evaluate postfix expressions
def evaluate_postfix(expression):
    stack = Stack()
    for token in expression.split():
        if token.isdigit():  # Check if the token is an operand
            stack.push(int(token))
        else:  # The token is an operator
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.push(a + b)
            elif token == '-':
                stack.push(a - b)
            elif token == '*':
                stack.push(a * b)
            elif token == '/':
                stack.push(a / b)
    return stack.pop()


# Task Scheduler Using Queue
class TaskScheduler:
    def __init__(self):
        self.queue = QueueWithTwoStacks()

    def add_task(self, task):
        self.queue.enqueue(task)

    def run_tasks(self):
        while not self.queue.is_empty():
            task = self.queue.dequeue()
            print(f"Processing task: {task}")


# Function to convert infix to postfix expressions
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0


def infix_to_postfix(expression):
    stack = Stack()
    postfix = []
    for char in expression:
        if char.isalnum():  # Check if character is an operand
            postfix.append(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.is_empty() and stack.peek() != '(':
                postfix.append(stack.pop())
            if not stack.is_empty():  # Check if stack is not empty before popping '('
                stack.pop()  # Pop the '('
        else:
            while (not stack.is_empty() and precedence(char) <= precedence(stack.peek())):
                postfix.append(stack.pop())
            stack.push(char)

    while not stack.is_empty():
        postfix.append(stack.pop())

    return " ".join(postfix)


# Testing the functions

# 1. Postfix Evaluation
postfix_expr = "3 4 + 2 * 7 /"
print("Postfix Evaluation Result:", evaluate_postfix(postfix_expr))  # Expected Result: 2.0

# 2. Queue with Two Stacks
queue = QueueWithTwoStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Dequeue from QueueWithTwoStacks:", queue.dequeue())  # Expected: 1

# 3. Task Scheduler
scheduler = TaskScheduler()
scheduler.add_task("Task 1")
scheduler.add_task("Task 2")
scheduler.add_task("Task 3")
scheduler.run_tasks()  # Expected to process each task in order

# 4. Infix to Postfix Conversion
infix_expr = "A+B*(C^D-E)"
print("Infix to Postfix:", infix_to_postfix(infix_expr))  # Expected Output: "A B C D ^ E - * +"
