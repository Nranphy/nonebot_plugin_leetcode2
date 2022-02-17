import httpx
import json
from nonebot_plugin_htmlrender import get_new_page

#获取今日的每日一题标题，之后再另外查询内容
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
        #题目难度
        problem_difficulty = "题目难度："+problem_data.get("difficulty")
        #题目内容（用html输出）
        problem_content = problem_data.get("translatedContent")
        ##去除转义
        problem_content.replace('\"','"')
        ##将html转为图片
        with open(f"/data/nonebot_plugin_leetcode/html/{titleSlug_}.html","w+") as f:
            f.write(problem_content)
        problem_content = html2img(f"/data/nonebot_plugin_leetcode/html/{titleSlug_}.html",titleSlug_)
        #题目链接
        problem_link = "本题链接："+f"https://leetcode-cn.com/problems/{titleSlug_}/" 
        return [problem_title,problem_difficulty,problem_content,problem_link]
    except Exception as e:
        raise e

    

#直接用大佬的插件转化html！！！！
async def html2img(path,title):
    try:
        async with get_new_page(viewport={"width": 300, "height": 300}) as page:
            await page.goto(
                path,
                wait_until="networkidle"
            )
            pic = await page.screenshot(full_page=True, path=f"/data/nonebot_plugin_leetcode/html/{title}.png")
            return pic
    except Exception as e:
        raise e