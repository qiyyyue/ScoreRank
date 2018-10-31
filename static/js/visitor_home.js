var page_num = 0;

var continent_0 = [["All","All"]];
var continent_1 = [["All","All"],
    ["UK","All","Aberdeen","Edinburgh"],
    ["France","All","Paris","Poitiers"]];
var continent_2 = [["All","All"],
    ["the United States","All","Chicago","New York"],
    ["Canada","All","Regina","Ottawa"]];
var continent_3 = [["All","All"],
    ["Egypt","All","Cairo","Ismailia"],
    ["Kenya","All","Nairobi","Eldoret"]];
var continent_4 = [["All","All"],
    ["Australia","All","Sydney","Melbourne"],
    ["New Zealand","All","Wellington","Auckland"]];
var continent_5 = [["All","All"],
    ["Japan","All","Kyoto","Sapporo"],
    ["Korea","All","Seoul","Incheon"]];

var rank_list;

function init_rank_data(continent, country, city, period )
{
    if (sessionStorage.getItem("username"))
    {
        //
    }

    // init rank_list info
    try
    {
        $.ajaxSetup({
            async : false
        });

        $.post("/home/GetVisitorLeaderBoard", {continent: continent, country: country, city: city, period: period},
        function (data)
        {
            var req_data = JSON.parse(data);
            console.log(req_data);
            if (req_data['code'] == 'True')
            {
                rank_list = req_data['leader_board_list'];
                // self_info = req_data['self_info']
                // alert("flag_l");
                // flag_l = true;
            }
        });

        // $.post("/home/GetRank", {username: sessionStorage.getItem("username")},
        // function (data) {
        //     var req_data = JSON.parse(data);
        //     if (req_data['code'] == 'True')
        //     {
        //         my_info['rank'] = req_data['rank'];
        //         // alert("flag_r");
        //         flag_r = true;
        //     }
        // });
        //
        // $.post("/home/GetPoint", {username: sessionStorage.getItem("username")},
        // function (data) {
        //     var req_data = JSON.parse(data);
        //     if (req_data['code'] == 'True')
        //     {
        //         my_info['point'] = req_data['point'];
        //         // alert("flag_p");
        //         flag_p = true;
        //     }
        // });
    }
    catch (e)
    {
        alert(e.toString());
    }

    // view_first_page();

}

function init_data()
{
    page_num = 0;

    var continent = document.getElementById("view_level_continent");
    var country = document.getElementById("view_level_country");
    var city = document.getElementById("view_level_city");
    var continent_index = 0;
    var country_index = 0;
    var city_index = 0;

    //1. clean old
    country.innerHTML ="";
    city.innerHTML = "";

    continent[continent_index].selected = true;
    for(var i=0;i<continent_0.length;i++){
        country.add(new Option(continent_0[i][0],continent_0[i][0]));
    }
    country[country_index].selected = true;
    for(var j=1;j<continent_0[country.selectedIndex].length;j++){
        city.add(new Option(continent_0[country.selectedIndex][j]));
    }
    city[city_index].selected = true;

    var period = document.getElementById("view_time");

    // alert(continent.options[continent.selectedIndex].value);
    init_rank_data(continent.options[continent.selectedIndex].value,
        country.options[country.selectedIndex].value,
        city.options[city.selectedIndex].value,
        period.options[period.selectedIndex].value);


    //3. update result table
    document.getElementById("table_home_list").style.display='none';
    var time = document.getElementById("view_time");
    var time_index = time.selectedIndex;

    view_first_page();
}

