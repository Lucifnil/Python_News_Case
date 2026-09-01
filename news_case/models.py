# 构建新闻对象的class
from dataclasses import dataclass


@dataclass
class NewsItem(object):
    title: str
    link: str
    pub_time: str
    keyword: str
    title_length: int
    source_name: str

    # def __init__(self, source_name, title, link, pub_time, keyword, title_length):
    #     self.title = title
    #     self.link = link
    #     self.pub_time = pub_time
    #     self.keyword = keyword
    #     self.title_length = title_length
    #     self.source_name = source_name
    # 后续会批量插入sqllite数据库 much([(source, "", "", "", "", "),(), (), (), ()])
    def to_row(self):
        return (self.source_name,
                self.title,
                self.link,
                self.pub_time,
                self.keyword,
                self.title_length)

    def __str__(self):
        return f"{self.source_name}-{self.title}"

