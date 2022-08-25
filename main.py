import time
import random
import requests
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage
import datetime


############### 参数设定区域 #################
# 微信测试号信息
appID = ''
appsecret = ''
# 模板消息接口id
template1 = '' # 自定义模板一的模板消息接口id号
template2 = '' # 自定义模板二的模板消息接口id号，不启用不用填写
template3 = '' # 自定义模板三的模板消息接口id号，不启用不用填写
template4 = '' # 自定义模板四的模板消息接口id号，不启用不用填写
# 关注的成员ID，测试号页面的微信号，实则为账户的openID
user_id = ''
# 天行数据
key = ''
# 心知天气
zxkey = ''
# 高德key
gdkey = ''

# 生日日期参数填写
birthyear = '' # 不要填写大于当前日期
birthmonth = '' # 直接填写整数，前面无需加0
birthday = '' # 出生日，日期

location = '' # 心知天气api 空气质量监测地区，英文拼写
cityacode = '' # 高德地图天气情况获取，城市acode 参照readme文档填写
############### 参数设定区域结束 ##################

############## ↓ ↓ ↓ ↓ 下方程序根据需求自定义更改 ↓ ↓ ↓ ↓ ################

# 当前日期获取
currentTime = time.strftime("%Y-%m-%d", time.localtime(time.time()))
nowDate = time.strftime("%H:%M:%S", time.localtime(time.time()))

# 生日日期计算
toyear = time.strftime('%Y',time.localtime(time.time()))    #"%Y"将被无世纪的年份锁代替
tomon = time.strftime('%m',time.localtime(time.time()))
today = time.strftime('%d',time.localtime(time.time()))
toyear = int(toyear)
tomon = int(tomon)
today = int(today)
todaynow = time.strftime("%Y-%m-%d",time.localtime())

# 定义距离生日日期天数计算
def insert_year():
    #润年2月29天，平年28天
    flag = True
    while flag:
        input_year = birthyear #输入出生的年份
        #今年之前出生的
        if input_year <= toyear:
            return input_year
            flag = False
        else:
            print("请不要输入未来的年份，因为她还没有出生...")
            continue

def insert_mon():
    flag = True
    while flag:
        input_mon = birthmonth # 出生月份
        if input_mon > 12 or input_mon < 1:
            print("请输入正确的出生月")
            continue
        else:
            return input_mon
            flag = False


def insert_day():
    flag = True
    while flag:
        input_day = birthday
        if input_day > today:
            if input_day > 31 or input_day < 1:
                print("请输入正确的出生日")
                continue
            elif input_day == today:
                print("生日快乐")
                flag = False
                return input_day
            else:
                return input_day
                flag = False
        else:
            return input_day
            flag = False

# 日期处理
def getweek():
    weekEng = time.strftime("%A", time.localtime(time.time()))
    week_list = {
        "Monday": "星期一",
        "Tuesday": "星期二",
        "Wednesday": "星期三",
        "Thursday": "星期四",
        "Friday": "星期五",
        "Saturday": "星期六",
        "Sunday": "星期日"
    }
    week = week_list[weekEng]
    return week

##### API调用部分开始 ###

# 高德
def getcitybase():
    url = 'https://restapi.amap.com/v3/weather/weatherInfo'
    params = {
        "key": gdkey,
        "city": cityacode, # 城市acode码填写
        "extensions": "base",
    }
    resp = requests.get(url, params)
    data = resp.json()
    if resp.status_code == 200:
        return data
    else:
        print('请求失败')


def getcityall():
    url = 'https://restapi.amap.com/v3/weather/weatherInfo'
    params = {
        "key": gdkey,
        "city": cityacode, # 城市acode码填写
        "extensions": "all",
    }
    resp = requests.get(url, params)
    data = resp.json()
    if resp.status_code == 200:
        return data
    else:
        print('请求失败')


getcitybase = getcitybase()
getcityall = getcityall()
address = getcitybase['lives'][0]['city']  # 地点
weather = getcitybase['lives'][0]['weather']  # 天气
temperature = getcitybase['lives'][0]['temperature']  # 温度
winddirection = getcitybase['lives'][0]['winddirection']  # 风向
windpower = getcitybase['lives'][0]['windpower']  # 风力
dayweather = getcityall['forecasts'][0]['casts'][0]['dayweather']
nightweather = getcityall['forecasts'][0]['casts'][0]['nightweather']
daytemp = getcityall['forecasts'][0]['casts'][0]['daytemp']
nighttemp = getcityall['forecasts'][0]['casts'][0]['nighttemp']

