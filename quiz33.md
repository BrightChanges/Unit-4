### Quiz 33


#### Solution

##### Flow Diagram:

![](https://github.com/BrightChanges/Unit-4/blob/main/IMG_0394.jpg)

##### Codes:

###### HTML file
```.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <script src="countLetter.js"></script>
    <title>Count_letter</title>
</head>

<body>
<h1>Quiz 33</h1>
<input type = "button" onclick = "ActivateFunction()" value = "Activate function">

<h5>Text:</h5>
<p id="text"></p>

<h5>Letter:</h5>
<p id="letter"></p>

<h5>Output:</h5>
<p id="output"></p>

</body>
</html>

```

###### Javascript file
```.js

//TASK: In order o be able to quickly analyze many texts, create a progra
//that calculates how many times a given letter is present in a text

function ActivateFunction() {
    var text = "abcdefgaaa" //should print 4 on the console
    var letter = "a"
    document.getElementById("text").innerHTML = text ;
    document.getElementById("letter").innerHTML = letter ;
    var count = 0

    // the code below is the backbone of this function.
    //it loop through all letters in the text and count
    //how many times the letters we want to count are the same with those letters
    //in doing so, count how many times it present in the text.
    for (i = 0; i < text.length; i++) {
        if (text[i] == letter){
            count += 1
        }
    }

    console.log(count)
    document.getElementById("output").innerHTML = count ;

}



```

##### Testing:

![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-04-22%20at%2011.35.42.png)
