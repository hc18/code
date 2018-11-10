#### 先上效果图
![上海市2010年第六次全国人口普查](http://upload-images.jianshu.io/upload_images/6634703-6f03b82926a58331.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 全国人口普查10年一次，不要问我为什么不找2017年，我也没办法，摊手～
####思路
1. 申请使用百度地图API密钥
2. 数据准备
3. 分析数据
4. 把地区改编成经纬度
5. 画图
####1. 申请使用百度地图API密钥
- 连接地址
http://lbsyun.baidu.com/apiconsole/key
![image.png](http://upload-images.jianshu.io/upload_images/6634703-f557b0d9559d53be.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 点击创建应用，应用名称随便取，IP白名单，写自己的本地IP，或者0.0.0.0/0 都可
![image.png](http://upload-images.jianshu.io/upload_images/6634703-8da003c4b79b6040.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 点击提交，记住自己的密钥（AK），后面有用。
####2. 数据准备(xlsx格式)
- 数据连接
http://www.stats.gov.cn/tjsj/tjgb/rkpcgb/dfrkpcgb/201202/t20120228_30403.html
![sh_population.xlsx](http://upload-images.jianshu.io/upload_images/6634703-4fc7c695210c5b35.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####3. 数据分析&4. 把地区改编成经纬度
- 我用python3.6
```
import json
from urllib.request import urlopen, quote
import xlrd

# 打开xlsx
book =xlrd.open_workbook("/Users/chengkai/Desktop/file/learn/project/sh_population/sh_population.xlsx")
# 打开sheet1
sh = book.sheet_by_index(0)
# 待拼接的url(不完整的url)
url = 'http://api.map.baidu.com/geocoder/v2/'
ak = '你自己的密钥'
# 遍历每一行，为什么从1开始呢，因为0是标题行，不需要
for i in range(1, sh.nrows):
    # 各个地区前面加上‘上海市’，保证后面检索到的所有经纬度都是上海市的地区，而不是别的省市的
    city ='上海市'+sh.cell_value(i,0)
    # 取第二列所有人口
    population = sh.cell_value(i,1)
    # 因为出现中文，所以转换一下格式
    add = quote(city)
    # 以 json 的格式输出
    output = 'json'
    # URL 正式拼接，这一句画，下面还会详解解释
    uri = url + '?' + 'address=' + add + '&output=' + output + '&ak=' + ak
    req = urlopen(uri)
    # 传入的字符串，需要解码
    res = req.read().decode()
    # 写成json 字典的形式
    temp = json.loads(res)
    # 提取经度
    lng = temp['result']['location']['lng']
    # 提取纬度
    lat = temp['result']['location']['lat']
    # 写成新的字典
    str_temp = '{"lat":' + str(lat) + ',"lng":' + str(lng) + ',"count":' + str(population) +'},'
    print(str_temp)
```
- 注释一，url拼接
- 仔细观察url 不一样的地方就是地区
- 看到下面的字典知道经纬度是怎么一层层提取了把
![image.png](http://upload-images.jianshu.io/upload_images/6634703-30f162fd3ce7f566.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](http://upload-images.jianshu.io/upload_images/6634703-0130e65ba1c3bfa3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
-  最后结果
```
{"lat":31.227203440768868,"lng":121.49607206403445,"count":429891.0},
{"lat":31.213348379555082,"lng":121.48123797847695,"count":248779.0},
{"lat":31.169152089592195,"lng":121.44623500472937,"count":1085130.0},
{"lat":31.213301496813617,"lng":121.3876161086648,"count":690571.0},
{"lat":31.23538080348789,"lng":121.45475555700204,"count":246788.0},
{"lat":31.263742929075534,"lng":121.39844294374956,"count":1288881.0},
{"lat":31.288044465926138,"lng":121.4577688102147,"count":830476.0},
{"lat":31.28249722898657,"lng":121.49191854079479,"count":852476.0},
{"lat":31.304510479541904,"lng":121.5357165996346,"count":1313222.0},
{"lat":31.093537540382123,"lng":121.42502428093465,"count":2429372.0},
{"lat":31.398622694466777,"lng":121.40904121844942,"count":1904886.0},
{"lat":31.36433805543363,"lng":121.25101353755592,"count":1471231.0},
{"lat":31.23089534913395,"lng":121.6384813140922,"count":5044430.0},
{"lat":30.83508077708232,"lng":121.24840817975154,"count":732410.0},
{"lat":31.021244628098586,"lng":121.22679050142115,"count":1582398.0},
{"lat":31.130862397996967,"lng":121.09142524282201,"count":1081022.0},
{"lat":30.915122452605868,"lng":121.56064167963345,"count":1083463.0},
{"lat":31.633564930802045,"lng":121.5353975435439,"count":703722.0},
```
####5. 画图
- 去百度API下载热图脚本
http://developer.baidu.com/map/jsdemo.htm#c1_15
- 复制粘贴下面的代码写到html文件
- 1 改成你的密钥
- 3 把下面的var points 的内容和上面上海市人口的内容替换
- 2 选一个地图的中心点，我选择黄浦区作为我的中心点
- 4 下面的代码还有很多参数值得研究，有时间的读者不妨研究一下，可以留言相互学习哈
![image.png](http://upload-images.jianshu.io/upload_images/6634703-cdcb71a56c77a08f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 如果写如密钥报错的话，可以用v=1.4版本的，因为这版本不需要密钥
```
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
    <script type="text/javascript" src="http://api.map.baidu.com/api?v=1.4"></script>
    <script type="text/javascript" src="http://api.map.baidu.com/library/Heatmap/2.0/src/Heatmap_min.js"></script>
    <title>热力图功能示例</title>
    <style type="text/css">
		ul,li{list-style: none;margin:0;padding:0;float:left;}
		html{height:100%}
		body{height:100%;margin:0px;padding:0px;font-family:"微软雅黑";}
		#container{height:500px;width:100%;}
		#r-result{width:100%;}
    </style>
</head>
<body>
	<div id="container"></div>
	<div id="r-result">
		<input type="button"  onclick="openHeatmap();" value="显示热力图"/><input type="button"  onclick="closeHeatmap();" value="关闭热力图"/>
	</div>
</body>
</html>
<script type="text/javascript">
    var map = new BMap.Map("container");          // 创建地图实例

    var point = new BMap.Point(121.44623500472937, 31.169152089592195);
    map.centerAndZoom(point,15);             // 初始化地图，设置中心点坐标和地图级别
    map.enableScrollWheelZoom(); // 允许滚轮缩放

    var points =[{"lat":31.227203440768868,"lng":121.49607206403445,"count":429891.0},
{"lat":31.213348379555082,"lng":121.48123797847695,"count":248779.0},
{"lat":31.169152089592195,"lng":121.44623500472937,"count":1085130.0},
{"lat":31.213301496813617,"lng":121.3876161086648,"count":690571.0},
{"lat":31.23538080348789,"lng":121.45475555700204,"count":246788.0},
{"lat":31.263742929075534,"lng":121.39844294374956,"count":1288881.0},
{"lat":31.288044465926138,"lng":121.4577688102147,"count":830476.0},
{"lat":31.28249722898657,"lng":121.49191854079479,"count":852476.0},
{"lat":31.304510479541904,"lng":121.5357165996346,"count":1313222.0},
{"lat":31.093537540382123,"lng":121.42502428093465,"count":2429372.0},
{"lat":31.398622694466777,"lng":121.40904121844942,"count":1904886.0},
{"lat":31.36433805543363,"lng":121.25101353755592,"count":1471231.0},
{"lat":31.23089534913395,"lng":121.6384813140922,"count":5044430.0},
{"lat":30.83508077708232,"lng":121.24840817975154,"count":732410.0},
{"lat":31.021244628098586,"lng":121.22679050142115,"count":1582398.0},
{"lat":31.130862397996967,"lng":121.09142524282201,"count":1081022.0},
{"lat":30.915122452605868,"lng":121.56064167963345,"count":1083463.0},
{"lat":31.633564930802045,"lng":121.5353975435439,"count":703722.0},
];

    if(!isSupportCanvas()){
    	alert('热力图目前只支持有canvas支持的浏览器,您所使用的浏览器不能使用热力图功能~')
    }
	//详细的参数,可以查看heatmap.js的文档 https://github.com/pa7/heatmap.js/blob/master/README.md
	//参数说明如下:
	/* visible 热力图是否显示,默认为true
     * opacity 热力的透明度,1-100
     * radius 势力图的每个点的半径大小
     * gradient  {JSON} 热力图的渐变区间 . gradient如下所示
     *	{
			.2:'rgb(0, 255, 255)',
			.5:'rgb(0, 110, 255)',
			.8:'rgb(100, 0, 255)'
		}
		其中 key 表示插值的位置, 0~1.
		    value 为颜色值.
     */
	heatmapOverlay = new BMapLib.HeatmapOverlay({"radius":50});
	map.addOverlay(heatmapOverlay);
	heatmapOverlay.setDataSet({data:points,max:100});
	//是否显示热力图
    function openHeatmap(){
        heatmapOverlay.show();
    }
	function closeHeatmap(){
        heatmapOverlay.hide();
    }
	closeHeatmap();
    function setGradient(){
     	/*格式如下所示:
		{
	  		0:'rgb(102, 255, 0)',
	 	 	.5:'rgb(255, 170, 0)',
		  	1:'rgb(255, 0, 0)'
		}*/
     	var gradient = {};
     	var colors = document.querySelectorAll("input[type='color']");
     	colors = [].slice.call(colors,0);
     	colors.forEach(function(ele){
			gradient[ele.getAttribute("data-key")] = ele.value;
     	});
        heatmapOverlay.setOptions({"gradient":gradient});
    }
	//判断浏览区是否支持canvas
    function isSupportCanvas(){
        var elem = document.createElement('canvas');
        return !!(elem.getContext && elem.getContext('2d'));
    }
</script>
```
####最后用浏览器打开html 文件，会看到最前面的镇楼图，祝君好运～！
