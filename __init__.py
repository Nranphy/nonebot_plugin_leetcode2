from nonebot import on_command
from nonebot.typing import T_State
from nonebot.params import State
from nonebot.adapters.onebot.v11 import Bot, Event, MessageSegment
from nonebot.log import logger
from .get_data import get_today_title ,get_sub_problem_data ,get_search_title
from nonebot_plugin_htmlrender import get_new_page
import os



request_today = on_command("每日一题",aliases={"lc","leetcode"},priority = 10,block = True)
request_search = on_command("lc查询",aliases={"lc搜索","leetcode搜索"},priority = 10,block = True)



#查询每日一题
@request_today.handle()
async def send_today_problem(bot: Bot,event:Event):
    try:
        today_title = get_today_title()
        logger.info(f"获取今日题目成功，题目为{today_title}.")
        today_data = get_sub_problem_data(today_title)
        logger.info("获取题目内容成功。")
        logger.debug(f"题目{today_data[0]}的难度为{today_data[1]},内容略。")
    except Exception as e:
        request_search.finish("连接到leetcode失败...呜呜呜...\n请稍后再试！！")
        raise e

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
        async with get_new_page(viewport={"width": 840, "height": 800}) as page:
                await page.goto(
                    "file://"+str(os.getcwd())+"/"+html_file_path,
                    wait_until="networkidle"
                )
                pic = await page.screenshot(full_page=True, path=img_file_path)
    except Exception as e:
        logger.error("题目内容（html）转图片出错。")
        request_today.send("题目内容转图片时出错×")
        raise e
    await request_today.send("\n".join(today_data[:2])+MessageSegment.image(pic)+f"\n{today_data[3]}")




#搜索题目
@request_search.handle()
async def parse(bot: Bot, event: Event, state: T_State = State()):
    temp = str(event.get_message()).split()
    if temp[1]:
        state["keyword"] = temp[1]


@request_search.got("keyword",prompt="请输出要在leetcode查找的内容哦~\n可为题号、题目、题干内容哒")
async def send_today_problem(bot: Bot,event:Event,  state: T_State = State()):
    try:
        search_title = get_search_title(state["keyword"])
        if search_title:
            logger.info(f"成功搜索到关键字题目，只取第一条，题目为{search_title}.")
        else:
            logger.info("搜索成功，但并无相关题目。")
            request_search.finish("未搜索到相关题目！！\n要不...换个关键字再搜索一下吧~可为题号、题目、题干内容哒")

        today_data = get_sub_problem_data(search_title)
        logger.info("获取题目内容成功。")
        logger.debug(f"题目{today_data[0]}的难度为{today_data[1]},内容略。")
    except Exception as e:
        request_search.finish("连接到leetcode失败...呜呜呜...\n请稍后再试！！")
        raise e

    ##将html转为图片
    html_path = f"data/nonebot_plugin_leetcode/html"
    check_dir(html_path)
    html_file_path = html_path+f'/{search_title}.html'
    img_path = f"data/nonebot_plugin_leetcode/img"
    check_dir(img_path)
    img_file_path = img_path+f'/{search_title}.png'
    with open(html_file_path,"w+") as f:
        f.write(today_data[2])
    try:
        async with get_new_page(viewport={"width": 840, "height": 800}) as page:
                await page.goto(
                    "file://"+str(os.getcwd())+"/"+html_file_path,
                    wait_until="networkidle"
                )
                pic = await page.screenshot(full_page=True, path=img_file_path)
    except Exception as e:
        logger.error("题目内容（html）转图片出错。")
        raise e
    await request_search.send("\n".join(today_data[:2])+MessageSegment.image(pic)+f"\n{today_data[3]}")









#创建不存在的目录
def check_dir(path):
    if not os.path.isdir(path):
        os.makedirs(path)
        return "Create Successful."