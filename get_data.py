import httpx
import json



#获取今日的每日一题标题，之后再另外查询内容
async def get_today_title():
    get_today_data = httpx.post("https://leetcode-cn.com/graphql", json={
        "query":"query questionOfToday {todayRecord { date question {frontendQuestionId: questionFrontendId difficulty titleSlug } } } ",
        "variables":{}
        })
    today_data = json.loads(get_today_data.text)
    titleSlug = today_data["data"]["todayRecord"][0]["question"]["titleSlug"]
    return titleSlug




#获取某一已知名称的题目内容
def get_sub_problem_data(titleSlug_):
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
    return [problem_title,problem_difficulty,problem_content]