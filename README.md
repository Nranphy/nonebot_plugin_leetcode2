# nonebot_plugin_leetcode2
基于nonebot2的leetcode查询插件。

## 目前已实现功能
- [x] **对指令`/每日一题`，`/lc`，`/leetcode`回复，发送今天的每日一题。**

- [x] **可搜索leetcode题目，指令`/lc搜索 XXXXX`，`/lc查找 XXXXX`，`/leetcode搜索 XXXXX`，将以关键词“XXXXX”进行leetcode搜索，发送搜索到的第一道题。**

- [x] **随机一题，指令`/lc随机`，`/lc随机一题`，`/leetcode随机`将请求leetcode随机一题，发送请求到的任意题目。**

- [x] **查询用户信息`/lc查询 XXXXX`，`/lc查询用户 XXXXX`，`/leetcode查询 XXXXX`，可查询用户基本信息，XXXXX为用户ID（不能用用户名）。**

- [x] **加入计划任务**  每日在指定时间向指定群和好友发送当天的每日一题

## 使用方法

1.在机器人plugins目录下进行git clone

2.使用`nb plugin install nonebot_plugin_leetcode2`

3.使用`pip install nonebot_plugin_leetcode2`，并修改插件加载。

## 注意事项

若有需要使用本插件计划任务相关功能，请在.env.\*文件中加入以下设置：
```
LEETCODE_QQ_FRIENDS=[3102002900]
LEETCODE_QQ_GROUPS=[805324289]
LEETCODE_INFORM_TIME=[{"HOUR":20,"MINUTE":1},{"HOUR":20,"MINUTE":10},{"HOUR":0,"MINUTE":1}]
```
其中`LEETCODE_QQ_FRIENDS`是欲定期发送题目的好友QQ，`LEETCODE_QQ_GROUPS`是定期发送题目的群聊群号，`LEETCODE_INFORM_TIME`是定时的时间。这和另一个leetcode插件的配置项是相同的。

当然，不添加配置项也可正常使用其他功能。感谢@j1g5awi佬的检查与提醒。

另外，由于使用到nonebot-plugin-apscheduler插件，请安排插件导入顺序以免发生错误。


.

.

*（悄悄写在后面...）*

（代码非常臃肿，原理却很简单...有机会再重做...）

（既然都用到了htmlrender了，应该就不用再请求题目信息，直接访问lc进行元素截图就好了吧×~~笨死了~~，不过，之前在境外的服务器访问lc页面经常超时，故放弃尝试了。）