function check_view_option(){
    page_num = 0;

    var continent = document.getElementById("view_level_continent");
    var country = document.getElementById("view_level_country");
    var city = document.getElementById("view_level_city");
    var continent_index = continent.selectedIndex;
    var country_index= country.selectedIndex;
    var city_index = city.selectedIndex;


    // init_rank_data("All", "All", "All", "All");

    //1. clean old
    country.innerHTML ="";
    city.innerHTML = "";

    // 2. add country
    if(continent_index==0)
    {//ALL
        for(var i=0;i<continent_0.length;i++){
            country.add(new Option(continent_0[i][0],continent_0[i][0]));
        }
        country[country_index].selected = true;
        for(var j=1;j<continent_0[country.selectedIndex].length;j++){
            city.add(new Option(continent_0[country.selectedIndex][j]));
        }
        city[city_index].selected = true;
    }
    if(continent_index==1)
    {//欧洲
        for(var i=0;i<continent_1.length;i++){
            country.add(new Option(continent_1[i][0],continent_1[i][0]));
        }
        country[country_index].selected = true;
        for(var j=1;j<continent_1[country.selectedIndex].length;j++){
            city.add(new Option(continent_1[country.selectedIndex][j]));
        }
        city[city_index].selected = true;
    }
    if(continent_index==2)
    {//美洲
        for (var i = 0; i < continent_2.length; i++) {
            country.add(new Option(continent_2[i][0], continent_2[i][0]));
        }
        country[country_index].selected = true;
        for(var j=1;j<continent_2[country.selectedIndex].length;j++){
            city.add(new Option(continent_2[country.selectedIndex][j]));
        }
        city[city_index].selected = true;
    }
    if(continent_index==3)
    {//非洲
        for (var i = 0; i < continent_3.length; i++) {
            country.add(new Option(continent_3[i][0], continent_3[i][0]));
        }
        country[country_index].selected = true;
        for(var j=1;j<continent_3[country.selectedIndex].length;j++){
            city.add(new Option(continent_3[country.selectedIndex][j]));
        }
        city[city_index].selected = true;
    }
    if(continent_index==4)
    {//大洋洲
        for (var i = 0; i < continent_4.length; i++) {
            country.add(new Option(continent_4[i][0], continent_4[i][0]));
        }
        country[country_index].selected = true;
        for(var j=1;j<continent_4[country.selectedIndex].length;j++){
            city.add(new Option(continent_4[country.selectedIndex][j]));
        }
        city[city_index].selected = true;
    }
    if(continent_index==5)
    {//亚洲
        for (var i = 0; i < continent_5.length; i++) {
            country.add(new Option(continent_5[i][0], continent_5[i][0]));
        }
        country[country_index].selected = true;
        for(var j=1;j<continent_5[country.selectedIndex].length;j++){
            city.add(new Option(continent_5[country.selectedIndex][j]));
        }
        city[city_index].selected = true;
    }


    var period = document.getElementById("view_time");

    // alert(continent.options[continent.selectedIndex].value);
    init_rank_data(continent.options[continent.selectedIndex].value,
        country.options[country.selectedIndex].value,
        city.options[city.selectedIndex].value,
        period.options[period.selectedIndex].value);

    //3. update result table
    document.getElementById("table_home_list").style.display='none';
    var time = document.getElementById("view_time");
    var time_index = time.selectedIndex;

    view_first_page();
}


function view_option_changed_continent(){
    var country = document.getElementById("view_level_country");
    var city = document.getElementById("view_level_city");
    country[0].selected = true;
    city[0].selected = true;

    check_view_option();
}


function view_option_changed_country(){
    var city = document.getElementById("view_level_city");
    city[0].selected = true;

    check_view_option();
}

function view_option_changed_city(){
    check_view_option();
}

function view_option_changed_time(){
    check_view_option();
}

function view_button_backTop10(){
    check_view_option();
}

function view_first_page()
{
    // for (var i = 0; i < rank_list.length; i++)
    //     alert (rank_list[i]['username']);
    // alert("rank " + my_info['rank']);
    // alert("point " + my_info['point']);

    page_num = 0;

    $('#home_list').html("");
    document.getElementById("table_home_list").style.display='none';

    // add_self_rank();

    for (var i = 0; i < 10 && i < rank_list.length; i++)
    {
        console.log(rank_list[i]);
        // alert(rank_list[i]['rank']);

        var tdRow = document.createElement('tr');
        //generate tdcell
        var tdCell = document.createElement('td');
        tdCell.innerHTML = rank_list[i]['rank'];
        tdRow.appendChild(tdCell);
        tdCell = document.createElement('td');
        tdCell.innerHTML = rank_list[i]['username'];
        tdRow.appendChild(tdCell);
        tdCell = document.createElement('td');
        tdCell.innerHTML = rank_list[i]['continent'];
        tdRow.appendChild(tdCell);
        tdCell = document.createElement('td');
        tdCell.innerHTML = rank_list[i]['country'];
        tdRow.appendChild(tdCell);
        tdCell = document.createElement('td');
        tdCell.innerHTML = rank_list[i]['city'];
        tdRow.appendChild(tdCell);
        tdCell = document.createElement('td');
        tdCell.innerHTML = rank_list[i]['point'];
        tdRow.appendChild(tdCell);
        tdCell = document.createElement('td');
        tdCell.innerHTML = rank_list[i]['status'];
        tdRow.appendChild(tdCell);
        //write tr row
        document.getElementById("home_list").appendChild(tdRow);
    }

    console.log("finished write table");
    document.getElementById("table_home_list").style.display='block';
}

