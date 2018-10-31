
var history_rank_list = [];
var history_point_list = [];
var history_avg_point_list = [];
var history_datetime = [];

function check_login()
{
    if (!sessionStorage.getItem('username'))
    {
        window.location.href = '/';
    }
}

function init_history_rank(period)
{
    try
    {
        $.ajaxSetup({
            async : false
        });
        $.post("/analysis/GetHistoryRank", {period: period, username: sessionStorage.getItem("username")},
        function (data)
        {
            var req_data = JSON.parse(data);
            if (req_data['code'] == 'True')
            {
                console.log(req_data['history_rank_list']);
                history_rank_list = req_data['history_rank_list'];
            }
        });
    }
    catch (e)
    {
        console.log("erro");
        return null;
    }
}

function init_history_points(period)
{
    try
    {
        $.ajaxSetup({
            async : false
        });
        $.post("/analysis/GetHistoryPoint", {period: period, username: sessionStorage.getItem("username")},
        function (data)
        {
            var req_data = JSON.parse(data);
            if (req_data['code'] == 'True')
            {
                console.log(req_data['history_point_list']);
                history_point_list = req_data['history_point_list'];
            }
        });
    }
    catch (e)
    {
        console.log("error_point");
        return null;
    }
}

function init_history_avg_points(period)
{
    try
    {
        $.ajaxSetup({
            async : false
        });
        $.post("/analysis/GetHistoryAvgPoint", {period: period, username: sessionStorage.getItem("username")},
        function (data)
        {
            var req_data = JSON.parse(data);
            if (req_data['code'] == 'True')
            {
                console.log(req_data['history_avg_point_list']);
                history_avg_point_list = req_data['history_avg_point_list'];
            }
        });
    }
    catch (e)
    {
        console.log("error_point");
        return null;
    }
}

function init_history_date(period)
{
    try
    {
        $.ajaxSetup({
            async : false
        });
        $.post("/analysis/GetHistoryDate", {period: period, username: sessionStorage.getItem("username")},
        function (data)
        {
            var req_data = JSON.parse(data);
            if (req_data['code'] == 'True')
            {
                console.log(req_data['history_date_list']);
                history_datetime = req_data['history_date_list'];
            }
        });
    }
    catch (e)
    {
        console.log("error_point");
        return null;
    }
}

function get_history_rank(period)
{
    try
    {
        $.ajaxSetup({
            async : false
        });
        $.post("/leader_board/GetHistoryRank", {period: period, username: sessionStorage.getItem("username")},
        function (data)
        {
            var req_data = JSON.parse(data);
            if (req_data['code'] == 'True')
            {
                console.log(req_data['history_rank_list']);
                return req_data['history_rank_list'];
            }
        });
    }
    catch (e)
    {
        console.log("error_point");
        return null;
    }
}

function check_li_option(li_option)
{
    check_login();
    document.getElementById("item_score_curve").style.display ='none';
    document.getElementById("item_rank_curve").style.display ='none';
    if(li_option==0){
        $('#li_0').addClass("li_item_selected").siblings().removeClass("li_item_selected");
        score_curve_chart_option();
        document.getElementById("item_score_curve").style.display ='block';
    }
    if(li_option==1){
        $('#li_1').addClass("li_item_selected").siblings().removeClass("li_item_selected");
        rank_curve_chart_option();
        document.getElementById("item_rank_curve").style.display ='block';
    }
}

/*score_curve 折线图选项变化时*/
function score_curve_chart_option(){
    var time=document.getElementById("score_curve_time");
    var app = document.getElementById("score_curve_APP");
    var time_index = time.selectedIndex;    //选择看多久的每日得分，展示最近一周的每日得分曲线/最近一个月/最近一年/最近
    var app_index = app.selectedIndex;      //选择看哪个APP的每日得分变化曲线

    alert(time.options[time.selectedIndex].value);
    //init data
    init_history_rank(time.options[time.selectedIndex].value);
    init_history_points(time.options[time.selectedIndex].value);
    init_history_avg_points(time.options[time.selectedIndex].value);
    init_history_date(time.options[time.selectedIndex].value);

    //******need to change:
    // xAxis-data (dates)
    // series-data(my, school average)
    //******according to the return values from back-end

    document.getElementById("score_curve_chart").style.display ='none';

    //获取容器，创建表格，设置主题
    var chart_container = document.getElementById('score_curve_chart');
    var myChart = echarts.init(chart_container, 'macarons');

    //图表配置 和数据
    var option = {
        tooltip: {trigger: 'axis'},
        legend: {
            data: ['My', 'School average'],
            x:'center'
        },
        calculable: true,
        xAxis: [{
            axisLabel: {rotate: 30, interval: 0},
            axisLine: {lineStyle: {color: '#575856'}},
            type: 'category',
            boundaryGap: false,
            data: history_datetime
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
                name: 'My',
                type: 'line',
                // symbol:'none',
                smooth: 0.1,
                data: history_point_list
                //     data:[301, 302, 304, 305, 306, 307,308]
            },
            {
                name: 'School average',
                type: 'line',
                // symbol:'none',
                smooth: 0.1,
                color: ['#eba052'],
                data: history_avg_point_list
                // data:[311, 312, 314, 315, 316, 317,318]
            }]
    };//end option
    //填充表格配置
    myChart.setOption(option);
    document.getElementById("score_curve_chart").style.display ='block';
}

function rank_curve_chart_option(){
    var time=document.getElementById("rank_curve_time");
    var app = document.getElementById("rank_curve_APP");
    var time_index = time.selectedIndex;    //选择看多久的每日得分，展示最近一周的每日得分曲线/最近一个月/最近一年/最近
    var app_index = app.selectedIndex;      //选择看哪个APP的每日得分变化曲线

    //******need to change:
    // xAxis-data (dates)
    // series-data(my)
    //******according to the return values from back-end

    init_history_rank("Weekly");

    document.getElementById("rank_curve_chart").style.display ='none';

    //获取容器，创建表格，设置主题
    var chart_container = document.getElementById('rank_curve_chart');
    var myChart = echarts.init(chart_container, 'macarons');

    //图表配置 和数据
    var option = {
        tooltip: {trigger: 'axis'},
        legend: {
            data: ['My ranking'],
            x:'center'
        },
        calculable: true,
        xAxis: [{
            axisLabel: {rotate: 30, interval: 0},
            axisLine: {lineStyle: {color: '#575856'}},
            type: 'category',
            boundaryGap: false,
            data: history_datetime
        }],
        yAxis: [{
            // min:300,
            // max:320,
            scale: true,
            type: 'value',
            inverse:true,
            axisLine: {lineStyle: {color: '#575856'}}
        }],
        series: [
            {
                name: 'My ranking',
                type: 'line',
                // symbol:'none',
                smooth: 0.1,
                data: history_rank_list
                //     data:[301, 302, 304, 305, 306, 307,308]
            }]
    };//end option
    //填充表格配置
    myChart.setOption(option);
    document.getElementById("rank_curve_chart").style.display ='block';
}