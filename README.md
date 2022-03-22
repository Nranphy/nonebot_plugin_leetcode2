# nonebot_plugin_leetcode2
基于nonebot2的leetcode查询插件。

## 目前已实现功能
- [x] **对指令`/每日一题`，`/lc`，`/leetcode`回复，发送今天的每日一题。**

- [x] **可搜索leetcode题目，指令`/lc搜索 XXXXX`，`/lc查找 XXXXX`，`/leetcode搜索 XXXXX`，将以关键词“XXXXX”进行leetcode搜索，发送搜索到的第一道题。**

- [x] **随机一题，指令`/lc随机`，`/lc随机一题`，`/leetcode随机`将请求leetcode随机一题，发送请求到的任意题目。**

- [x] **查询用户信息`/lc查询 XXXXX`，`/lc查询用户 XXXXX`，`/leetcode查询 XXXXX`，可查询用户基本信息，XXXXX为用户ID（不能用用户名）。**<br/>
因为能查到的东西太多了，包括用户各方面分数、解题提交总数、解题失败总数、还未接触的题目数、勋章成就、题解标题等等等等，继续爬还有其他信息，所以都加进来会显得杂乱，便大概保留了一些用httpx.post请求的的函数，如感觉有必要对机器人返回信息进行修改，可以简单看看json文件夹内的一些记录（当然...这些json请求和响应写法随时可能过时，请提交issues提醒我或者自行前往leetcode检查×）

- [x] **加入计划任务**  每日在指定时间向指定群和好友发送当天的每日一题

## 使用方法

在机器人plugins目录下进行git clone

## 注意事项

若有需要使用本插件计划任务相关功能，请在.env.\*文件中加入以下设置：
```
LEETCODE_QQ_FRIENDS=[3102002900]
LEETCODE_QQ_GROUPS=[805324289]
LEETCODE_INFORM_TIME=[{"HOUR":20,"MINUTE":1},{"HOUR":20,"MINUTE":10},{"HOUR":0,"MINUTE":1}]
```
其中`LEETCODE_QQ_FRIENDS`是欲定期发送题目的好友QQ，`LEETCODE_QQ_GROUPS`是定期发送题目的群聊群号，`LEETCODE_INFORM_TIME`是定时的时间。

另外，由于使用到nonebot-plugin-apscheduler插件，请安排插件导入顺序以免发生错误。


.

.

*（悄悄写在后面...）*

（代码非常臃肿，原理却很简单...有机会会重做...）

（既然都用到了htmlrender了，应该就不用再请求题目信息，直接访问lc进行元素截图就好了吧×~~笨死了~~）

~~补充，改成直接使用htmlrender截图了，图片质量会更好一些 （有什么比得过原生页面呢） 上面将来加入功能都不算复杂，等空闲的时候会去做的，应该...~~

再次补充...咱服务器在境外，不管timeout调多高都等不到leetcode题目元素出现的×最终还是采用了html渲染...如果有幸有人使用了这个拙劣的插件，有需要的话请自行修改吧！！
