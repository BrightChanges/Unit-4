### Quiz 37


#### Solution

##### Flow Diagram:

![](https://github.com/BrightChanges/Unit-4/blob/main/IMG_0454.jpg)

##### Codes:

###### HTML file
```.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <script src="quiz37.js"></script>
    <title>Quiz 37</title>
</head>

<body>
<h1>Quiz 37</h1>
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

//TASK: Create a program that find the biggest difference between two numbers from a string:

function ActivateFunction() {
    //Use for testing:
    var input = "02354310"
    // var input = "12386456792"
    // var input = "12387856792"
    // var input = "21025643894"
    // var input = "0"
    document.getElementById("input").innerHTML = input;

    //we create a value to store the biggest difference:
    var biggest_difference = 0

    //we create a for loop that compare the difference between every two
    //elements that are next to each other, if the difference is bigger than
    //the preset biggest difference, we update that value as the biggest difference:

    for (i = 0; i < input.length; i++) {
        var difference =  input[i+1] - input[i]
        if (Math.abs(difference) > Math.abs(biggest_difference)){
            biggest_difference = difference
        }
    }

    console.log(biggest_difference)
    document.getElementById("output").innerHTML = biggest_difference;

}


```

##### Testing:

![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-04-30%20at%2014.08.23.png)
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-04-30%20at%2014.08.00.png)
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-04-30%20at%2014.07.05.png)
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-04-30%20at%2014.06.40.png)
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-04-30%20at%2014.06.04.png)

