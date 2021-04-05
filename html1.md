
#### My first HTML website "About me":

![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-04-05%20at%2017.06.39.png)

##### HTML file:

```.html

<!DOCTYPE html>
<html lang="en">

<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
    <meta charset="UTF-8">
    <link rel="stylesheet" href="index.css">
    <title>KienLeTrung</title>
</head>

<body>




    <img src="jet5.jpg" id="image">

    <div >
        <div class="top-left">
            <h1 class="empha">Kien Le Trung</h1>
        </div>

        <div class="top-left-1">
            <h2>Hi. I'm the CEO of Upchanges. I'm creating the world's best knowledge app Apollo. I read book.
            I admire Jeff Bezos.</h2>
        </div>

            <img src="kien.png" id="profile">

    </div>





</body>

</html>

```

##### CSS file:

```.css

h1{
    font-size: 100px;
}


.container {
    position: relative;
    text-align: center;
    color: black;
    alignment: center;
    width: 100%;
    max-width: 1800px;
    height:auto;
    max-height:850px;
}

#image{
    alignment: center;
    width: 100%;
    max-width: 1800px;
    height:100%;
    max-height:850px;

}



.centered {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

#profile{

    position: absolute;
    width: 100%;
    max-width:100px;
    height:auto;
    max-height: 100px;
    top: 40%;
    left: 47%;
}


.top-left {
    position: absolute;
    top: 8px;
    left: 16px;
}

.top-left-1 {
    position: absolute;
    top: 270px;
    left: 16px;
    width: 650px;
    word-wrap: break-word;
    text-align: left;
}

.empha{
    color: white;
}

```
