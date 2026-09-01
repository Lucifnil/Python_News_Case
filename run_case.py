import time

from news_case.utils import make_counter
from news_case.utils import timer


# 后续所有操作全部在run_case中展示整体的流程和步骤
def run_case():
    print("综合案例开始执行")
    counter = make_counter()
    print(f"步骤{counter()}:执行")
    print(f"步骤{counter()}:执行")
    print(f"步骤{counter()}:执行")
    test()
    test1()


@timer("测试函数")
def test():
    time.sleep(1)
    print("hello 测试")


@timer("网络抓取")
def test1():
    time.sleep(3)
    print("hello 测试")


if __name__ == '__main__':
    run_case()
