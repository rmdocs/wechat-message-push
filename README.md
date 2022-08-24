# 每日天气推送

> 本项目基本功能使用了Python的wechatpy,requests第三方库,以及内置的python库进行实现例如: time , random模块进行实现

### 本项目提供版本说明

本项目提供了两个版本：

第一个版本挂载Linux服务器运行版本，也就是单一文件，其中代码包含有run.sh脚本，运行run.sh脚本添加自动执行任务！

脚本内容实则使用了crontab命令进行定时运行指令操作！

部署教程：【正在编写中...】

本作者文档站【新站点】:

第二个版本windows版本，windows版本因为之前有人使用Java版本打包做了，我这里也不再用pyexe进行二次打包了，大家可以前往另一个作者仓库进行查看安装操作！

如果有人想要java版本进行更改可以看这位作者的，这位作者做了个可执行化的exe执行文件，效果几乎相同调用内容api不同罢了！

下图是另一个java作者的可执行程序的下载地址！在阅读README的文末！

https://gitee.com/simeitol-sajor/wechat-push

然后还有一个可视化的windows程序，是一个抖音上的作者发布的，也可以去看看！

第三个版本腾讯云函数版本，vercel版本【正在开发中....】

第四个版本github action版本

部署教程：【正在编写中...】

本作者文档站【新站点】:

下面讲一讲我写的程序需要的api以及后续的可扩展操作！手把手教会特别详细！

:speech_balloon: 不会可以留评论进行讨论

:red_circle: 代码有实质性问题可以提交issue，作者会想办法解决的！

不做windows端的原因有很多，包括程序不稳定因素，本作者开发的几个内容基本是比较稳妥的执行方案！

### 本程序源代码运行

本程序是Python程序，主程序为main.py，其它为不同版本的程序。

您只需要安装Python ≥3.6 版本，并且确保pip可以正常使用即可运行本程序！

克隆本项目

```
git clone https://gitee.com/icbugcoder/wechat-push-multi.git
```

安装第三方库，在cmd命令行中运行，mac同理在终端或者iterm2中运行

```shell
pip install -r requirements.txt
```

修改完成对应选项，运行程序

```
windows: python main.py
macos/linux: python3 main.py
```

上述命令只运行一次，多时间段分别推送需要使用定时执行crontab命令！

:warning:程序运行时挂代理会报错

## 微信测试号申请

微信测试号平台地址：[点击前往微信测试号申请页面](https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login)

进入先使用微信登录，登录后会看到下图，我们首先要获取的信息是appID和appsecret，获取后粘贴至注释对应区域

