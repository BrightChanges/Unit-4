### Class Stack


#### Solution


##### Codes:

```.py

class Stack:

    def __init__(self, data):
        self.data = data

    def push(self, value):
        if self.isempty() == False:
            self.data.append(value)
        return self.data


#need to remove every last item in order to simulate the
#Last in first out data structure of a Stack

    def pop(self):
        updated_stack = []
        if self.isempty() == False:
            for i in range(0, len(self.data)-1):
                updated_stack.append(self.data[i])
        else:
            print("Stack is empty, pls push something into the stack first")
        self.data = updated_stack
        print(self.data)
        return updated_stack

    def isempty(self):
        return len(self.data) == 0

    def count(self):
        return len(self.data)


Stack1 = Stack(["printer","CPU task scheduling","call center"])

print("Starting to push")
print(Stack1.push("spotify"))
print(Stack1.push("handling of interrupt"))
print(Stack1.push("virtual waitlist"))
print("Starting to pop")
print(Stack1.pop())
print(Stack1.pop())
print(Stack1.pop())
print("Count elements in stack")
print(Stack1.count())




```

##### Testing:

![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-09-16%20at%208.51.49.png)
