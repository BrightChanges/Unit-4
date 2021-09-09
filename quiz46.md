### Quiz 46


#### Solution


##### Codes:

```.py

def zero_to_thousand():
    Highest = 0
    Counter = 0
    Amount = 0
    Sum = 0
    Lowest = 1


    while Counter < 999:
        for input in range(1,1000):
            if input >= 0 and input <=999:
                Amount+=1
                Sum+=input

                if input>Highest:
                    Highest = input
                elif input < Lowest:
                    Lowest = input
                Counter +=1

    # print(Counter)
    print(Highest)
    print(Lowest)
    print("Sum is {}".format(Sum))
    print("Amount is {}".format(Amount))
    print(Sum/Amount)

zero_to_thousand()

```

##### Testing:

![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-09-09%20at%2022.06.11.png)
