## Quiz 44


### Solution



#### Codes:

##### Javascript
###### HTML file with Javascript:

```.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">

    <title>Quiz 44</title>
</head>

<body>
<h1>Quiz 44</h1>


<script>
    function conversion (l) {
        var list_0 = ["false", "no", "zero", "0"]
        var list_1 = ["true", "yes", "one", "1"]
        var binary_list = []
        
        //we split the input
        l = l.split(" ")

        //we loop over the input to convert each element to a binary number
        //then we add the converted binary number to a list for further use.
        for (i = 0; i < l.length; i++) {
            if(list_0.includes(l[i])){
                binary_list.push(0)
            }
            else if(list_1.includes(l[i])){
                binary_list.push(1)
            }
        }

        console.log(binary_list)

        var exponent = binary_list.length -1
        var sum = 0
        
        //we then do a final loop over the converted list of binary numbers
        //to convert it to a decimal:
        for (x = 0; x < binary_list.length; x++) {
            sum += binary_list[x] * (2**exponent)
            exponent -=1
        }

        console.log(sum)

    }

    conversion("1 0 yes no one true yes false yes no 1 0 1")
    conversion("true no 1 false")
    conversion("true true true true")
    conversion("0 1 no yes zero false no true no yes 0 1 0")


</script>






</body>

</html>


```

##### Python

```.py



def conversion(l):
    #we split the input:
    l = l.split(" ")


    list_0 = ["false", "no", "zero", "0"]
    list_1 = ["true", "yes","one", "1"]
    binary_list = []
    
    #we loop over the input to convert each element to a binary number
    #then we add the converted binary number to a list for further use.
    for i in range(len(l)):
        if l[i] in list_0:
            binary_list.append(0)
        elif l[i] in list_1:
            binary_list.append(1)

    print(binary_list)

    exponent = len(binary_list)-1
    sum = 0
    
    #we then do a final loop over the converted list of binary numbers
    #to convert it to a decimal:
    for x in range(len(binary_list)):
        sum += binary_list[x] * 2**exponent
        exponent -=1

    return sum

print(conversion("1 0 yes no one true yes false yes no 1 0 1"))
print(conversion("true no 1 false"))
print(conversion("true true true true"))
print(conversion("0 1 no yes zero false no true no yes 0 1 0"))

```


### Testing:

##### Javascript:
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-05-28%20at%2012.16.36.png)

##### Python:
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-05-28%20at%2012.22.20.png)

