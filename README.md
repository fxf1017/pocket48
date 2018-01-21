# pocket48
纯属个人自娱自乐

基于[qqbot](https://github.com/pandolia/qqbot)和Python2.7制作，基于酷Q的请参照coolq分支

监控成员口袋48聚聚房间，微博和微打赏项目

目前可用的插件: 
* pocket48_plugin(口袋48插件)
* weibo_plugin(微博监听插件)
* wds_plugin（微打赏监听插件)

口袋48插件1分钟监听一次，微博插件45秒监听一次，微打赏插件1分钟监听一次（可以自行调整）

### qqbot配置
* 具体使用请参照qqbot的主页
* 在~/.qqbot-tmp/v2.3.conf中配置机器人的qq消息, 在plugin中可以填写自己想要使用的插件
* 请填写接收二维码的邮箱及邮箱授权码，百度即可搜到授权码生成方法
* 在run-pocket48.sh中最后一行'qqbot -u'后面的参数修改为配置的qq用户名
* 配置完成之后，运行run-pocket48.sh即可
 
### 口袋48和微博插件使用
* 首先确保你想监控的成员已经开通口袋房间
* 在conf.ini中修改自己想要监控的成员的拼音（目前只有Team SII和NII的资料，如果有其他人的话，可以自行按照里面的格式添加成员的口袋ID，房间ID，微博链接）
* 可以给不同的群开放不同的功能(目前有房间消息，房间评论，直播提醒，微博提醒），详情请见conf.ini</p>
* 由于qqbot限制，暂不支持语音和图片消息</p>
* 在conf.ini中修改内容，注意一定要按照格式来写，否则无法解析
* 在写了群号之后，一定在底下加上群名称（底层限制，无法通过群号来搜索群名）


### 微打赏插件使用
* 微打赏监控数据在data/wds.json中，monitor_activities为监控项目，wds_pk_activities为PK活动的项目
* 摩点的插件还在开发中


### 注意事项
* 第一次使用时会向邮箱中发送登录二维码，用手机QQ扫码登录即可
* 每天晚上10点钟（可以再pocket48_plugin.py中的restart_sche()函数中修改重启时间）
* qqbot没有coolq稳定，会经常出现掉线的情况，所以需要扫码重新登录
