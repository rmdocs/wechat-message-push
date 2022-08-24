import time
import random
import requests
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage

# 微信Key
appID = ''
appsecret = ''
# 关注的成员ID，测试号页面的微信号，实则为账户的openID
user_id = ''
# 天行数据
key = ''
# 心知天气
zxkey = ''
# 高德key
gdkey = ''

currentTime = time.strftime("%Y-%m-%d", time.localtime(time.time()))
nowDate = time.strftime("%H:%M:%S", time.localtime(time.time()))


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


# 高德
def getcitybase():
    url = 'https://restapi.amap.com/v3/weather/weatherInfo'
    params = {
        "key": gdkey,
        "city": "", # 城市acode码填写
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
        "city": "", # 城市acode码填写
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


# 随机颜色
def get_random_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)


# 获取空气质量
def getkqzl():
    params = {
        "key": zxkey,
        "location": "dalian",  # 查询地点设置为访问IP所在地
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

# 推送消息
client = WeChatClient(appID, appsecret)
wm = WeChatMessage(client)

if "06:00:00" < nowDate < "09:00:00":
    # 微信消息模板 ID
    template_id = ''
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
#     template_id = 'fvxNrCL9nq3MMxi_DstlnKkBtsnpsYAm62wxURWe2NY'
#     data = {
#         "nowDate": {"value": nowDate, "color": get_random_color()},
#         "week": {"value": getweek(), "color": get_random_color()},
#         "city": {"value": address, "color": get_random_color()},
#         "weather": {"value": weather, "color": get_random_color()},
#         "kqtype": {"value": suggestion, "color": suggestioncolor()},
#         "tem": {"value": temperature + '℃', "color": get_random_color()},
#     }
# if "14:00:00" < nowDate < "18:00:00":
#     template_id = 'U7ZvonOp9jRdpc9J2X7FwdjLEqs-ZogbzUnFYU9K2jY'
#     data = {
#         "nowDate": {"value": nowDate, "color": get_random_color()},
#         "week": {"value": getweek(), "color": get_random_color()},
#         "city": {"value": address, "color": get_random_color()},
#         "weather": {"value": weather, "color": get_random_color()},
#         "kqtype": {"value": suggestion, "color": suggestioncolor()},
#         "tem": {"value": temperature + '℃', "color": get_random_color()},
#     }
# if "18:00:00" < nowDate < "24:00:00":
#     template_id = 'M5U2l1QiNWCxN8q5LLj6LaIOPDi3T3NDHn2VLDmh2k0'
#     data = {
#         "nowDate": {"value": nowDate, "color": get_random_color()},
#         "week": {"value": getweek(), "color": get_random_color()},
#         "city": {"value": address, "color": get_random_color()},
#         "weather": {"value": weather, "color": get_random_color()},
#         "kqtype": {"value": suggestion, "color": suggestioncolor()},
#         "tem": {"value": temperature + '℃', "color": get_random_color()},
#     }



resp = wm.send_template(user_id, template_id, data)

print(resp)
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
