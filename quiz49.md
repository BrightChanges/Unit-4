### Quiz 49


#### Solution


##### Codes:

Codes for the quiz:
```.py
#Create a program that asks the user for 10 ib scores stores them in
#a stack and shows the average-without losing elements in the stack
#when pop()
from classstack import Stack

#can't create an empty Queue
#because in the class Queue,
#if the queue is empty, I can't enqueue or dequeue value
S1=Stack([ ])
S2=Stack([ ])
sum = 0

# print(Q)

#creates a stack- called stack 1
#mirror that stack- called stack 2
#pop stack 2 so stack 1 will not be affected

for i in range(10):
    inp = input("Pls input an IB score")
    if int(inp) > 0 and int(inp) <8:
        S1.push(inp)
    else:
        print("Your IB score is invalid. Pls re start the program and input proper IB score")

S2=S1

# Q.print_all_elements()

for i in range(10):
    pop_element = S2.pop()
    sum += int(pop_element)


# Q.print_all_elements()

# print(S)
print(sum/10)






```
Codes for the class:

```.py


class Stack:

    def __init__(self, data):
        self.data = data

    def push(self, value):
        # if self.isempty() == False:
        self.data.append(value)
        return self.data


#need to remove every last item in order to simulate the
#Last in first out data structure of a Stack

    def pop(self):
        updated_stack = []
        if self.isempty() == False:
            for i in range(0, len(self.data)-1):
                updated_stack.append(self.data[i])
            holding_variable = self.data[len(self.data)-1]
            self.data = updated_stack
            return holding_variable

        else:
            print("Stack is empty, pls push something into the stack first")
            return 0

    def isempty(self):
        return len(self.data) == 0

    def count(self):
        return len(self.data)

    def print_all_elements(self):
        for i in self.data:
            print(i)





```

##### Testing:

![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-09-17%20at%2011.36.36.png)
