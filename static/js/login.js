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

    $.post("/log_reg/Login", {username: username, password: password},
        function (data)
        {
            var login_req = JSON.parse(data);
            console.log(login_req);
            if (login_req['code'] == 'True')
            {
                sessionStorage.setItem("username", username);
                sessionStorage.setItem("user_role", login_req['user_role']);
                home_url = '/';
                if(login_req['user_role']==0)
                    var home_url = 'teacher_home';
                else if(login_req['user_role']==1)
                    var home_url = 'student_home';
                window.location.href = home_url;
            }
            else
            {
                alert('Wrong user_id/password! Please try again!');
            }
        })
            .error(function (e)
                {
                    alert('Wrong user_id/password! Please try again!');
                });
}

function visitor_login(){
    window.location.href='visitor_home';
}
