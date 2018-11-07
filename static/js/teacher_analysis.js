

var tc_rank_list;
var page_num = 0;
var one_page_num = 100;

function init_rank_data(period )
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

        $.post("/tc_analysis/GetTcClassLeaderBoard", {period: period, username: sessionStorage.getItem("username")},
        function (data)
        {
            var req_data = JSON.parse(data);
            if (req_data['code'] == 'True')
            {
                tc_rank_list = req_data['leader_board_list'];
                console.log(tc_rank_list);
                // self_info = req_data['self_info']
                // alert("flag_l");
                // flag_l = true;
            }
        });

    }
    catch (e)
    {
        alert(e.toString());
    }


}

function init_data()
{
    if (!sessionStorage.getItem('username'))
    {
        window.location.href = '/';
    }


    page_num = 0;

    //1. clean old
    country.innerHTML ="";
    city.innerHTML = "";

    var period = document.getElementById("class_time");

    // alert(continent.options[continent.selectedIndex].value);
    init_rank_data(period.options[period.selectedIndex].value);

    view_first_page();
}

function view_first_page()
{
    // for (var i = 0; i < rank_list.length; i++)
    //     alert (rank_list[i]['username']);
    // alert("rank " + my_info['rank']);
    // alert("point " + my_info['point']);

    page_num = 0;

    // $('#home_my').html("");
    // $('#home_list').html("");
    // document.getElementById("table_home_my").style.display='none';
    // document.getElementById("table_home_list").style.display='none';

    // add_self_rank();

    for (var i = 0; i < one_page_num && i < tc_rank_list.length; i++)
    {
        console.log(tc_rank_list[i]);
        // alert(rank_list[i]['rank']);

        var tdRow = document.createElement('tr');
        //generate tdcell
        var tdCell = document.createElement('td');
        tdCell.innerHTML = tc_rank_list[i]['rank'];
        tdRow.appendChild(tdCell);
        tdCell = document.createElement('td');
        tdCell.innerHTML = tc_rank_list[i]['class_name'];
        tdRow.appendChild(tdCell);
        tdCell = document.createElement('td');
        tdCell.innerHTML = tc_rank_list[i]['teacher_name'];
        tdRow.appendChild(tdCell);
        tdCell = document.createElement('td');
        tdCell.innerHTML = tc_rank_list[i]['avg_point'];
        tdRow.appendChild(tdCell);
        tdCell = document.createElement('td');
        tdCell.innerHTML = tc_rank_list[i]['status'];
        tdRow.appendChild(tdCell);
        //write tr row
        document.getElementById("class_rank_table").appendChild(tdRow);
    }

    console.log("finished write table");
    // document.getElementById("table_home_my").style.display='block';
    // document.getElementById("table_home_list").style.display='block';
}


function check_li_option(li_option) {
    document.getElementById("item_class_rank").style.display ='none';
    document.getElementById("item_st_list").style.display ='none';
    document.getElementById("item_st_score").style.display ='none';
    if(li_option==0){
        $('#li_0').addClass("li_item_selected").siblings().removeClass("li_item_selected");
        cl_rank_changed();
        document.getElementById("item_class_rank").style.display ='block';
    }
    if(li_option==1){
        $('#li_1').addClass("li_item_selected").siblings().removeClass("li_item_selected");
        cl_num_changed();
        document.getElementById("item_st_list").style.display ='block';
    }
}

function cl_rank_changed(){
    var time = document.getElementById("class_time");
    var app = document.getElementById("class_APP");
    var time_index= time.selectedIndex;
    var app_index = app.selectedIndex;

    var flag = true;

    init_rank_data(time.options[time.selectedIndex].value);

    //******the above 2 variables are the return values from back-end
    //******back-end may need :
    // the chosen "time,app",

    if(flag==false){
        alert("No records!");
    }
    else{
        $('#class_rank_table').html("");
        view_first_page();
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
        //write tr row
        document.getElementById(tb_id).appendChild(tdRow);
    }
}

