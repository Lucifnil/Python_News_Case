# 闭包计数器
import re
import time
from functools import wraps


def make_counter():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner


# 清洗函数

# 时间装饰器
def timer(label):
    def outer(fn):
        @wraps(fn)
        def inner(*args, **kwargs):
            print(f"开始:{label}")
            start_time = time.time()
            res = fn(*args, **kwargs)
            print(f"结束: {label}, 耗时:{(time.time() - start_time):.4f}秒")
            return res

        return inner

    return outer


# 正则清洗函数
# 从网络上爬取的内容 需要进行清洗
# <![CDATA[示例：我国多地发布稳就业新举措]]> -> 示例：我国多地发布稳就业新举措
# () () () \1 \2 \3
def clean_text(text):
    # 这只是第一种情况
    # <![CDATA[示例：我国多地发布稳就业新举措]]> -> 示例：我国多地发布稳就业新举措

    text = re.sub(r"<!\[CDATA\[(.*?)\]\]>", r"\1", text)
    # <a>你好我是老高</a> -> 你好我是老高
    text = re.sub(r"<.*?>", "", text)
    # 去除一些空格
    # 我是你            爸爸         的       学生 -> 我是你 爸爸 的 学生
    text = re.sub(r"\s+", " ", text)

    # 百度 新浪 网易
    return text.strip()


print(clean_text("<![CDATA[示例：我国多地发布稳就业新举措]]>"))

print(clean_text("<a>我是你爸爸</a>"))

print(clean_text("我是你            爸爸         的       学生"))