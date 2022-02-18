import httpx
import json
import os
from nonebot_plugin_htmlrender import get_new_page

#获取今日的每日一题标题，之后再另查询内容
def get_today_title():
    try:
        get_today_data = httpx.post("https://leetcode-cn.com/graphql", json={
            "query":"query questionOfToday {todayRecord { date question {frontendQuestionId: questionFrontendId difficulty titleSlug } } } ",
            "variables":{}
            })
        today_data = json.loads(get_today_data.text)
        titleSlug = today_data["data"]["todayRecord"][0]["question"]["titleSlug"]
        return titleSlug
    except Exception as e:
        raise e




#获取某一已知名称的题目内容
def get_sub_problem_data(titleSlug_):
    try:
        get_problem_data = httpx.post("https://leetcode-cn.com/graphql", json={
            "operationName": "questionData",
            "variables": {
                "titleSlug": titleSlug_ },
            "query": "query questionData($titleSlug: String!) { question(titleSlug: $titleSlug) { questionFrontendId title titleSlug translatedTitle translatedContent difficulty } } "
            })
        problem_data = json.loads(get_problem_data.text)
        problem_data = problem_data["data"]["question"]
        #题目信息(题号+题目译名)
        problem_title = problem_data.get("questionFrontendId")+"."+problem_data.get("translatedTitle")
        #题目难度(英语单词)
        problem_difficulty = "题目难度："+problem_data.get("difficulty")
        #题目内容（用html输出）
        problem_content = problem_data.get("translatedContent")
        ##去除转义
        problem_content.replace('\"','"')
        ##将html转为图片
        html_path = f"data/nonebot_plugin_leetcode/html"
        check_dir(html_path)
        with open(html_path+f"/{titleSlug_}.html","w+") as f:
            f.write(problem_content)
        problem_content = html2img(html_path+f"/{titleSlug_}.html",titleSlug_)
        #题目链接
        problem_link = "本题链接："+f"https://leetcode-cn.com/problems/{titleSlug_}/" 
        return [problem_title,problem_difficulty,problem_content,problem_link]
    except Exception as e:
        raise e

    

#直接用大佬的插件转化html！！！！yyds
async def html2img(path,title):
    try:
        async with get_new_page(viewport={"width": 300, "height": 300}) as page:
            await page.goto(
                "file://"+path,
                wait_until="networkidle"
            )
            img_path = f"data/nonebot_plugin_leetcode/img"
            check_dir(img_path)
            pic = await page.screenshot(full_page=True, path=img_path+f"/{title}.png")
            return pic
    except Exception as e:
        raise e


#网上找来的，创建不存在的目录
def check_dir(path):
    '''判断文件夹是否存在，如果不存在就创建一个'''
    if not os.path.isdir(path):
        os.makedirs(path)
        return "Create Successful."