function cl_num_changed() {
    var cls = document.getElementById("class_num");
    var cls_index= cls.selectedIndex;

    var flag = true;
    var jsonData_list = [{c1:"Class 1",c2:"28854",c3:"Shawn",c4:"Dr. Mary"},
        {c1:"Class 1",c2:"28855",c3:"Tyler",c4:"Dr. Mary"},
        {c1:"Class 1",c2:"28856",c3:"Daisy",c4:"Dr. Mary"},
        {c1:"Class 1",c2:"28857",c3:"Vinson",c4:"Dr. Mary"},
        {c1:"Class 1",c2:"28858",c3:"Wilbert",c4:"Dr. Mary"},
        {c1:"Class 1",c2:"28859",c3:"xx",c4:"Dr. Mary"},
        {c1:"Class 1",c2:"28860",c3:"xx",c4:"Dr. Mary"},
        {c1:"Class 1",c2:"28861",c3:"xx",c4:"Dr. Mary"},
        {c1:"Class 1",c2:"28862",c3:"xx",c4:"Dr. Mary"},
        {c1:"Class 1",c2:"28863",c3:"xx",c4:"Dr. Mary"},
        {c1:"Class 1",c2:"28864",c3:"xx",c4:"Dr. Mary"},
        {c1:"Class 1",c2:"28865",c3:"xx",c4:"Dr. Mary"},
        {c1:"Class 1",c2:"28866",c3:"xx",c4:"Dr. Mary"},
        {c1:"Class 1",c2:"28867",c3:"xx",c4:"Dr. Mary"},
        {c1:"Class 1",c2:"28868",c3:"xx",c4:"Dr. Mary"},
        {c1:"Class 1",c2:"28869",c3:"xx",c4:"Dr. Mary"},
        {c1:"Class 1",c2:"28870",c3:"xx",c4:"Dr. Mary"},
    ]; //return all records

    //******the above 2 variables are the return values from back-end
    //******back-end may need :
    // the chosen "class_num",

    if(flag==false){
        alert("No records!");
    }
    else{
        $('#st_list_table').html("");
        write_table_rows_2(jsonData_list,"st_list_table");
    }
}


function write_table_rows_2(jsonData,tb_id){

    for(var i=0;i<jsonData.length;i++){
        var st_id = jsonData[i].c2;   //will be used

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
        tdCell.innerHTML="<input type='button' value='View' class='st_list_btn' onclick='view_st_score("+st_id+")'>";
        // tdCell.innerHTML="<input type='button' value='View' class='st_list_btn' onclick='view_st_score("+st_id+","+st_name+")'>";
        tdRow.appendChild(tdCell);
        //write tr row
        document.getElementById(tb_id).appendChild(tdRow);
    }
}

function back_st_list(){
    document.getElementById("item_st_score").style.display ='none';
    document.getElementById("item_st_list").style.display ='block';
}

function view_st_score(st_id) {
    // alert(st_id); //for test
    document.getElementById("item_st_list").style.display ='none';
    document.getElementById("item_st_score").style.display ='none';

    score_chart_option(st_id);

    document.getElementById("item_st_score").style.display ='block';
}

function score_chart_option(st_id) {
    // alert(st_id); //for test

    var time=document.getElementById("st_time");
    var app = document.getElementById("st_APP");
    var time_index = time.selectedIndex;    //选择看多久的每日得分，展示最近一周的每日得分曲线/最近一个月/最近一年/最近
    var app_index = app.selectedIndex;      //选择看哪个APP的每日得分变化曲线


    var st_name = 'Daisy'; //obtain according to the st_id
    document.getElementById("st_name_title").textContent = st_name+"'s Score Variation Curve";
    //******need to change:
    // xAxis-data (dates)
    // series-data(student, class average, school average)
    //******according to the return values from back-end

    document.getElementById("st_score_chart").style.display ='none';


    //获取容器，创建表格，设置主题
    var chart_container = document.getElementById('st_score_chart');
    var myChart = echarts.init(chart_container, 'macarons');

    //图表配置 和数据
    var option = {
        tooltip: {trigger: 'axis'},
        legend: {
            data: [st_name, 'Class Average','School Average'],
            x:'center'
        },
        calculable: true,
        xAxis: [{
            axisLabel: {rotate: 30, interval: 0},
            axisLine: {lineStyle: {color: '#575856'}},
            type: 'category',
            boundaryGap: false,
            data: ["2018-7-4", "2018-7-5", "2018-7-6", "2018-7-7", "2018-7-8", "2018-7-9", "2018-7-10"]
        }],
        yAxis: [{
            // min:300,
            // max:320,
            scale: true,
            type: 'value',
            axisLine: {lineStyle: {color: '#575856'}}
        }],
        series: [
            {
                name: st_name,
                type: 'line',
                // symbol:'none',
                smooth: 0.1,
                data: [800, 300, 500, 800, 300, 600, 500]
                //     data:[301, 302, 304, 305, 306, 307,308]
            },
            {
                name: 'Class Average',
                type: 'line',
                // symbol:'none',
                smooth: 0.1,
                color: ['#ad92ff'],
                data: [750, 310, 480, 667, 430, 550, 550]
                //     data:[301, 302, 304, 305, 306, 307,308]
            },
            {
                name: 'School Average',
                type: 'line',
                // symbol:'none',
                smooth: 0.1,
                color: ['#eba052'],
                data: [600, 300, 400, 200, 300, 300, 200]
                // data:[311, 312, 314, 315, 316, 317,318]
            }]
    };//end option
    //填充表格配置
    myChart.setOption(option);
    document.getElementById("st_score_chart").style.display ='block';
}