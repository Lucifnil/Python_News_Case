from pathlib import Path

# 包含当前的路径

# 当前脚本包的路径
# __file__

# print(__file__)
# 表示得到当前脚本执行路径的绝对路径对象
PACKAGE_DIR = Path(__file__).resolve().parent

# 项目根目录
PROJECT_DIR = PACKAGE_DIR.parent

# 需要一个数据库脚本文件的路径 sql/schema.sql

DB_PATH = PROJECT_DIR / "sql" / "schema.sql"

# 还要一个matplotlib 图片的保存目录
CHART_DIR = PROJECT_DIR / "output" / "charts"

# csv文件存储的路径
CLEAN_CSV_PATH = PROJECT_DIR / "output" / "clean_news.csv"


# 关键词列表：后面做简单统计时会用到
KEYWORDS = [
    "中国",
    "经济",
    "科技",
    "教育",
    "AI",
    "市场",
    "就业",
    "消费",
    "恋爱",
    "青蛙",
    "程序员",
    "访问",
    "裁员",
    "互联网",
    "人事",
    "情感",
    "美国",
    "Agent",
    "OpenAI"
]

# Matplotlib 中文字体候选，谁可用就用谁
FONT_CANDIDATES = [
    "PingFang SC",
    "Microsoft YaHei",
    "SimHei",
    "Arial Unicode MS",
]

# 新闻源配置
SOURCES = [
    {
        "name": "中新网滚动",
        "url": "https://www.chinanews.com.cn/rss/scroll-news.xml",
        "sample": """
            <rss>
                <channel>
                    <title>中新网滚动</title>
                    <item>
                        <title><![CDATA[示例：我国多地发布稳就业新举措]]></title>
                        <link>https://example.com/news-1</link>
                        <pubDate>Wed, 27 Aug 2026 08:30:00 GMT</pubDate>
                    </item>
                    <item>
                        <title><![CDATA[示例：人工智能产业链迎来新进展]]></title>
                        <link>https://example.com/news-2</link>
                        <pubDate>Wed, 27 Aug 2026 09:00:00 GMT</pubDate>
                    </item>
                </channel>
            </rss>
        """,
    },
    {
        "name": "人民网时政",
        "url": "http://www.people.com.cn/rss/politics.xml",
        "sample": """
            <rss>
                <channel>
                    <title>人民网时政</title>
                    <item>
                        <title><![CDATA[示例：多地加快推进教育数字化建设]]></title>
                        <link>https://example.com/news-3</link>
                        <pubDate>Wed, 27 Aug 2026 09:30:00 GMT</pubDate>
                    </item>
                    <item>
                        <title><![CDATA[示例：消费市场延续稳定恢复态势]]></title>
                        <link>https://example.com/news-4</link>
                        <pubDate>Wed, 27 Aug 2026 10:00:00 GMT</pubDate>
                    </item>
                </channel>
            </rss>
        """,
    },
]


