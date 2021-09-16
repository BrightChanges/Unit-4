### Quiz 48


#### Solution


##### Codes:

Codes for the quiz:
```.py
from classqueue import Queue

#can't create an empty Queue
#because in the class Queue,
#if the queue is empty, I can't enqueue or dequeue value
Q=Queue([ ])
sum = 0

# print(Q)

for i in range(10):
    inp = input("Pls input an integer")
    Q.enqueue(inp)

# Q.print_all_elements()

for i in range(10):
    dq = Q.dequeue()
    print(dq)
    sum += int(dq)

# Q.print_all_elements()

print(Q)
print(sum/10)




```
Codes for the class:

```.py





class Queue:

    def __init__(self, data):
        self.data = data

    def enqueue(self, value):
        # if self.isempty() == False:
        self.data.append(value)
        return self.data


    def dequeue(self):
        updated_queue = []
        if self.isempty() == False:
            for i in range(1,len(self.data)):
                updated_queue.append(self.data[i])
            holding_variable = self.data[0]
            self.data = updated_queue

            return holding_variable
        else:
            return 0
        # self.data = updated_queue
        # print(self.data)
        # print (updated_queue)


    def isempty(self):
        return len(self.data) == 0

    def print_all_elements(self):
        for i in self.data:
            print(i)








```

##### Testing:

![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-09-16%20at%209.44.08.png)
