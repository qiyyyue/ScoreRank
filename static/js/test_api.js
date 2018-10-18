

function login()
{
    var username = 'Jack';
    var password = '123456';

    $.post("/user_info/login", {email: username, password: password},
        function (data)
        {
            console.log(data);
            var login_req = JSON.parse(data);
            if (login_req['code'] == 'True')
            {
                console.log("true");
            }
            else
            {

            }
        },
        "json");
}

login();