print('--------', '\n', '城市:', address, '\n', '天气:', weather, '\n', '当下温度:', temperature + '℃', '\n', '风向:',
      winddirection, '\n', '风速:', windpower)
print('--------')
print(getcityall['forecasts'][0]['casts'][0]['dayweather'])
print(getcityall['forecasts'][0]['casts'][0]['nightweather'])
print(getcityall['forecasts'][0]['casts'][0]['daytemp'])
print(getcityall['forecasts'][0]['casts'][0]['nighttemp'])
print('--------')
print(getcityall['forecasts'][0]['casts'][1]['dayweather'])
print(getcityall['forecasts'][0]['casts'][1]['nightweather'])
print(getcityall['forecasts'][0]['casts'][1]['daytemp'])
print(getcityall['forecasts'][0]['casts'][1]['nighttemp'])


# 随机颜色渲染
def get_random_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)


# 获取空气质量
def getkqzl():
    params = {
        "key": zxkey,
        "location": location,  # 查询地点设置为访问IP所在地
        "language": "zh-Hans",
        "unit": "c",
        "days": "1"
    }
    url = 'https://api.seniverse.com/v3/life/suggestion.json'
    resp = requests.get(url, params)
    if resp.status_code == 200:
        data = resp.json()["results"]
        return data[0]['suggestion'][0]['air_pollution']['brief']
    else:
        print('请求失败')


# 处理获取到的数据
getkqzl = getkqzl()
suggestion = getkqzl  # 空气质量


# 根据空气质量设置颜色
def suggestioncolor():
    if suggestion == '优':
        return '#33FF33'
    elif suggestion == '良' or suggestion == '中':
        return '#77FF00'
    else:
        return '#FFAA33'


# 土味情话
def getSayLove():
    url = 'http://api.tianapi.com/saylove/index?key='
    resp = requests.get(url + key)
    if resp.status_code == 200:
        data = resp.json()
        return data['newslist'][0]['content']
    else:
        print('请求失败')


# 情诗
def getqingshi():
    url = 'http://api.tianapi.com/qingshi/index?key='
    resp = requests.get(url + key)
    if resp.status_code == 200:
        data = resp.json()
        return data['newslist'][0]['content']
    else:
        print('请求失败')


# 早安心语
def getzaoan():
    url = 'http://api.tianapi.com/zaoan/index?key='
    resp = requests.get(url + key)
    if resp.status_code == 200:
        data = resp.json()
        return data['newslist'][0]['content']
    else:
        print('请求失败')


# 晚安心语
def getwanan():
    url = 'http://api.tianapi.com/wanan/index?key='
    resp = requests.get(url + key)
    if resp.status_code == 200:
        data = resp.json()
        return data['newslist'][0]['content']
    else:
        print('请求失败')


# 励志古言
def getlzmy():
    url = 'http://api.tianapi.com/lzmy/index?key='
    resp = requests.get(url + key)
    if resp.status_code == 200:
        data = resp.json()
        return data['newslist'][0]
    else:
        print('请求失败')


# 彩虹屁
def getcaihongpi():
    url = 'http://api.tianapi.com/caihongpi/index?key='
    resp = requests.get(url + key)
    if resp.status_code == 200:
        data = resp.json()
        return data['newslist'][0]['content']
    else:
        print('请求失败')


# 节假日
def getjiejiari():
    url = 'http://api.tianapi.com/jiejiari/index?key='
    resp = requests.get(url + key + '&date=' + currentTime + '&type=2')
    if resp.status_code == 200:
        data = resp.json()
        return data['newslist'][0]
    else:
        print('请求失败')


# one一个
def getone():
    url = 'http://api.tianapi.com/one/index?key='
    resp = requests.get(url + key + '&rand=1')
    if resp.status_code == 200:
        data = resp.json()
        return data['newslist'][0]['word']
    else:
        print('请求失败')


# 天气诗句
def gettianqishiju():
    url = 'http://api.tianapi.com/tianqishiju/index?key='
    weatherlist = {
        "风": "1",
        "云": "2",
        "雨": "3",
        "雪": "4",
        "霜": "5",
        "露": "6",
        "雾": "7",
        "雷": "8",
        "晴": "9",
        "阴": "10",
    }
    resp = requests.get(url + key + '&tqtype=' + weatherlist[weather])
    if resp.status_code == 200:
        data = resp.json()
        return data['newslist'][0]
    else:
        print('请求失败')


