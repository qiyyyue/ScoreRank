function check_login()
{
    var username = $("#user_id").val();
    var password = $("#password").val();
    if (  username == "" )
    {
        alert("Please entering the user ID number.");
        return;
    }
    if (  password == "" )
    {
        alert("Please entering the password.");
        return;
    }

    alert("111");
    $.post("/user_info/login", {username: username, password: password},
        function (data)
        {
            alert("true");
            var login_req = JSON.parse(data);
            if (login_req['code'] == 'True')
            {
                sessionStorage.setItem("username", username);
                sessionStorage.setItem("user_role", login_req['user_role']);
                if(login_req['user_role']==0)
                    var home_url = 'teacher_home.php';
                else if(login_req['user_role']==1)
                    var home_url = 'student_home.php';
                window.location.href = home_url;
            }
            else
            {

            }
        })
            .error(function (e)
                {

                });

}

function visitor_login(){
    window.location.href='visitor_home';
}
