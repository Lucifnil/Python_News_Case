# URL、关键词、路径这些通常会在配置文件中统一管理，避免多次修改和硬编码

# 使用pathlib获取当前脚本包的路径
from pathlib import Path

# 获取当前脚本包的路径的父目录，即项目根目录
PACKAGE_DIR = Path(__file__).resolve().parent

# 获取项目根目录
PROJECT_DIR = PACKAGE_DIR.parent

# 定义数据库的路径
DB_PATH = PROJECT_DIR / "sql" / "schema.sql"

# 定义matplotlib图片的保存路径
CHARTS_DIR = PROJECT_DIR / "charts"

# 定义csv文件的保存路径
CLEAN_CSV_DIR = PROJECT_DIR / "output" / "clean_news.csv"

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
