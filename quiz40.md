### Quiz 40


#### Solution



##### Codes:

###### HTML file
```.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <script src="quiz40.js"></script>
    <title>Quiz 40</title>
</head>

<body>
<h1>Quiz 39</h1>
<input type = "button" onclick = "ActivateFunction()" value = "ActivateFunction">

<h5>Input:</h5>
<p id="input"></p>


<h5>Output/Number of matches that Lily needs:</h5>
<p id="output"></p>



</body>

</html>
```

###### Javascript file
```.js


function ActivateFunction() {
    var input_of_distance = 500
    var input_of_speed = 150
    document.getElementById("input").innerHTML = input_of_distance + "," + input_of_speed ;

    //converting meters to centimeters:
    input_of_distance = input_of_distance*100

    //check how many seconds does Lily need to walk:
    input_of_distance = input_of_distance/input_of_speed

    //check how many 5 seconds matches Lily needs:
    var matches = input_of_distance/5
    matches = Math.ceil(matches)

    console.log(matches)
    document.getElementById("output").innerHTML = matches + " matches" ;
}


```

##### Testing:

![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-05-07%20at%2011.47.33.png)
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-05-07%20at%2011.47.16.png)
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-05-07%20at%2011.46.29.png)
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-05-07%20at%2011.42.57.png)
