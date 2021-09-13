### Class Queue


#### Solution


##### Codes:

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
        return updated_queue

    def isempty(self):
        return len(self.data) == 0


Queue1 = Queue(["printer","CPU task scheduling","call center"])

print(Queue1.enqueue("spotify"))
print(Queue1.enqueue("handling of interrupt"))
print(Queue1.enqueue("virtual waitlist"))
print(Queue1.dequeue())
print(Queue1.dequeue())


```

##### Testing:

![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-09-13%20at%208.57.28.png)
