### Quiz 41


#### Solution



##### Codes:

###### HTML file
```.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <script src="quiz41.js"></script>
    <title>Quiz 41</title>
</head>

<body>
<h1>Quiz 41</h1>
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
    //input
    var list = [6,9]
    document.getElementById("input").innerHTML = list ;
    var flag = true

    while(flag==true){
        var count = 0
        var possible_combinations = 0

        //we want to takes the absolute value of an element in the list[i]
        //with all the other elements list[x], so we do the double
        //loops below:
        for (i = 0; i < list.length; i++) {
            possible_combinations = list.length * (list.length-1)

            for (x = 0; x < list.length; x++) {
                //we exclude case where the element list[i] is the same as list[x]:
                if(list[i]!=list[x]){
                    var absolute_value = Math.abs(list[i]-list[x])
                    //if the new particles created above is not 0
                    //or not in the list, we add it to the list:
                    if(absolute_value != 0 && !(list.includes(absolute_value))){
                        list.push(absolute_value)
                    }else{
                       //the code below is to help count
                       //how many times a new particle is created
                       count+=1
                    }
                }
            }
        }
        //if the number of new particle that cannot
        //be created equal to total possible combinations,
        //this means that the list at this time
        //is the final list and cannot create
        //any new kind of particles.
        if(count==possible_combinations){
            flag = false
        }
    }

    //we take the length of the list at this state:
    console.log(list.length)
    var length = list.length.toString()

    document.getElementById("output").innerHTML = length + " particles";


}




```

##### Testing:

![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-05-18%20at%2016.55.07.png)
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-05-18%20at%2016.54.51.png)
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-05-18%20at%2016.54.32.png)
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-05-18%20at%2016.53.54.png)
