import setuptools

setuptools.setup(
    name='nonebot_plugin_leetcode2',
    version='1.1.3',
    author='Nranphy',
    author_email='3102002900@qq.com',
    url='https://github.com/Nranphy/nonebot_plugin_leetcode2',
    description="基于nonebot2的leetcode查询插件。",
    long_description=u'一个基于nonebot2的leetcode查询插件，可以查询用户和题目，包含每日一题和随机一题，并可以每日定时发送题目。',
    packages=setuptools.find_packages(),
    install_requires=[
        "httpx",
        "nonebot-plugin-htmlrender",
        "nonebot-plugin-apscheduler"
        ],
)