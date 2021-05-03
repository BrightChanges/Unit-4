### Quiz 38


#### Solution


##### Codes:

###### HTML file
```.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <script src="quiz38.js"></script>
    <title>Quiz 38</title>
</head>

<body>
<h1>Quiz 38</h1>
<input type = "button" onclick = "ActivateFunction()" value = "Activate function">

<h5>Input:</h5>
<p id="input"></p>



<h5>Output:</h5>
<p id="output"></p>

</body>

</html>

```

###### Javascript file
```.js

//TASK: Data structure alignment creates pack of one size.
//It takes the biggest object to be stored and choose
//that to be the size of each pack. Each pack will
//take up that much memory even if the pack is not full
//Then it takes object in order and group them into packs
//output the amount of memory from an array with different object sizes:

function ActivateFunction() {

    //for testing:
    // var array = [64,1]
    // var array = [4,3,3,3,3,3]
    // var array = [5,10,16,5,10]
    // var array = [1,2,8,2,4]
    var array = [1,2,4,10,2,4,2,16,2,1,1]
    document.getElementById("input").innerHTML = array ;
    var max = 0
    var sum = 0
    var count = 0

    //the for loop below find the maximum value in the array:
    for (i = 0; i < array.length; i++) {
        if (array[i] > max){
            max = array[i]
        }
    }

    console.log(max)

    //the for loop below sum up the elements in the array along the way and
    //compare it to the maximum value, if the sum of the value and the next value with the
    //original sum is greater than the maximum value, we increase the count variable by 1
    //and reset the sum back to 0 because we know that the next element will be
    //in another packet:
    for (x = 0; x < array.length-1; x++) {

        if(sum+array[x]+array[x+1]>max){
            count+=1
            sum = 0
        }else{
            sum+=array[x]

        }

    }

    //the count variable represents the number of packets that have the maximum size
    //equal to the maximum value in the array.
    //because of this, to calculate the total memory size, we take the count
    //and multiply it with the maximum value:
    var number_of_bytes = ((count+1) * max) //+1 for count as we count the last package in the end of the array

    console.log(number_of_bytes)

    document.getElementById("output").innerHTML = number_of_bytes + " bytes" ;

}


```

##### Testing:

![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-05-03%20at%2017.43.38.png)
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-05-03%20at%2017.43.19.png)
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-05-03%20at%2017.42.59.png)
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-05-03%20at%2017.42.31.png)
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-05-03%20at%2017.42.13.png)

