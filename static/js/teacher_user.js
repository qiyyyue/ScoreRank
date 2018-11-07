function check_login()
{
    if (!sessionStorage.getItem('username'))
    {
        window.location.href = '/';
    }
}

function check_setting_option(set_option) {
    document.getElementById("item_weight").style.display ='none';
    document.getElementById("item_profile").style.display ='none';
    document.getElementById("item_passwd").style.display ='none';
    if(set_option==0){
        $('#set_0').addClass("li_item_selected").siblings().removeClass("li_item_selected");
        weight_init();
        document.getElementById("item_weight").style.display ='block';
    }
    if(set_option==1){
        $('#set_1').addClass("li_item_selected").siblings().removeClass("li_item_selected");
        Profile_init();
        document.getElementById("item_profile").style.display ='block';
    }
    if(set_option==2){
        $('#set_2').addClass("li_item_selected").siblings().removeClass("li_item_selected");
        Password_init();
        document.getElementById("item_passwd").style.display ='block';
    }
}

function weight_init() {
    //duolingo
    $('#collapse_duo').collapse('hide');

    //get weight from back-end
    //.........
    var weight = 7;

    $.ajaxSetup({
        async : false
    });

    try
    {
        $.post("/tc_setting/TcGetWight", {username: sessionStorage.getItem('username'), app_id: 1},
            function (data)
            {
                var req_data = JSON.parse(data);
                if (req_data['code'] == 'True')
                {
                    weight = req_data['weight'];
                    // console.log(user_self_info);
                }
                else
                {
                    // console.log('false');
                }
            });
    }
    catch (e)
    {
        // console.log("wrong");
        // console.log(e.toString());
        // alert('Fail to bind! Please check your account and password.');
    }


    document.getElementById("weight_status_duo").innerHTML = weight;
    document.getElementById("weight_value_duo").value = weight;

    //others
    $('#collapse_mem').collapse('hide');
    $('#collapse_he').collapse('hide');
    $('#collapse_sk').collapse('hide');

}

function Profile_init() {
    //get personal information from back-end
    //...............

    var user_self_info = {};

    $.ajaxSetup({
        async : false
    });

    try
    {
        $.post("/tc_setting/TcGetSelfInfo", {username: sessionStorage.getItem('username')},
            function (data)
            {
                var req_data = JSON.parse(data);
                if (req_data['code'] == 'True')
                {
                    user_self_info = req_data['self_info'];
                    // console.log(user_self_info);
                }
                else
                {
                    // console.log('false');
                }
            });
    }
    catch (e)
    {
        // console.log("wrong");
        // console.log(e.toString());
        // alert('Fail to bind! Please check your account and password.');
    }

    document.getElementById("prof_name").innerHTML = user_self_info['teacher_name'];
    document.getElementById("prof_id").innerHTML = user_self_info['teacher_number'];
    document.getElementById("prof_class").innerHTML = user_self_info['course_list'];
    document.getElementById("prof_ci").innerHTML = user_self_info['CI'];
    document.getElementById("prof_city").innerHTML = user_self_info['city'];
    document.getElementById("prof_cr").innerHTML = user_self_info['continent'];

}

function Password_init(){
    $('#collapse_passwd').collapse('hide');
    $('#passwd_value_new').val('');
    $('#passwd_value_confirm').val('');
}

function edit_weight(app) {
    var msg = "Are you sure to change the weight?";
    if(app==0){
        if (confirm(msg)==true){
            var weight_new = document.getElementById("weight_value_duo").value;
            var weight_old = document.getElementById("weight_status_duo").innerHTML;

            if(weight_new==weight_old){
                alert("You choose the same value!")
            }
            else{
                //submit weight_new of (app=0) to back-end.
                //.......

                $.ajaxSetup({
                    async : false
                });
                try
                {
                    $.post("/tc_setting/TcSetWight", {username: sessionStorage.getItem('username'), app_id: 1, weight: weight_new},
                        function (data)
                        {
                            var req_data = JSON.parse(data);
                            if (req_data['code'] == 'True')
                            {
                                document.getElementById("weight_status_duo").innerHTML = weight_new;
                                $('#collapse_duo').collapse('hide');
                                alert('Set weight Successfully!');
                            }
                            else
                            {
                                alert('Set weight Failly! Please try again later!');
                            }
                        });
                }
                catch (e)
                {
                    alert('Set weight Failly! Please try again later!');
                }


                //document.getElementById("weight_status_duo").innerHTML = weight_new;
                // $('#collapse_duo').collapse('hide');
                //alert("Submit successfully!");
            }
        }
        else{
            $('#collapse_duo').collapse('hide');
        }
    }
}

function edit_passwd(flag) {
    //submit
    if(flag==true){
        var p1 = $('#passwd_value_new').val();
        var p2 = $('#passwd_value_confirm').val();

        //check the legality of p1
        var regu = "^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,18}$";
        var re = new RegExp(regu);
        if (!re.test(p1)) {
            alert('The password must contain Letters and Numbers with the length 6~18.');
        }
        else if (p1 != p2){
            alert('The two passwords you entered do not match!');
        }
        else{
            //submit to back-end
            //...............

            $.ajaxSetup({
                    async : false
                });

            try
            {
                $.post("/tc_setting/TcChangePassword", {username: sessionStorage.getItem('username'), password: p1},
                    function (data)
                    {
                        var req_data = JSON.parse(data);
                        if (req_data['code'] == 'True')
                        {
                            alert('Change Successfully!');
                        }
                        else
                        {
                            alert('Change Failly! Please try again later!');
                        }
                    });
            }
            catch (e)
            {
                alert('Change Failly! Please try again later!');
            }

            $('#passwd_value_new').val('');
            $('#passwd_value_confirm').val('');
            $('#collapse_passwd').collapse('hide');
            //alert("Change successfully!")
        }
    }
    //cancel
    if(flag==false){
        $('#passwd_value_new').val('');
        $('#passwd_value_confirm').val('');
    }
}