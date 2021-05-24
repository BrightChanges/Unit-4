### Quiz 42


#### Solution



##### Codes:

###### HTML file
```.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <script src="quiz42.js"></script>
    <title>Quiz 42</title>
</head>

<body>
<h1>Quiz 42</h1>
<input type = "button" onclick = "ActivateFunction()" value = "ActivateFunction">

<h5>Input:</h5>
<p id="input"></p>


<h5>Output:</h5>
<p id="output"></p>



</body>

</html>
```

###### Javascript file
```.js






function ActivateFunction() {

    var input = 1520000

    document.getElementById("input").innerHTML = input ;
    input = String(input)
    //we create a placeholder for the output:

    var output = ""
    //we add the first element,  a dot, and the next 2 elements from the string
    output += input[0] + "." + input[1] + input[2] + " *"
    //we then add the amount of 0 by minus the length by 1:
    output += " le" + String(input.length-1)

    document.getElementById("output").innerHTML = output ;
    console.log(output)
}



```

##### Testing:

![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-05-24%20at%2013.44.20.png)
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-05-24%20at%2013.44.01.png)
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-05-24%20at%2013.43.49.png)