[# appID #appsecret 注释下方项分别填写入内]

![image-20220824211335606](https://img.recode.fun/img-2022/image-20220824211335606.png?)

接口配置信息以及js接口安全域名暂时不用配置，可以做到正常使用！

然后我们要做的是扫描测试号二维码获取用户的openid填写入程序内

openid对应项目即为测试号显示的"微信号"

![image-20220824211712276](https://img.recode.fun/img-2022/image-20220824211712276.png?!)

模板消息接口【我的配置】

```
标题: {{getSayLove.DATA}}
   今日是: {{currentTime.DATA}}, 农历: {{nongli.DATA}}, {{week.DATA}}
   当前时间: {{nowDate.DATA}}
   地点: {{address.DATA}}
   今天天气: {{dayweather.DATA}}转{{nightweather.DATA}}, {{winddirection.DATA}}风, 风速: {{windpower.DATA}}
   现在天气: {{weather.DATA}}
   最高气温: {{daytemp.DATA}}
   最低气温: {{nighttemp.DATA}}
   当前温度: {{temperature.DATA}}

   空气质量: {{suggestion.DATA}}

   一言:{{saying.DATA}}-{{source.DATA}}
   注释: {{transl.DATA}}
```

如果你不喜欢的话可以选择自定义接口！

自定义方法【需要看程序中data是怎么定义的】：

`{{data中的传入参数值.DATA}}`

![image-20220824213522001](https://img.recode.fun/img-2022/image-20220824213522001.png?)

例如我在自定义内容的python程序data中写入了如下内容

```
"birthday": {"value": birthday, "color": get_random_color()},
```

那它的模板消息接口表示方法即为: `{{birthday.DATA}}`

这个value值即等于前面定义类api数据请求的内容调用，现在这个步骤属于api数据整合准备传送阶段。

这样即可完成模板消息接口的定制了，其它接口同理！

## 时间段消息模板的配置

![image-20220824210554830](https://img.recode.fun/img-2022/image-20220824210554830.png?!)

预设了四个时间段，自行在代码中修改

:warning:如果时间段不在范围内请求的消息是无法发送出去的，会报错，返回错误信息！

## 所需API申请

需要申请对应账号去获取appkey

1.天行数据：https://www.tianapi.com/

【早安，晚安，彩虹屁语句调用】--详情功能自行看代码

内容API需要进行申请，请在天行数据api主页进行所需要api添加

申请操作如下图：

![image-20220824191433008](https://img.recode.fun/img-2022/image-20220824191433008.png?)

![image-20220824191518562](https://img.recode.fun/img-2022/image-20220824191518562.png?)

![image-20220824191538329](https://img.recode.fun/img-2022/image-20220824191538329.png?)

因为我们申请后的鉴权key就是我们的账户秘钥key，所以暂时不需要管接口调试问题，我们把所需api申请完成过后去查看下方的账户秘钥查看！

:warning: 本项目<mark>默认</mark>需要进行API申请的接口如下图，大家搜索申请即可：

本源码使用的都是免费接口其接口每天有次数限制，免费用户大多数是每日调用次数不超过100次，因为这些接口api其实可以手写，后期如果有时间的话会把常用的api写完开源

![image-20220824192337846](https://img.recode.fun/img-2022/image-20220824192337846.png?!)

2.心知天气api

官网：https://www.seniverse.com/

注册后进入控制台，这个就是单一的天气api不做多的解释，详情查看下文秘钥apikey查看标题下的，心知天气api申请操作流程

3.高德地图api

[高德开放平台 | 高德地图API (amap.com)](https://lbs.amap.com/)



### 秘钥apikey查看申请

1.天行数据秘钥申请：进入控制台，进入我的秘钥，如下图

![image-20220824190044571](https://img.recode.fun/img-2022/image-20220824190044571.png?)

复制apikey到代码对应注释区域

![image-20220824190115615](https://img.recode.fun/img-2022/image-20220824190115615.png?)

填写区域[需要填写至 # 天行数据  下方的key = '   key填写于此    ' 内]

![image-20220824190157378](https://img.recode.fun/img-2022/image-20220824190157378.png?cd)

2.高德地图api：对应地域天气调用！

3.心知天气API：空气质量等参数

见上文部分注册进入控制台后，先申请免费版产品，见下图

![image-20220824193147788](https://img.recode.fun/img-2022/image-20220824193147788.png?)

然后点击产品内容-->免费版

![image-20220824193318057](https://img.recode.fun/img-2022/image-20220824193318057.png?)



会有一个默认生成的一个api秘钥，然后我们点击小眼睛查看私钥

注意:根据API文档说明<mark>key为私钥</mark>，并不是公钥！

![image-20220824193858983](https://img.recode.fun/img-2022/image-20220824193858983.png?)

把这串私钥复制到我们代码对应注释区 [# 心知天气 注释 下方的  zxkey = '  apikey填写于此  ']

3.高德地图提供的天气api

> 高德开放平台需要进行个人实名认证！验证较为简单，使用认证的支付宝账号授权即可，详情见控制台弹窗指引！

进入控制台，创建应用

![image-20220824195213801](https://img.recode.fun/img-2022/image-20220824195213801.png?)

![image-20220824195246634](https://img.recode.fun/img-2022/image-20220824195246634.png?)

创建好应用后我们添加key

![image-20220824195326579](https://img.recode.fun/img-2022/image-20220824195326579.png?)

选择web服务平台，web服务平台的api支持天气调用，然后编写名称，同意协议后提交即可

天气实名后给的调用次数也是比较多的，可以达到5000次每日

![image-20220824195757197](https://img.recode.fun/img-2022/image-20220824195757197.png?)

申请过后你就可以看到一窜key

![image-20220824200015283](https://img.recode.fun/img-2022/image-20220824200015283.png?)

把key复制到代码对应填写区域[# 高德key 注释下一行的 gdkey = '     此处粘贴key     ']

#### 高德地图天气API地域设定

因为高德地图api需要根据地区的acode码设定进行获取天气信息

acode码如下方腾讯文档表格：

```text
【腾讯文档】AMap_adcode_citycode_20210406
https://docs.qq.com/document/DQkVXZFF6ckRMelll

```

大家进入查看acode码，使用ctrl+F输入城市区县的名称找到自己所在市区县的acode码

![image-20220824200907241](https://img.recode.fun/img-2022/image-20220824200907241.png?)

找到acode码后复制到我们代码中高德注释下 param项下的`"city": "Acode",`

![image-20220824201026815](https://img.recode.fun/img-2022/image-20220824201026815.png?)

#### 心知天气API空气质量地区设定

请在`getkqzl()`类中找到`params`中的`location`项，然后这个是设定监测空气质量的地理位置，官方api中location项支持如下几种格式请自行选择使用！

官方空气质量api文档：[逐小时空气质量预报 API文档](https://seniverse.yuque.com/books/share/f4f9bf1a-d3d9-4a68-8996-950f8c88400e/size6p)

![image-20220824212634996](https://img.recode.fun/img-2022/image-20220824212634996.png?)

![image-20220824211028719](https://img.recode.fun/img-2022/image-20220824211028719.png?)

#### 对本项目源码更改需求的解释

代码中给出如下的API调用，如果需要删除请自行更改代码部分

自行修改def类或删除，删除的时候要注意推送时微信测试号平台的信息模板，以及下方的调用发送数据包推送的模板

![image-20220824190645223](https://img.recode.fun/img-2022/image-20220824190645223.png?)

请根据def后的定义类名称对推送内容及参数进行CRUD操作！

![image-20220824190729515](https://img.recode.fun/img-2022/image-20220824190729515.png?)

当然你也可以选择其它内容api进行调用，具体编写方法参照代码的写法和对应API的api文档的要求参数进行编写！

-----

Powered By icbugcoder



