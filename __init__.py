from email.message import Message
from nonebot import get_driver,on_command
from .config import Config
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.log import logger
from .get_data import get_today_title,get_sub_problem_data
from nonebot_plugin_htmlrender import get_new_page
import os



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

    ##将html转为图片
    html_path = f"data/nonebot_plugin_leetcode/html"
    check_dir(html_path)
    html_file_path = html_path+f'/{today_title}.html'
    img_path = f"data/nonebot_plugin_leetcode/img"
    check_dir(img_path)
    img_file_path = img_path+f'/{today_title}.png'
    with open(html_file_path,"w+") as f:
        f.write(today_data[2])
    try:
        async with get_new_page(viewport={"width": 300, "height": 300}) as page:
                await page.goto(
                    "file://"+html_file_path,
                    wait_until="networkidle"
                )
                pic = await page.screenshot(full_page=True, path=img_file_path)
    except Exception as e:
        logger.error("题目内容（html）转图片出错。")
        raise e
    await request_today.send("\n".join(today_data[:2])+pic+f"\n{today_data[3]}")



#网上找来的，创建不存在的目录
def check_dir(path):
    '''判断文件夹是否存在，如果不存在就创建一个'''
    if not os.path.isdir(path):
        os.makedirs(path)
        return "Create Successful."