<!DOCTYPE html>
<html lang="en">
<head>
    <title>Leaderboard-Confucius Institute</title>
    <meta charset="utf-8">

    <!-- CSS Files -->
    <link rel="stylesheet" type="text/css" href="css/reset.css">
    <link rel="stylesheet" type="text/css" href="css/animate.css">
    <link rel="stylesheet" type="text/css" href="css/main.css">
    <link rel="stylesheet" type="text/css" href="css/main_2.css">  <!--customized-->
    <link rel="stylesheet" href="http://cdn.bootcss.com/bootstrap/3.3.0/css/bootstrap.min.css">

    <!-- Javascript Files -->
    <script type="text/javascript" src="js/jquery.js"></script>
    <script type="text/javascript" src="js/slider.js"></script>
    <script type="text/javascript" src="js/wow.js"></script>
    <script type="text/javascript" src="js/main.js"></script>
    <script type="text/javascript" src="js/teacher_home.js"></script>  <!--customized -->
    <script src="http://cdn.bootcss.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>
</head>

<body onload = "check_view_option()">

<!-- check whether the user logged in -->
<?php
if(!isset($_SESSION['user_id'])){
    echo "no id"; //test
//    $home_url = 'index.php';
//    header('Location: '.$home_url);
}
else{
    echo "id";  //test
//    $home_url = 'teacher_home.php';
//    header('Location: '.$home_url);
}
?>
<!-- end check -->

<!-- header Section -->
<header>
    <div class="container">
        <!-- Logo  -->
        <a href="#" class="logo">
            <img src="img/logo.png" alt="Logo Img"/>
        </a>
        <!-- Navigation Menu  -->
        <nav>
            <ul class="nav navbar-nav">
                <li><a href="#" class="selected">Home</a> </li>
                <li><a href="teacher_analysis.php" target="_self">Analysis</a> </li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                        User<b class="caret"></b>
                    </a>
                    <ul class="dropdown-menu">
                        <li><a href="teacher_user.php#" target="_self">Settings</a></li>
                        <li><a href="logout.php" target="_self">Log out</a></li>
                    </ul>
                </li>
            </ul>
        </nav>
    </div>
</header>
<!-- end header -->

<!-- Ranking View -->
<section class="services container sec_rank">
    <div class="table_rank_1">
        <!-- option -->
        <br/>
        <div class="table_rank_2">
            <!--refresh the result according to the selected item-->
            <label style="font-size:40px;color: #575856;">
                Leaderboard
            </label>
            <br/><br/><br/>
            <!-- Continent 洲 -->
            <label for="view_level_continent">Continent:</label>
            <select id="view_level_continent" onchange="view_option_changed_continent()" style="width:100px;">
                <option>all</option>
                <option selected>Europe</option>
                <option>America</option>
                <option>Africa</option>
                <option>Oceania</option>
                <option>Asia</option>
            </select>
            <label>&ensp; &ensp;</label>
            <!-- Country/Region 国家和地区 -->
            <label for="view_level_country">Country/Region:</label>
            <select id="view_level_country" onchange="view_option_changed_country()" style="width:120px;">
                <option selected>all</option>
            </select>
            <label>&ensp; &ensp;</label>
            <!-- City 城市-->
            <label for="view_level_city">City:</label>
            <select id="view_level_city" onchange="view_option_changed_city()">
                <option selected>all</option>
            </select>
            <label>&ensp; &ensp;</label>
            <!-- time range 总，每日，每周，每月-->
            <label for="view_time">range:</label>
            <select id="view_time" onchange="view_option_changed_time()" style="width:80px;">
                <option selected>all time</option>
                <option>daily</option>
                <option>weekly</option>
                <option>monthly</option>
            </select>
        </div>
        <br/><br/>
        <!-- end option -->

        <!--result table-->
        <!-- table -->
        <div id="table_home_my">
            <table class="table_rank_4">
                <thead>
                <tr style="background-color: transparent;border-bottom: 2px solid #626361;">
                    <th style="text-align: center">Ranking</th>
                    <th style="text-align: center">Student</th>
                    <th style="text-align: center">CI</th>
                    <th style="text-align: center">City</th>
                    <th style="text-align: center">Country/Region</th>
                    <th style="text-align: center">Score</th>
                    <th style="text-align: center">status</th>
                </tr>
                </thead>
            </table>
        </div>
        <div id="table_home_list">
            <table class="table_rank_3">
                <tbody id="home_list">
                </tbody>
            </table>
        </div>
        <!-- end result -->

        <!--  pager  -->
        <div class="table_rank_2">
            <ul class="pager">
                <li class="previous"><a href="#" onclick="previous_page()">&larr; Previous</a></li>
                <li><a href="#" onclick="view_button_backTop10()">Back to Top 10</a></li>
                <li class="next"><a href="#" onclick="next_page()">Next &rarr;</a></li>
            </ul>
        </div>
        <!-- end page -->
    </div>
</section>
<!-- end -->

<!-- Footer Section -->
<footer class="clearfix">
    <div class="container">

        <!-- Copyrights  -->
        <div class="copyright animated wow fadeInUp">
            <img src="img/footer_logo.png" alt="logo img2" class="footer_logo">
            <p>© 2018 copyright Aberdeen-Wuhan JRI- All rights reserved. This Site.</p>
        </div>

        <div class="footer_links">

            <!-- About Links  -->
            <div class="about columns animated wow fadeInRight" data-wow-delay=".3s">
                <h3 class="columns_title">About</h3>
                <ul>
                    <li>
                        <a href="">Leaderboard</a>
                    </li>
                    <li>
                        <a href="">Aberdeen-Wuhan JRI</a>
                    </li>
                    <li>
                        <a href="">Disclaimer</a>
                    </li>
                </ul>
            </div>

            <!-- Address  -->
            <div class="address columns animated wow fadeInRight" data-wow-delay=".4s">
                <h3 class="columns_title">Address</h3>
                <p>xx  xx</p>
                <p>Aberdeen, UK xxxxxxx</p>
                <p class="phone">(000) 000-0000</p>
            </div>

        </div>

    </div>

</footer><!-- end footer -->


</body>

</html>