import matplotlib.pyplot as plt
from matplotlib import font_manager
from pandas import DataFrame

# 本地适配:导入兜底,脚本方式(python run_case.py)与包方式均可运行
try:
    from news_case.config import CHART_DIR, FONT_CANDIDATES
except ImportError:
    from config import CHART_DIR, FONT_CANDIDATES


class NewsCharts(object):
    def __init__(self):
        CHART_DIR.mkdir(parents=True, exist_ok=True)
        self._setup_font()

    @staticmethod
    def _setup_font() -> None:
        """配置 matplotlib 中文显示."""
        # 查询当前计算机的可用字体
        available_fonts = {f.name for f in font_manager.fontManager.ttflist}
        for font_name in FONT_CANDIDATES:
            if font_name in available_fonts:
                plt.rcParams["font.sans-serif"] = [font_name]
                break
        plt.rcParams["axes.unicode_minus"] = False

    def create_bar(self, df: DataFrame):
        plt.bar(df["source_name"], df["news_count"])
        plt.savefig(CHART_DIR / "01.新闻来源柱状图.png")
        plt.close()

    def create_line(self, df: DataFrame):
        plt.plot(df["id"], df["title_length"])
        plt.savefig(CHART_DIR / "02.新闻标题长度变化.png")
        plt.close()

    def create_pie(self, df: DataFrame):
        plt.pie(df["keys_count"], labels=list(df["keyword"]))
        plt.savefig(CHART_DIR / "03.关键字分布.png")
        plt.close()

    def create_scatter(self, df: DataFrame):
        # 本地修复:兄弟版只 savefig 没画图,且文件名写错;补上散点绘制
        plt.scatter(df["id"], df["title_length"])
        plt.savefig(CHART_DIR / "04.新闻标题长度散点图.png")
        plt.close()
