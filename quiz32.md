### Quiz 32


#### Solution



##### Codes:

###### HTML file
```.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <script src="Blackbox.js"></script>
    <title>Blackbox</title>
</head>

<body>
<h1>Quiz 32</h1>
<input type = "button" onclick = "ActivateFunction()" value = "Activate function">

<h5>Input:</h5>
<p>Input 1: " oworllledH!", Input 2: "SSEEESESSESE"</p>

<h5>Output:</h5>
<p id="output"></p>

</body>


</html>
```

###### Javascript file
```.js
//TASK: Black box: create the algorithm that produces the output given the input.

function ActivateFunction() {
    var input_1 = " oworllledH!"
    var input_2 = "SSEEESESSESE"


    var s_letters = []

    var e_letters = []

    //First, group all the element of input 1 that has same index with element in input 2 that are equal to S and E
    //into either s_letters and e_letters:

    for (i = 0; i < input_2.length; i++) {
        if (input_2[i] == "S"){
            s_letters.push(input_1[i])
        }else if(input_2[i] == "E"){
            e_letters.push(input_1[i])
        }
    }


    //convert s_letters to a string:
    s_letters = s_letters.join("");

    console.log(s_letters)

    //flip all the element in s_letters into new_s_letters:
    var new_s_letters = ""

    for (let a = s_letters.length - 1; a >= 0; a--) {
        new_s_letters += s_letters[a];
    }

    console.log(new_s_letters)

    // convert e_letters to a string:
    e_letters= e_letters.join("")
    console.log(e_letters)

    //add new_s_letters with e_letters to get the output:
    var output = new_s_letters + e_letters

    console.log(output)
    document.getElementById("output").innerHTML = output ;

}



```

##### Testing:

![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-04-16%20at%2012.10.58.png)

![]()

![]()
