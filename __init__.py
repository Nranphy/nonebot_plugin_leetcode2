from email.message import Message
from nonebot import get_driver,on_command
from .config import Config
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.log import logger
from .get_data import get_today_title,get_sub_problem_data

global_config = get_driver().config
config = Config.parse_obj(global_config.dict())

request_today = on_command("每日一题",aliases={"lc","leetcode"},priority = 10,block = True)


@request_today.handle()
async def send_today_problem(bot: Bot,event:Event):
    today_title = get_today_title()
    logger.info(f"获取今日题目成功，题目为{today_title}.")
    today_data = get_sub_problem_data(today_title)
    logger.info("获取题目内容成功。")
    logger.debug(f"题目{today_data[0]}的难度为{today_data[1]},内容略。")
    await request_today.send("\n".join(today_data[:2])+Message.img(today_data[2])+f"\n{today_data[3]}")