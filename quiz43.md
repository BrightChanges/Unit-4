### Quiz 43


#### Solution



##### Codes:

###### HTML file with Javascript:
```.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">

    <title>Quiz 43</title>
</head>

<body>
<h1>Quiz 43</h1>
<h3>Input is "560i_"</h3>

<script>
    function rectangle (input) {
        //we create the widths of the rectangle:
        var up_down_side = ""
        up_down_side += input[2]

        for (a = 0; a < input.length-2; a++) {
            up_down_side+= input[4]
        }

        up_down_side += input[2]

        //we draw one of the width of the rectangle
        console.log(up_down_side)
        
        //we then create the heights of the rectangle:
        var middle_side = ""
        middle_side += input[3]

        for (b = 0; b< input.length-2; b++) {
            middle_side += " "
        }

        middle_side+= input[3]

        for (i = 0; i < input.length-2; i++) {
            //we draw the heights of the rectangle
            console.log(middle_side)
        }
        
        
        //we then draw the last width of the rectangle to completely draw
        //the entire rectangle:
        console.log(up_down_side)
    }

    rectangle("560i_")
</script>






</body>

</html>


```



##### Testing:

![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-05-25%20at%208.26.34.png)
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-05-25%20at%208.25.37.png)

