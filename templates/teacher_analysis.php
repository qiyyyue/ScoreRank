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
    <link rel="stylesheet" type="text/css" href="css/main_3.css">  <!--customized-->
    <link rel="stylesheet" href="http://cdn.bootcss.com/bootstrap/3.3.6/css/bootstrap.min.css">

    <!-- Javascript Files -->
    <script type="text/javascript" src="js/jquery.js"></script>
    <script type="text/javascript" src="js/slider.js"></script>
    <script type="text/javascript" src="js/wow.js"></script>
    <script type="text/javascript" src="js/main.js"></script>
    <script type="text/javascript" src="js/teacher_analysis.js"></script>  <!--customized -->
    <script src="http://cdn.bootcss.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
    <script type="text/javascript" src="js/echarts/echarts.js"></script>  <!--echarts-->
    <script type="text/javascript" src="js/echarts/macarons.js"></script>  <!--echarts-theme-->
</head>

<body onload="check_li_option(0)">

<!-- check whether the user logged in -->
<?php
if(!isset($_SESSION['user_id'])){
    echo "no id"; //test
//    $home_url = 'index.php';
//    header('Location: '.$home_url);
}
else{
    echo "id";  //test
//    $home_url = 'student_analysis.php';
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
                <li><a href="teacher_home.php#" target="_self"  >Home</a> </li>
                <li><a href="#" class="selected">Analysis</a> </li>
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

<!-- Analysis Section -->
<div class="container" id="user_container">
    <!-- begin left -->
    <div class="user_left">
        <label class="left_label">Analysis</label>
        <ul id="user_nav">
            <li class="nav_li clearfix" onclick="check_li_option(0)"  id="li_0">
                <div class="li_icon"><img src="img/icon_2.png"></div>
                <div class="li_item">Class Ranking</div>
            </li>
            <li class="nav_li clearfix" onclick="check_li_option(1)"  id="li_1">
                <div class="li_icon"><img src="img/icon_7.png"></div>
                <div class="li_item">Student Score</div>
            </li>
        </ul>
    </div>
    <!-- end left -->

    <!-- begin right -->
    <div class="user_right">
        <!-- class ranking -->
        <div class="right_item" id="item_class_rank">
            <!--choices-->
            <div class="table_rank_2">
                <label class="title_table">Class Leaderboard</label>
                <br/><br/>
                <!-- time range 总，每日，每周，每月-->
                <label for="class_time">range:</label>
                <select id="class_time" onchange="cl_rank_changed()">
                    <option selected>all time</option>
                    <option>daily</option>
                    <option>weekly</option>
                    <option>monthly</option>
                </select>
                <label>&ensp; &ensp;</label>
                <!-- APP -->
                <label for="class_APP">Chinese Learning App:</label>
                <select id="class_APP" onchange="cl_rank_changed()">
                    <option selected>All</option>
                    <option>Duolingo</option>
                </select>
            </div>
            <!--result table-->
            <table class="table_rank_4" style="width:90%;">
                <thead>
                <tr style="background-color: transparent;border-bottom: 2px solid #626361;">
                    <th style="text-align: center">Ranking</th>
                    <th style="text-align: center">Class</th>
                    <th style="text-align: center">Teacher</th>
                    <th style="text-align: center">Average Score</th>
                    <th style="text-align: center">status</th>
                </tr>
                </thead>
            </table>
            <table class="table_rank_3" style="width:90%;">
                <tbody id="class_rank_table">
                </tbody>
            </table>
            <br/>
        </div>
        <!-- end class ranking -->

        <!-- student list -->
        <div class="right_item" id="item_st_list">
            <div class="table_rank_2">
                <label class="title_table">Student List</label>
                <br/><br/>
                <label for="class_num">choose a class:</label>
                <select id="class_num" onchange="cl_num_changed()" style="width:100px;">
                    <option selected>class 1</option>
                    <option>class 2</option>
                    <option>class 3</option>
                    <option>class 4</option>
                    <option>class 5</option>
                </select>
            </div>
            <!--student list table-->
            <table class="table_rank_4" style="width:90%;">
                <thead>
                <tr style="background-color: transparent;border-bottom: 2px solid #626361;">
                    <th style="text-align: center">Class</th>
                    <th style="text-align: center">Student ID</th>
                    <th style="text-align: center">Name</th>
                    <th style="text-align: center">Teacher</th>
                    <th style="text-align: center">Score Curve</th>
                </tr>
                </thead>
            </table>
            <table class="table_rank_3" style="width:90%;">
                <tbody id="st_list_table">
                </tbody>
            </table>
            <br/>
        </div>
        <!-- end student list -->

        <!-- student score -->
        <div class="right_item" id="item_st_score">
            <div style="float: left; margin-top: 20px;">
                <a href="#" onclick="back_st_list()">&larr; Back</a>
            </div>
            <div class="table_rank_2">
                <label class="title_table" id="st_name_title"></label>
                <br/><br/>
                <!--refresh the result according to the selected item-->
                <!-- time range 近一周，近一个月，近三个月，近六个月，近一年-->
                <label for="st_time">time:</label>
                <select id="st_time" onchange="score_chart_option()" style="width:180px;">
                    <option selected>the latest week</option>
                    <option>the latest month</option>
                    <option>the latest three months</option>
                    <option>the latest six months</option>
                    <option>the latest year</option>
                </select>
                <label>&ensp; &ensp; &ensp; &ensp;</label>
                <!-- APP -->
                <label for="st_APP">Chinese Learning App:</label>
                <select id="st_APP" onchange="score_chart_option()">
                    <option selected>All</option>
                    <option>Duolingo</option>
                </select>
                <div><br/></div>
                <div id="st_score_chart"></div>
            </div>

            <div style="float: left; margin-bottom: 20px;">
                <a href="#" onclick="back_st_list()">&larr; Back</a>
            </div>
        </div>
        <!-- end student score -->

    </div>
    <!-- end right -->

</div>
<!-- end analysis-->


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