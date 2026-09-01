from pandas import DataFrame
import numpy as np
from news_case.config import CLEAN_CSV_PATH


class NewsAnalyzer(object):
    def __init__(self, df: DataFrame):
        # 复制一份dataFrame数据
        self.df = df.copy()

    # 清洗方法 df.dropna() df.fillna()
    def clean_data(self):
        # 去掉所有title为空的数据
        # subset的作用是只检查title这一列 这一列为空 这一行就删除
        #  self.df.dropna(how="any") -只要有一列为空就删除
        #  self.df.dropna(how="all") -全部列为空就删除
        #  self.df.dropna(subset=["列名"]) -某一列为空就删除

        self.df.dropna(subset=["title"], inplace=True)
        # 去除title前后的空白
        self.df["title"] = self.df["title"].str.strip()
        # 如果关键字中没有数据 就换成其他
        self.df["keyword"] = self.df["keyword"].replace("", np.nan).fillna("其他")
        # NaN fillna() -> 只能填nan
        # 希望把数据转成csv文件 可以去看
        # 如果文件不存在则创建该文件
        CLEAN_CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
        self.df.to_csv(CLEAN_CSV_PATH, index=False, encoding="utf-8-sig")
        return self.df

    # 按照新闻来源分组 source_name -统计数量
    def source_count(self):
        #  把统计的数量的列名设置为news_count
        return self.df.groupby("source_name")["id"].count().reset_index(name="news_count")

    def keyword_count(self):
        #  把统计的数量的列名设置为news_count
        return self.df.groupby("keyword")["id"].count().reset_index(name="keys_count")

    # 使用numpy计算平均值 标准差 最大值 最小值
    def title_length_stats(self):
        arr = self.df["title_length"].to_numpy()
        return {
            "平均长度": float(arr.mean()),
            "最大值": int(arr.max()),
            "最小值": int(arr.min()),
            "标准差": float(arr.std())
        }
# var 方差
# std 标准差
