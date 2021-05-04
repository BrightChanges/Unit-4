### Quiz 39


#### Solution



##### Codes:

###### HTML file
```.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <script src="quiz39.js"></script>
    <title>Quiz 39</title>
</head>

<body>
<h1>Quiz 39</h1>
<input type = "button" onclick = "ActivateFunction()" value = "ActivateFunction">

<h5>Input:</h5>
<p id="input"></p>


<h5>Output:</h5>
<p id="output"></p>

<h5>Amount of Narcissistic numbers:</h5>
<p id="length"></p>

</body>

</html>

```

###### Javascript file
```.js


//TASK: Find Narcissistic numbers between a range of number m~n

function ActivateFunction() {
    var m = 0
    var n = 500
    var output = []
    document.getElementById("input").innerHTML = m + "~"+ n ;

    for (i = m; i < n+1; i++) {


        i = i.toString()

        var length = i.length

        var sum = 0

        for (x = 0; x < length; x++) {
            x = parseInt(x)
            sum += parseInt(i[x])**length

        }

        if(sum == parseInt(i) && sum!=n && sum!=m){
            console.log(i)
            output.push(i)
            document.getElementById("output").innerHTML = output ;
            document.getElementById("length").innerHTML = output.length ;

        }
    }
}



```

##### Testing:

![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-05-04%20at%209.35.33.png)

