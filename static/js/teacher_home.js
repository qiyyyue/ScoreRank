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

var self_info;
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

        $.post("/tc_home/GetTcLeaderBoard", {continent: continent, country: country, city: city, period: period, username: sessionStorage.getItem("username")},
        function (data)
        {
            var req_data = JSON.parse(data);
            if (req_data['code'] == 'True')
            {
                rank_list = req_data['leader_board_list'];
                console.log(rank_list);
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
    if (!sessionStorage.getItem('username'))
    {
        window.location.href = '/';
    }


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

    // $('#home_my').html("");
    $('#home_list').html("");
    // document.getElementById("table_home_my").style.display='none';
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
    // document.getElementById("table_home_my").style.display='block';
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
    // $('#home_my').html("");
    $('#home_list').html("");
    // document.getElementById("table_home_my").style.display='none';
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

    // document.getElementById("table_home_my").style.display='block';
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

    // add_self_rank();
    // $('#home_my').html("");
    $('#home_list').html("");
    // document.getElementById("table_home_my").style.display='none';
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

    // document.getElementById("table_home_my").style.display='block';
    document.getElementById("table_home_list").style.display='block';
}

function add_self_rank(){
    $('#home_my').html("");
    document.getElementById("table_home_my").style.display='none';

    var tdRow = document.createElement('tr');
    //generate tdcell
    var tdCell = document.createElement('td');
    tdCell.innerHTML = self_info['rank'];
    tdRow.appendChild(tdCell);
    tdCell = document.createElement('td');
    tdCell.innerHTML = self_info['username'];
    tdRow.appendChild(tdCell);
    tdCell = document.createElement('td');
    tdCell.innerHTML = self_info['continent'];
    tdRow.appendChild(tdCell);
    tdCell = document.createElement('td');
    tdCell.innerHTML = self_info['country'];;
    tdRow.appendChild(tdCell);
    tdCell = document.createElement('td');
    tdCell.innerHTML = self_info['city'];;
    tdRow.appendChild(tdCell);
    tdCell = document.createElement('td');
    tdCell.innerHTML = self_info['point'];
    tdRow.appendChild(tdCell);
    tdCell = document.createElement('td');
    tdCell.innerHTML = self_info['status'];
    tdRow.appendChild(tdCell);
    //write tr row
    document.getElementById("home_my").appendChild(tdRow);

    document.getElementById("table_home_my").style.display='block';
}

function update_view_table(continent,country,city,time){
    var flag = true;
    var jsonData_list = [{c1:1,c2:"Hughes",c3:"The Confucius Institute of the University of Aberdeen",c4:"Aberdeen",c5:"the United Kingdom",c6:551,c7:"+2"},
            {c1:2,c2:"Aaron",c3:"The Confucius Institute in Chicago",c4:"Chicago",c5:"the United States",c6:532,c7:"-1"},
            {c1:3,c2:"Fallon",c3:"The Confucius Institute at Cairo University",c4:"Cairo",c5:"Egypt",c6:517,c7:"+3"},
            {c1:4,c2:"Halley",c3:"Institute Confucius of Centre culturel de Chine à Paris",c4:"Paris",c5:"France",c6:509,c7:"+5"},
            {c1:5,c2:"Pearson",c3:"The Confucius Institute at Carleton University",c4:"Ottawa",c5:"Canada",c6:497,c7:"-2"},
            {c1:6,c2:"Shawn",c3:"The Confucius Institute at theUniversity of Nairobi",c4:"Nairobi",c5:"Kenya",c6:471,c7:"-3"},
            {c1:7,c2:"Tyler",c3:"Confucius Institute of the University of Sydney",c4:"Sydney",c5:"Australia",c6:458,c7:"0"},
            {c1:8,c2:"Daisy",c3:"Confucius Institute at the University of Auckland",c4:"Auckland",c5:"New Zealand",c6:421,c7:"0"},
            {c1:9,c2:"Vinson",c3:"Confucius Institute in Seoul",c4:"Seoul",c5:"Korea",c6:391,c7:"-5"},
            {c1:10,c2:"Wilbert",c3:"Confucius Institute at Sapporo University",c4:"Sapporo",c5:"Japan",c6:361,c7:"+4"},
        ]; //return 10 records
    var jsonData_my = [{c1:112,c2:"Henry",c3:"The Confucius Institute of the University of Aberdeen",c4:"Aberdeen",c5:"the United Kingdom",c6:177,c7:"+12"}];    //NULL when userRole is "teacher"

    //******the above 3 variables are the return values from back-end
    //******back-end may need :
    // the user id,
    // the chosen "continent,country,city,time",
    // and the current page number "page_num"

    if(flag==false && page_num>0){    // only happens when user click "next page"
        alert("No more data!");
        if(page_num>0){
            page_num = page_num-1;
        }
        document.getElementById("table_home_my").style.display='block';
        document.getElementById("table_home_list").style.display='block';
    }
    else if (flag==false && page_num==0){  //happens when no records under this choice
        alert("No records!");
    }
    else{
        $('#home_my').html("");
        $('#home_list').html("");
        write_table_rows(jsonData_my,"home_my");
        document.getElementById("table_home_my").style.display='block';
        write_table_rows(jsonData_list,"home_list");
        document.getElementById("table_home_list").style.display='block';
    }

}


function write_table_rows(jsonData,tb_id){

    for(var i=0;i<jsonData.length;i++){
        var tdRow = document.createElement('tr');
        //generate tdcell
        var tdCell = document.createElement('td');
        tdCell.innerHTML=jsonData[i].c1;
        tdRow.appendChild(tdCell);
        tdCell = document.createElement('td');
        tdCell.innerHTML=jsonData[i].c2;
        tdRow.appendChild(tdCell);
        tdCell = document.createElement('td');
        tdCell.innerHTML=jsonData[i].c3;
        tdRow.appendChild(tdCell);
        tdCell = document.createElement('td');
        tdCell.innerHTML=jsonData[i].c4;
        tdRow.appendChild(tdCell);
        tdCell = document.createElement('td');
        tdCell.innerHTML=jsonData[i].c5;
        tdRow.appendChild(tdCell);
        tdCell = document.createElement('td');
        tdCell.innerHTML=jsonData[i].c6;
        tdRow.appendChild(tdCell);
        tdCell = document.createElement('td');
        tdCell.innerHTML=jsonData[i].c7;
        tdRow.appendChild(tdCell);
        //write tr row
        document.getElementById(tb_id).appendChild(tdRow);
    }
}