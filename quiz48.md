### Quiz 48


#### Solution


##### Codes:

Codes for the quiz:
```.py

from classqueue import Queue

#can't create an empty Queue
#because in the class Queue,
#if the queue is empty, I can't enqueue or dequeue value
Q=Queue(["0"])
sum = 0

print(Q)

for i in range(10):
    inp = input("Pls input an integer")
    Q.enqueue(inp)

for i in range(10):
    dq = Q.dequeue()
    # print(dq)
    sum += int(dq)

print(Q)
print(sum/10)


```
Codes for the class:

```.py



class Queue:

    def __init__(self, data):
        self.data = data

    def enqueue(self, value):
        if self.isempty() == False:
            self.data.append(value)
        return self.data


    def dequeue(self):
        updated_queue = []
        if self.isempty() == False:
            for i in range(1,len(self.data)):
                updated_queue.append(self.data[i])
        self.data = updated_queue
        print(self.data)
        print (updated_queue)
        return self.data[0]

    def isempty(self):
        return len(self.data) == 0



```

##### Testing:

![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-09-16%20at%209.19.50.png)
