### Quiz 34


#### Solution



##### Codes:

###### HTML file
```.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <script src="Cities.js"></script>

    <title>Cities</title>
</head>

<body>
<h1>Quiz 34</h1>
<input type = "button" onclick = "ActivateFunction()" value = "Activate function">

<h5>Input of city roads' direction:</h5>
<p id="input"></p>



<h5>Output/ Amount of cities that can be reached from city 0:</h5>
<p id="output"></p>

</body>
</html>

```

###### Javascript file
```.js

//TASK: There are N cities in a row, numbered from 0 to N-1
//There are one-way roads going from left to right between cities
//For each city, you know where the road starts (provided with a number of the city from the
// road_direction arrays), or if there is no road (-1).
//Output the number of cities that can be reached from city 0 using the road.

function ActivateFunction() {

    // var road_directions = []
    //
    // for (let i = -1; i<999; i++) {
    //     road_directions.push(i)
    // }



    //these codes below were for testing:
    // var road_directions = [-1,0,-1,1,2,3]
    // var road_directions = [-1,0]
    // var road_directions = [-1,0,1,2,3,0,2,6,7,8]
    // var road_directions = [1,-1,1,2,3,4,5,6,7,8,9]
    var road_directions = [-1,0,-1,1,2,3]

    console.log(road_directions)
    document.getElementById("input").innerHTML = road_directions ;

    //As cities are connected one way, every city that are connected to 0 could
    //provide connection path from 0 to other cities. This is why
    //we need to create a list to store all the cities that are connected to 0
    //for example, if city 1 is connected with city 0 and city 2 is connected with city 1,
    //city 2 is also connected with city 0. This is why we need to stores city 1 in a list
    //because even when city 2 is not connected directly to city 0, if it is connected with
    //city 1, it could still be reached from city 0:
    var cities_connect_with_city0 = []

    //a for loop check the direction of every city, if it connects with 0 or belongs
    //in the list above, we push the city name (which is the index) into the list itself.
    for(i = 0; i < road_directions.length; i++){
        if (road_directions[i] == 0 || cities_connect_with_city0.includes(road_directions[i])){
            cities_connect_with_city0.push(i)
        }
    }

    var num_of_cities_from_city0 = cities_connect_with_city0.length

    console.log(num_of_cities_from_city0)
    document.getElementById("output").innerHTML = num_of_cities_from_city0 ;

}




```

##### Testing:

![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-04-23%20at%2016.04.02.png)
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-04-23%20at%2016.03.48.png)
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-04-23%20at%2016.03.37.png)
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-04-23%20at%2016.03.26.png)
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-04-23%20at%2016.03.16.png)
![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-04-23%20at%2016.02.42.png)
