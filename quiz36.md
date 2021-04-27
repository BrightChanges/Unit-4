### Quiz 36


#### Solution



##### Codes:

###### HTML file
```.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <script src="quiz36.js"></script>

    <title>Quiz 36</title>
</head>

<body>
<h1>Quiz 36</h1>
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

//TASK: BlackBox

function ActivateFunction() {

    //For testing:

    // var array = [22,13,4,5,1,12,10,66,9]
    // var array = [1,2,3,4,5,6,7]
    // var array = [20,18,19,16,9,8,7,6,8,2]
    var array = [3,2,1]
    // var array = [5,4,3,2,1]
    // var array = [30,2,1,2]
    // var array = [5,4,1,3,2,2]
    // var array = [8,7,6,5,4,3,2,1]
    document.getElementById("input").innerHTML = array ;


    //first, we need to re-organize the array in order from big to small:

    for (i=0; i<array.length; i++){

        for (x=0; x<array.length; x++){
            if (array[x]<array[x+1]){
                var small_value = array[x]
                var big_value = array[x+1]

                array[x] = big_value
                array[x+1] = small_value
            }



        }
    }

    //for even length array, we find the mean and take it down to the nearest integer
    if(array.length % 2 == 0){
        var mean = 0
        for(a=0;a<array.length;a++){
            mean += array[a]

        }
        mean = mean/array.length
        mean = Math.floor(mean)
        console.log(mean)
        document.getElementById("output").innerHTML = mean ;
    }
    //for odd length array, we find the median number
    if(array.length % 2 != 0){
        var index_of_median = ((array.length+1)/2) -1 //-1 is because the index goes from 0
        var median = array[index_of_median]

        console.log(median)
        document.getElementById("output").innerHTML = median ;
    }






}



```

##### Testing:

![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-04-27%20at%2012.14.30.png)
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-04-27%20at%2012.14.20.png)
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-04-27%20at%2012.14.09.png)
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-04-27%20at%2012.13.53.png)
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-04-27%20at%2012.13.14.png)
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-04-27%20at%2012.13.02.png)
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-04-27%20at%2012.12.45.png)
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-04-27%20at%2012.12.24.png)