getSayLove = getSayLove()
getqingshi = getqingshi()
getzaoan = getzaoan()
getwanan = getwanan()
getlzmy = getlzmy()
getcaihongpi = getcaihongpi()
getjiejiari = getjiejiari()
getone = getone()
# gettianqishiju = gettianqishiju()

##### API调用部分结束 ###

# 推送消息
client = WeChatClient(appID, appsecret)
wm = WeChatMessage(client)

if "06:00:00" < nowDate < "22:00:00":
    # 微信消息模板 ID
    template_id = template1
    # 自定义的内容
    data = {
        "getSayLove": {"value": getSayLove, "color": get_random_color()},
        "currentTime": {"value": currentTime, "color": get_random_color()},
        "nongli": {"value": getjiejiari['lunarmonth'] + '-' + getjiejiari['lunarday'], "color": get_random_color()},
        "week": {"value": getweek(), "color": get_random_color()},
        "nowDate": {"value": nowDate, "color": get_random_color()},
        "address": {"value": address, "color": get_random_color()},
        "dayweather": {"value": dayweather, "color": get_random_color()},
        "nightweather": {"value": nightweather, "color": get_random_color()},
        "winddirection": {"value": winddirection, "color": get_random_color()},
        "windpower": {"value": windpower, "color": get_random_color()},
        "weather": {"value": weather, "color": get_random_color()},
        "daytemp": {"value": daytemp, "color": get_random_color()},
        "nighttemp": {"value": nighttemp, "color": get_random_color()},
        "temperature": {"value": temperature + '℃', "color": get_random_color()},
        "suggestion": {"value": suggestion, "color": suggestioncolor()},
        "saying": {"value": getlzmy['saying'], "color": get_random_color()},
        "source": {"value": getlzmy['source'], "color": get_random_color()},
        "transl": {"value": getlzmy['transl'], "color": get_random_color()},
   }

# if "11:00:00" < nowDate < "14:00:00":
#     template_id = template2
#     data = {
#         "nowDate": {"value": nowDate, "color": get_random_color()},
#         "week": {"value": getweek(), "color": get_random_color()},
#         "city": {"value": address, "color": get_random_color()},
#         "weather": {"value": weather, "color": get_random_color()},
#         "kqtype": {"value": suggestion, "color": suggestioncolor()},
#         "tem": {"value": temperature + '℃', "color": get_random_color()},
#     }
# if "14:00:00" < nowDate < "18:00:00":
#     template_id = template3
#     data = {
#         "nowDate": {"value": nowDate, "color": get_random_color()},
#         "week": {"value": getweek(), "color": get_random_color()},
#         "city": {"value": address, "color": get_random_color()},
#         "weather": {"value": weather, "color": get_random_color()},
#         "kqtype": {"value": suggestion, "color": suggestioncolor()},
#         "tem": {"value": temperature + '℃', "color": get_random_color()},
#     }
# if "18:00:00" < nowDate < "24:00:00":
#     template_id = template4
#     data = {
#         "nowDate": {"value": nowDate, "color": get_random_color()},
#         "week": {"value": getweek(), "color": get_random_color()},
#         "city": {"value": address, "color": get_random_color()},
#         "weather": {"value": weather, "color": get_random_color()},
#         "kqtype": {"value": suggestion, "color": suggestioncolor()},
#         "tem": {"value": temperature + '℃', "color": get_random_color()},
#     }


# 发送自定义参数集，请求微信api进行处理，改成模板形式进行请求
resp = wm.send_template(user_id,template_id,data)
print(resp)


######## 下方是可获取api信息的显示，如有需要可以打开进行查看 #######

# print("当前时间：", currentTime, '-', nowDate, '-', getweek())
# print('位置天气：', address, '-', temperature + '℃', '-', weather, '-', suggestion)
# print('土味情话', getSayLove)
# print('情诗', getqingshi)
# print('早安', getzaoan)
# print('晚安', getwanan)
# print('励志名言', getlzmy['saying'], '-', getlzmy['source'], '-', getlzmy['transl'])
# print('彩虹屁', getcaihongpi)
# print('节假日', getjiejiari['lunarmonth'], '-', getjiejiari['lunarday'], getjiejiari['info'])
# print('one', getone)
# print(weather, '-', gettianqishiju['source'], '-', gettianqishiju['author'], '-', gettianqishiju['content'])
