### Class Collection


#### Solution


##### Codes:

```.py



class Collection:

    def __init__(self, data, current_index):
        self.data = data
        self.current_index = current_index

    def additem(self, value):
        # if self.isempty() == False:
        self.data.append(value)
        return self.data

    def getnext(self):
        # holding_variable = 0
        if self.current_index == -1:
            holding_variable = self.data[0]
            self.current_index +=1
        else:
            holding_variable = self.data[self.current_index+1]
            self.current_index += 1

        return holding_variable


    def resetnext(self):
        self.current_index = -1
        return self.current_index


    def hasnext(self):
        if len(self.data) > self.current_index +1:
            return True
        else:
            return False

    def isempty(self):
        if len(self.data)==0:
            return True
        else:
            return False


    def print_all_elements(self):
        for i in self.data:
            print(i)


Collection1 = Collection(["printer","CPU task scheduling","call center"],-1)

print(Collection1.hasnext())
print(Collection1.isempty())
print(Collection1.additem("spotify"))
print(Collection1.getnext())
print(Collection1.getnext())
print(Collection1.getnext())
print(Collection1.resetnext())
print(Collection1.getnext())







```

##### Testing:

![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-09-23%20at%2010.33.02.png)
