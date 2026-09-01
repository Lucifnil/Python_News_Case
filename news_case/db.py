try:
    from .config import DB_PATH, SCHEMA_PATH
    from .models import NewsItem
except ImportError:
    from config import DB_PATH, SCHEMA_PATH
    from models import NewsItem
import pandas as pd
import sqlite3


class NewsDataBase(object):
    def __init__(self, db_path=DB_PATH):
        # sqllite3 只需要一个路径 存储数据库
        # 不传路径的情况下 使用dbpath
        self.db_path = db_path

    # 连接方法 每次操作数据库  都需要 connect连接 创建游标 执行sql 提交 关闭
    def connect(self):
        # 如果路径不存在这创建
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        return sqlite3.connect(self.db_path)
        # 建立数据库建立 不需要 host 端口 密码 不需要账号 不需要数据库名称

    # 初始化数据库
    def init_db(self):
        # 在引用启动流程的时候 需要建立table
        # 把 文件的sql的内容一次读取过来 然后交给sqllite来执行就行了
        # Path对象可以读写文件 可以创建目录
        sql = SCHEMA_PATH.read_text(encoding="utf-8")
        with self.connect() as conn:
            # 创建游标对象
            cursor = conn.cursor()
            # 执行建表的脚本
            cursor.executescript(sql)
            conn.commit()
            cursor.close()

        pass

    # 插入新闻
    def save_news(self, news_list:list[NewsItem]):
        # insert into news (source_name, title, link,pub_time,keyword, title_length) values (?,?,?,?,?,?)
        with self.connect() as conn:
            cursor = conn.cursor()
            # 清空新闻表数据
            cursor.execute("delete from news")
            cursor.executemany("""
            insert into news
            (source_name, title, link,pub_time,keyword, title_length)
            values (?,?,?,?,?,?)
            """, [item.to_row() for item in news_list])
            # 推导式 [i for i in range(10)] (i for i in range(10))
            conn.commit()
            cursor.close()
        pass
    # 读取新闻 Series DataFrame
    def read_news_df(self):
        with self.connect() as conn:
            return pd.read_sql_query("select * from news order by id",conn)

    pass

if __name__ == "__main__":
    NewsDataBase().init_db()