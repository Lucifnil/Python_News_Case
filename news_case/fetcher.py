# 爬虫请求核心
import asyncio
from urllib.request import Request, urlopen
from news_case.config import SOURCES
import ssl


# 1.Request 构建请求对象
# 2.urlopen 用来发起请求

class BaseFetcher(object):
    # 网络请求的核心方法
    def load(self, url):
        # 1.构建request对象
        # 有的网站判断UA-User-Agent
        # 判断来源是不是正常的属性
        # 关闭ssl的证书校验
        ctx = ssl.create_default_context()
        # 关闭证书校验
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        req = Request(url, headers={
            # 模拟真实的浏览器UA
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })
        # 2.发起网络请求 TCP协议
        # 使用with可以自动释放占用的文件资源
        with urlopen(req, context=ctx, timeout=10) as f:
            # errors="ignore" 遇到无法解码的字符直接忽略
            return f.read().decode("utf-8", errors="ignore")


# 子类负责 所有来源数据的请求 汇总 -> [NewsItem, NewsItem] -> SqlLite -> Pandas/Numpy -> Matplotlib
class NewsFetcher(BaseFetcher):
    # 爬取一个
    async def fetch_one(self, source):
        # 返回当前源的html内容
        try:
            # 将一个普通函数转化成可等待对象
            html = await asyncio.to_thread(self.load, source["url"])
            return source["name"], html
        except Exception as e:
            print(f"抓取失败:{source['name']}", e)
            return source["name"], source["sample"]
        # { "name": "中新闻“， html: 'xxxx' }

    # 爬取所有
    async def fetch_all(self):
        # 针对来源的每一条进行爬取
        #
        # asyncio.gather(任务1， 任务2)
        # 生成一个列表 [等待任务1，等待任务2] -所有等待任务都结束 返回一个结果
        # [(name, html),(name, html)，(name，html)]
        # tasks = []
        # for source in SOURCES:
        #     task = self.fetch_one(source)
        #     tasks.append(task)
        # res = await asyncio.gather(*tasks)
        # return res
        return await asyncio.gather(*[self.fetch_one(source) for source in SOURCES])

    async def crawl_news(self):
        html_list = await self.fetch_all()
        for name, html in html_list:
            print(name, html)
        return html_list


# 基础BaseFetcher负责网络爬取内容

# NewsFetcher继承BaseFetcher,负责数据协程并发 网络发起，正则匹配，垃圾处理
# print(asyncio.run(NewsFetcher().crawl_news()))
# 证书 mac版本 没有ssl证书
# asyncio.create_task(函数名(), 参数)
# asyncio.to_thread(函数名, 参数) - 把一个非等待对象转化等待对象实现并发
# await 只能可等待对象
# asyncio.gather(任务1，任务2，任务3， 任务4)

asyncio.run(NewsFetcher().crawl_news())