function previous_page()
{
    if(page_num == 0){
        alert("It's already the first page!");
        return;
    }

    page_num = page_num - 1;

    // add_self_rank();
    $('#home_list').html("");
    document.getElementById("table_home_list").style.display='none';

    var continent = document.getElementById("view_level_continent");
    var country = document.getElementById("view_level_country");
    var city = document.getElementById("view_level_city");
    var time = document.getElementById("view_time")
    var continent_index = continent.selectedIndex;
    var country_index= country.selectedIndex;
    var city_index = city.selectedIndex;
    var time_index = time.selectedIndex;


    for (var i = page_num * 10; i < (page_num + 1)*10 && i < rank_list.length; i++)
    {
        var tdRow = document.createElement('tr');
        //generate tdcell
        var tdCell = document.createElement('td');
        tdCell.innerHTML = rank_list[i]['rank'];
        tdRow.appendChild(tdCell);
        tdCell = document.createElement('td');
        tdCell.innerHTML = rank_list[i]['username'];
        tdRow.appendChild(tdCell);
        tdCell = document.createElement('td');
        tdCell.innerHTML = rank_list[i]['continent'];
        tdRow.appendChild(tdCell);
        tdCell = document.createElement('td');
        tdCell.innerHTML = rank_list[i]['country'];
        tdRow.appendChild(tdCell);
        tdCell = document.createElement('td');
        tdCell.innerHTML = rank_list[i]['city'];
        tdRow.appendChild(tdCell);
        tdCell = document.createElement('td');
        tdCell.innerHTML = rank_list[i]['point'];
        tdRow.appendChild(tdCell);
        tdCell = document.createElement('td');
        tdCell.innerHTML = rank_list[i]['status'];
        tdRow.appendChild(tdCell);
        //write tr row
        document.getElementById("home_list").appendChild(tdRow);
    }

    document.getElementById("table_home_list").style.display='block';
}

function next_page()
{
    if (10 * (page_num + 1) >= rank_list.length)
    {
        alert("It's already the last page!");
        return;
    }


    page_num = page_num + 1;


    $('#home_list').html("");
    document.getElementById("table_home_list").style.display='none';

    var continent = document.getElementById("view_level_continent");
    var country = document.getElementById("view_level_country");
    var city = document.getElementById("view_level_city");
    var time = document.getElementById("view_time");
    var continent_index = continent.selectedIndex;
    var country_index= country.selectedIndex;
    var city_index = city.selectedIndex;
    var time_index = time.selectedIndex;

    for (var i = page_num * 10; i < (page_num + 1)*10 && i < rank_list.length; i++)
    {
        var tdRow = document.createElement('tr');
        //generate tdcell
        var tdCell = document.createElement('td');
        tdCell.innerHTML = rank_list[i]['rank'];
        tdRow.appendChild(tdCell);
        tdCell = document.createElement('td');
        tdCell.innerHTML = rank_list[i]['username'];
        tdRow.appendChild(tdCell);
        tdCell = document.createElement('td');
        tdCell.innerHTML = rank_list[i]['continent'];
        tdRow.appendChild(tdCell);
        tdCell = document.createElement('td');
        tdCell.innerHTML = rank_list[i]['country'];
        tdRow.appendChild(tdCell);
        tdCell = document.createElement('td');
        tdCell.innerHTML = rank_list[i]['city'];
        tdRow.appendChild(tdCell);
        tdCell = document.createElement('td');
        tdCell.innerHTML = rank_list[i]['point'];
        tdRow.appendChild(tdCell);
        tdCell = document.createElement('td');
        tdCell.innerHTML = rank_list[i]['status'];
        tdRow.appendChild(tdCell);
        //write tr row
        document.getElementById("home_list").appendChild(tdRow);
    }

    document.getElementById("table_home_list").style.display='block';
}
