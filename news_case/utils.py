# 闭包计数器
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
