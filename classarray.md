### Class Array


#### Solution


##### Codes:

```.py
class Array:
    def __init__(self, size, data):
        self.size = size
        self.data = data

    def get(self, index):
        print(self.data[index])

    def set(self, index, value):
        self.data[index] = value
        print(self.data)


Array1 = Array(5,[1,0,2,0,10])

Array1.get(4)
Array1.set(1,9)

```

##### Testing:

![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-09-10%20at%2011.56.23.png)
