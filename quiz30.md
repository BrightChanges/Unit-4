### Quiz 30


#### Solution

##### Flow Diagram:
![](https://github.com/BrightChanges/Unit-4/blob/main/IMG_0341.jpg)

##### Codes:

```.py

#TASK: Find the numbers of divisors of the number that are divisible by 2

class quiz30():

    def __init__(self, input):
        self.input = input


    def FindTwoDivisiors(self):

        num = 0
        
        #any number that cannot be divided by 2
        #will not have any divisors that could
        #divide by 2, there for, the if 
        #statement below could quickly
        #determine the number of divisors that are divisible by 2 of the input  number:
        
        if self.input % 2 == 0:
            for x in range(1,self.input+1):
                if self.input%x==0 and x%2==0:
                    num+=1

            return num
        else:
            return 0



test1=quiz30(8)
print(test1.FindTwoDivisiors())

test2=quiz30(9)
print(test2.FindTwoDivisiors())

test3=quiz30(158260522)
print(test3.FindTwoDivisiors())

test4=quiz30(861648772)
print(test4.FindTwoDivisiors())

test5=quiz30(569097293)
print(test5.FindTwoDivisiors())


```

##### Testing:

![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-04-12%20at%2014.45.58.png)
