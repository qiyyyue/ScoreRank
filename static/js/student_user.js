function check_setting_option(set_option) {
    document.getElementById("item_bind").style.display ='none';
    document.getElementById("item_profile").style.display ='none';
    document.getElementById("item_passwd").style.display ='none';
    if(set_option==0){
        $('#set_0').addClass("li_item_selected").siblings().removeClass("li_item_selected");
        bind_init();
        document.getElementById("item_bind").style.display ='block';
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

function bind_init() {
    //duolingo
    $('#collapse_duo').collapse('hide');
    $('#account_duo').val('');
    $('#passwd_duo').val('');

    //get bingding status from back-end
    //.........
    var status_duo = false;
    if(status_duo==true){
        document.getElementById("bind_status_duo").innerHTML = "Bound";
        document.getElementById("bind_edit_duo").innerHTML = "Change";
    }
    else{
        document.getElementById("bind_status_duo").innerHTML = "Not Bound";
        document.getElementById("bind_edit_duo").innerHTML = "Bind Now";
    }

    //others
    $('#collapse_mem').collapse('hide');
    $('#collapse_he').collapse('hide');
    $('#collapse_sk').collapse('hide');
}

function Profile_init() {
    //get personal information from back-end
    //...............

    var jsonData = {
        c1: "Daisy Julie",
        c2: "Daisy Julie",
        c3: "28855",
        c4: "2005-12-18",
        c5: "1",
        c6: "The Confucius Institute of the University of Aberdeen",
        c7: "Aberdeen",
        c8: "UK"
    };
    document.getElementById("prof_username").innerHTML = jsonData.c1;
    document.getElementById("prof_name").innerHTML = jsonData.c2;
    document.getElementById("prof_id").innerHTML = jsonData.c3;
    document.getElementById("prof_birth").innerHTML = jsonData.c4;
    document.getElementById("prof_class").innerHTML = jsonData.c5;
    document.getElementById("prof_ci").innerHTML = jsonData.c6;
    document.getElementById("prof_city").innerHTML = jsonData.c7;
    document.getElementById("prof_cr").innerHTML = jsonData.c8;

    $('#prof_edit_username').val('');
    $('#collapse_username').collapse('hide');
}

function Password_init(){
    $('#collapse_passwd').collapse('hide');
    $('#passwd_value_new').val('');
    $('#passwd_value_confirm').val('');
}

function bind_app(app,flag){
    var msg = "Are you sure to bind the Account?";

    if(app==0){
        if(flag==true){
            var account = $('#account_duo').val();
            var passwd = $('#passwd_duo').val();
            if(account!='' && passwd!='') {
                if (confirm(msg) == true) {

                    //submit to back-end
                    //........
                    var return_flag = false;
                    if(return_flag==true){
                        $('#account_duo').val('');
                        $('#passwd_duo').val('');
                        $('#collapse_duo').collapse('hide');
                        document.getElementById("bind_status_duo").innerHTML = "Bound";
                        document.getElementById("bind_edit_duo").innerHTML = "Change";
                        alert('Bind successfully!');
                    }
                    else{
                        alert('Fail to bind! Please check your account and password.');
                    }
                }
                else {
                    $('#account_duo').val('');
                    $('#passwd_duo').val('');
                }
            }
            else{
                alert('The Account and Password cannot be empty!');
            }
        }
        else{
            $('#account_duo').val('');
            $('#passwd_duo').val('');
        }
    }
}

function edit_username(flag) {
    if(flag==true){
        var new_username = $('#prof_edit_username').val();
        var msg = "Are you sure to change the user name for display?";

        //check the legality of new_username
        var re = /^[a-zA-Z]\w{4,16}$/ig;
        if(!re.test(new_username)){
            alert('1. Start with a letter.\n2. Only consist of letters, numbers, dots, minus signs or underscores.\n3. Length between 4~16.')
        }
        else{
            if(confirm(msg)==true){
                //submit to back-end
                //..........

                $('#prof_edit_username').val('');
                $('#collapse_username').collapse('hide');
                document.getElementById("prof_username").innerHTML = new_username;
                alert('Change Successfully!');
            }
        }
    }
    else{
        $('#prof_edit_username').val('');
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

            $('#passwd_value_new').val('');
            $('#passwd_value_confirm').val('');
            $('#collapse_passwd').collapse('hide');
            alert("Change successfully!")
        }
    }
    //cancel
    if(flag==false){
        $('#passwd_value_new').val('');
        $('#passwd_value_confirm').val('');
    }
}