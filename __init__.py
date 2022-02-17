from nonebot import get_driver,on_command
from .config import Config
from nonebot.adapters.onebot.v11 import Bot, Event
from get_data import get_today_title,get_sub_problem_data

global_config = get_driver().config
config = Config.parse_obj(global_config)

request_today = on_command("每日一题",aliases=("lc","leetcode"),priority = 10,block = True)


@request_today.handle
async def send_today_problem(bot: Bot,event:Event):
    today_title = await get_today_title()
    today_data = await get_sub_problem_data(today_title)
    bot.send(event,message="\n".join(today_data))