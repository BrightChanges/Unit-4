### Class Array


#### Solution


##### Codes:

```.py

class Array:
    def __init__(self, size, data):
        self.size = size
        self.data = data

    def get(self, index):
        if index>=self.size:
            print("Error: index out of range. Pls get a value that has an index smaller than 5")
        else:
            print(self.data[index])


    def set(self, index, value):
        if index>=self.size:
            print("Error: index out of range. Pls get a value that has an index smaller than 5")
        else:
            self.data[index] = value
        print(self.data)


Array1 = Array(5,[1,0,2,0,10])

Array1.get(4)
Array1.set(1,9)

Array1.get(6)


```

##### Testing:

![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-09-10%20at%2012.07.42.png)
