### Quiz 31


#### Solution



##### Codes:

###### HTML file
```.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <script src="crewmember.js"></script>
    <title>Crew Member</title>
</head>

<body>

<h1>Quiz 31</h1>
<input type = "button" onclick = "ActivateFunction()" value = "Activate function">

<h5>Input:</h5>
<p>["Green voted for Black", "Black voted for Blue", "Brown voted for Blue", "Blue voted for Black", "Cyan skipped voting", "Lime voted for Black"]</p>

<h5>Output:</h5>
<p id="output"></p>

</body>


</html>
```

###### Javascript file
```.js
//TASK: There is a saboteur on the ship! An emergency meeting is called. Each crewmember may 
// vote for who they believe is the guilty party. At the end of the meeting, if one crewmember 
// receives more votes than any other, and more than the number of votes skipped, that person is 
// ejected from the ship

function ActivateFunction() {
    // variable for the string
    var vote_input = ["Green voted for Black", "Black voted for Blue", "Brown voted for Blue", "Blue voted for Black", "Cyan skipped voting", "Lime voted for Black"]
    // var vote_input = ["Green skipped voting", "Black skipped voting", "Brown skipped voting", "Blue skipped voting", "Cyan skipped voting", "Lime skipped voting"]
    // var vote_input = ["Green voted for Black", "Black voted for Green", "Brown voted for Blue", "Blue voted for Brown", "Cyan voted for Lime", "Lime voted for Cyan"]
    var vote_counted = [] //to record all votes name of all members got
    var vote_skipped = 0
    var voted_num_counted = [] //to record all votes number of all members got
    var index_of_guilty_member = 0

    // variable for a blank list
    var members = [] // to get all the members who voted
    var members_who_got_voted = []


    //loop through all the element in the var input to split each element (string)
    for (i = 0; i < vote_input.length; i++) {
        //split the string and get [0] of the string

        var member = vote_input[i].split(" ")[0]


        //check if the element above is in the blank list,
        if (members.includes(member)) {

        } else {//if members didn't exist
            //add it to the blank list
            members.push(member)

            //proceed to start evaluating votes:


            var member_who_is_voted = vote_input[i].split(" ")[vote_input[i].split(" ").length - 1]

            //check if the element above is in the blank list,
            if (members_who_got_voted.includes(member_who_is_voted)) {

            } else {
                members_who_got_voted.push(member_who_is_voted)
            }

            console.log(members_who_got_voted)

            if ((vote_input[i].split(" ")[1] === "skipped")) {
                vote_skipped += 1
            } else if ((vote_input[i].split(" ")[1] == "voted")) {
                vote_counted.push(member_who_is_voted)
                console.log(vote_counted)

            }

        }


    }



    for (a = 0; a < members_who_got_voted.length; a++) {
        var num = 0

        for (b = 0; b < vote_counted.length; b++) {
            if (vote_counted[b] == members_who_got_voted[a]) {
                num += 1
            }
        }


        voted_num_counted.push(num)

    }
    console.log(voted_num_counted)

    //All the code below determine the biggest vote number in the list voted_num_counted:
    var biggest_value = 0

    for (c = 0; c < voted_num_counted.length; c++) {

        if (voted_num_counted[c] > biggest_value) {
            biggest_value = voted_num_counted[c]
        }

    }

    //All the code below counts how many time a biggest vote number appears in the list voted_num_counted.
    //this is to use to determine if the votes of every member is the same or not:
    var num_biggest_value = 0

    for (e = 0; e < voted_num_counted.length; e++) {

        if (voted_num_counted[e] == biggest_value) {
            num_biggest_value += 1
        }

    }


    if (num_biggest_value == voted_num_counted.length){
        console.log(" No one was ejected. (Tie)")
        document.getElementById("output").innerHTML = " No one was ejected. (Tie)" ;
    }else if (vote_skipped == members.length){
        console.log(" No one was ejected. (Skipped)")
        document.getElementById("output").innerHTML = " No one was ejected. (Skipped)" ;

    }else if (num_biggest_value == 1) {
        //the for loop below get the index of the member with the highest vote numer in the list voted_num_counted
        for (d = 0; d < voted_num_counted.length; d++) {
            if (voted_num_counted[d] == biggest_value) {
                index_of_guilty_member = d
            }
        }

        console.log(members_who_got_voted[index_of_guilty_member] + " was ejected.")
        document.getElementById("output").innerHTML = members_who_got_voted[index_of_guilty_member] + " was ejected." ;
    }

    console.log("Number of skipped vote:", vote_skipped)



}






```

##### Testing:

![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-04-13%20at%2018.00.11.png)

![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-04-13%20at%2018.00.30.png)

![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-04-13%20at%2018.00.57.png)
