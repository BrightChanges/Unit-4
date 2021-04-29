### Quiz 35


#### Solution (currently only works for positive degrees that are divisble by 5)



##### Codes:

###### HTML file
```.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <script src="quiz35.2.js"></script>

    <title>Quiz 35</title>
</head>

<body>
<h1>Quiz 35.2</h1>
<input type = "button" onclick = "ActivateFunction()" value = "Activate function">

<h5>Input of degree:</h5>
<p id="input"></p>



<h5>Output of time:</h5>
<p id="output"></p>

</body>
</html>

```

###### Javascript file
```.js


function ActivateFunction() {

    //45 works, 15 works, 90 works
    var input = 15
    document.getElementById("input").innerHTML = input ;

    var hours = [1,2,3,4,5,6,7,8,9,10,11,12]
    var minutes = ["00","01","02","03","04","05","06","07","08","09"]

    for(i = 10; i<61 ; i++){
        minutes.push(i)
    }
    
    //looping through all the combination of hours and minutes:
    for (x = 0; x<hours.length; x++ ){

        for (y=0; y<minutes.length; y++){
            var first_range = hours[x]
            var minute_hint = parseInt(minutes[y])

            if(minute_hint == "00"){
                        var minute_hint_updated= 60
                    }else{
                minute_hint_updated = minute_hint
            }

            var second_range = minute_hint_updated/5

            var real_degree = second_range - (first_range + (minute_hint/60))

            var degree = 30 * real_degree

            var absolute_value_input = Math.abs(input)
            
            //the code below check if a degree of one of the combination from the loop above
            //match the input degree or not:
            if (degree == absolute_value_input && minute_hint!=60){

                if (minute_hint == "0"){
                    minute_hint = "0" + minute_hint
                }

                var correct_output = first_range + ":" + minute_hint
                // console.log(minute_hint)
                // console.log(degree)
                console.log(correct_output)
                document.getElementById("output").innerHTML = correct_output;
            }
        }

    }


  




}




```

##### Testing:

![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-04-26%20at%2020.50.05.png)
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-04-26%20at%2020.50.17.png)
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-04-26%20at%2020.50.26.png)
