from news_case.utils import make_counter

def run_case():
    print("综合案例开始执行")
    counter = make_counter()
    print(counter())
    print(counter())

# 运行综合案例的入口,判断当前模块是否是主模块（即是否直接执行该脚本）
if __name__ == "__main__":
    run_case()