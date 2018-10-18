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
    <link rel="stylesheet" type="text/css" href="css/main_4.css">  <!--customized-->
    <link rel="stylesheet" href="http://cdn.bootcss.com/bootstrap/3.3.6/css/bootstrap.min.css">

    <!-- Javascript Files -->
    <script type="text/javascript" src="js/jquery.js"></script>
    <script type="text/javascript" src="js/slider.js"></script>
    <script type="text/javascript" src="js/wow.js"></script>
    <script type="text/javascript" src="js/main.js"></script>
    <script type="text/javascript" src="js/teacher_user.js"></script>  <!--customized -->
    <script src="http://cdn.bootcss.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
</head>

<body onload="check_setting_option(0)">

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
                <li><a href="teacher_analysis.php#" target="_self">Analysis</a> </li>
                <li class="dropdown">
                    <a href="#" style="color:#53a7ff;font-weight: bold;" class="dropdown-toggle" data-toggle="dropdown">
                        User<b class="caret"></b>
                    </a>
                    <ul class="dropdown-menu">
                        <li><a href="#">Settings</a></li>
                        <li><a href="logout.php" target="_self">Log out</a></li>
                    </ul>
                </li>
            </ul>
        </nav>
    </div>
</header>
<!-- end header -->

<!-- Settings Section -->
<div class="container" id="user_container">
    <!-- begin left -->
    <div class="user_left">
        <label class="left_label">Settings</label>
        <ul id="user_nav">
            <li class="nav_li clearfix" onclick="check_setting_option(0)"  id="set_0">
                <div class="li_icon"><img src="img/icon_1.png"></div>
                <div class="li_item">APP Weight</div>
            </li>
            <li class="nav_li clearfix" onclick="check_setting_option(1)"  id="set_1">
                <div class="li_icon"><img src="img/icon_8.png"></div>
                <div class="li_item">Profile</div>
            </li>
            <li class="nav_li clearfix" onclick="check_setting_option(2)"  id="set_2">
                <div class="li_icon"><img src="img/icon_10.png"></div>
                <div class="li_item">Password</div>
            </li>
        </ul>
    </div>
    <!-- end left -->
    <!-- begin right -->
    <div class="user_right">
        <!-- weight -->
        <div class="right_item" id="item_weight">
            <div class="strip_title">Weight Values</div>
            <div class="strip_note">The higher the value, the higher the importance.</div>

            <!-- Duolingo -->
            <div class="panel panel-default">
                <div class="panel-heading">
                    <table class="strip_table">
                        <tbody>
                        <td class="strip_name">
                            <img src="img/app_icon_duo.jpg" class="app_icon">
                            Duolingo</td>
                        <td id="weight_status_duo" class="status"></td>
                        <td class="edit">
                            <a data-toggle="collapse" href="#collapse_duo">Edit</a>
                        </td>
                        </tbody>
                    </table>
                </div>
                <div id="collapse_duo" class="panel-collapse collapse in">
                    <div class="panel-body">
                        <table class="edit_content_table">
                            <tbody>
                            <td style="text-align: center;">
                                Weight:
                                &nbsp;&nbsp;
                                <input id="weight_value_duo" type="number" min="0" max="10">
                            </td>
                            </tbody>
                        </table>
                        <table class="edit_content_table">
                            <tbody>
                            <td style="text-align: right; padding-right: 15px;">
                                <button class="st_list_btn" onclick="edit_weight(0)">Submit</button>
                            </td>
                            <td style="text-align: left; padding-left: 15px;">
                                <button class="st_list_btn" data-toggle="collapse" href="#collapse_duo">Cancel</button>
                            </td>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
            <!-- end Duolingo -->

            <!-- Memrize -->
            <div class="panel panel-default">
                <div class="panel-heading">
                    <table class="strip_table">
                        <tbody>
                        <td class="strip_name">
                            <img src="img/app_icon_mem.jpg" class="app_icon">
                            Memrize</td>
                        <td id="weight_status_mem" class="status">Developing</td>
                        <td class="edit">
                            <a data-toggle="collapse" href="#collapse_mem">Developing</a>
                        </td>
                        </tbody>
                    </table>
                </div>
                <div id="collapse_mem" class="panel-collapse collapse in">
                    <div class="panel-body">
                        The developers are working on it.
                    </div>
                </div>
            </div>
            <!-- end Memrize -->

            <!-- Hello Chinese -->
            <div class="panel panel-default">
                <div class="panel-heading">
                    <table class="strip_table">
                        <tbody>
                        <td class="strip_name">
                            <img src="img/app_icon_he.jpg" class="app_icon">
                            Hello Chinese</td>
                        <td id="weight_status_he" class="status">Developing</td>
                        <td class="edit">
                            <a data-toggle="collapse" href="#collapse_he">Developing</a>
                        </td>
                        </tbody>
                    </table>
                </div>
                <div id="collapse_he" class="panel-collapse collapse in">
                    <div class="panel-body">
                        The developers are working on it.
                    </div>
                </div>
            </div>
            <!-- end Hello Chinese -->

            <!-- Chinese Skill -->
            <div class="panel panel-default">
                <div class="panel-heading">
                    <table class="strip_table">
                        <tbody>
                        <td class="strip_name">
                            <img src="img/app_icon_sk.png" class="app_icon">
                            Chinese Skill</td>
                        <td id="weight_status_sk" class="status">Developing</td>
                        <td class="edit">
                            <a data-toggle="collapse" href="#collapse_sk">Developing</a>
                        </td>
                        </tbody>
                    </table>
                </div>
                <div id="collapse_sk" class="panel-collapse collapse in">
                    <div class="panel-body">
                        The developers are working on it.
                    </div>
                </div>
            </div>
            <!-- end Chinese Skill -->
        </div>
        <!-- end weight -->

        <!-- Profile -->
        <div class="right_item" id="item_profile">
            <div class="strip_title">My Profile</div>
            <div class="strip_note">Some information is not editable.</div>

            <!-- Name -->
            <div class="panel panel-default">
                <div class="panel-heading">
                    <table class="strip_table">
                        <tbody>
                        <td class="strip_name">
                            Name</td>
                        <td id="prof_name" class="status"></td>
                        <td class="edit">
                        </td>
                        </tbody>
                    </table>
                </div>
            </div>
            <!-- end Name -->

            <!-- ID -->
            <div class="panel panel-default">
                <div class="panel-heading">
                    <table class="strip_table">
                        <tbody>
                        <td class="strip_name">
                            Teacher ID</td>
                        <td id="prof_id" class="status"></td>
                        <td class="edit">
                        </td>
                        </tbody>
                    </table>
                </div>
            </div>
            <!-- end ID -->

            <!-- class -->
            <div class="panel panel-default">
                <div class="panel-heading">
                    <table class="strip_table">
                        <tbody>
                        <td class="strip_name">
                            Class</td>
                        <td id="prof_class" class="status"></td>
                        <td class="edit">
                        </td>
                        </tbody>
                    </table>
                </div>
            </div>
            <!-- end class -->

            <!-- CI -->
            <div class="panel panel-default">
                <div class="panel-heading">
                    <table class="strip_table">
                        <tbody>
                        <td class="strip_name">
                            Confucius Institute</td>
                        <td id="prof_ci" class="status"></td>
                        <td class="edit">
                        </td>
                        </tbody>
                    </table>
                </div>
            </div>
            <!-- end CI -->

            <!-- city -->
            <div class="panel panel-default">
                <div class="panel-heading">
                    <table class="strip_table">
                        <tbody>
                        <td class="strip_name">
                            City</td>
                        <td id="prof_city" class="status"></td>
                        <td class="edit">
                        </td>
                        </tbody>
                    </table>
                </div>
            </div>
            <!-- end city -->

            <!-- country/region -->
            <div class="panel panel-default">
                <div class="panel-heading">
                    <table class="strip_table">
                        <tbody>
                        <td class="strip_name">
                            Country/Region</td>
                        <td id="prof_cr" class="status"></td>
                        <td class="edit">
                        </td>
                        </tbody>
                    </table>
                </div>
            </div>
            <!-- end city -->

        </div>
        <!-- end Profile -->

        <!-- Passwd -->
        <div class="right_item" id="item_passwd">
            <div class="strip_title">Change Password</div>
            <br>
            <div class="panel panel-default">
                <div class="panel-heading">
                    <table class="strip_table">
                        <tbody>
                        <td class="strip_name">
                            Password</td>
                        <td class="status">************</td>
                        <td class="edit">
                            <a data-toggle="collapse" href="#collapse_passwd">Reset</a>
                        </td>
                        </tbody>
                    </table>
                </div>
                <div id="collapse_passwd" class="panel-collapse collapse in">
                    <div class="panel-body">
                        <table class="edit_content_table">
                            <tbody>
                                <td style="text-align: right; padding-right: 5px;">
                                    New Password:
                                </td>
                                <td style="text-align: left; padding-left: 5px;">
                                    <input id="passwd_value_new" type="password">
                                </td>
                            </tbody>
                        </table>
                        <table class="edit_content_table">
                            <tbody>
                            <td style="text-align: right; padding-right: 5px;">
                                Confirm:
                            </td>
                            <td style="text-align: left; padding-left: 5px;">
                                <input id="passwd_value_confirm" type="password">
                            </td>
                            </tbody>
                        </table>
                        <table class="edit_content_table">
                            <tbody>
                            <td style="text-align: right; padding-right: 15px;">
                                <button class="st_list_btn" onclick="edit_passwd(true)">Submit</button>
                            </td>
                            <td style="text-align: left; padding-left: 15px;">
                                <button class="st_list_btn" onclick="edit_passwd(false)" data-toggle="collapse" href="#collapse_passwd">Cancel</button>
                            </td>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
        <!-- end Passwd -->
    </div>
    <!-- end right -->
</div>
<!-- end Settings -->


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