import asyncio

from news_case.utils import make_counter
from news_case.db import NewsDataBase
from news_case.fetcher import NewsFetcher


# 后续所有操作全部在run_case中展示整体的流程和步骤
def run_case():
    print("综合案例开始执行")
    counter = make_counter()
    db = NewsDataBase()
    fetcher = NewsFetcher()
    print(f"步骤{counter()}-初始化数据库")
    db.init_db()
    print(f"步骤{counter()}-抓取新闻数据")
    news_list = asyncio.run(fetcher.crawl_news())
    print(f"抓取到{len(news_list)}条新闻")
    print(f"步骤{counter()}-写入新闻到sqllite数据库")
    db.save_news(news_list)


if __name__ == '__main__':
    run_case()
