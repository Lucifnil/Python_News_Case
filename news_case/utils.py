# 闭包三要素：
# 1. 必须有一个嵌套函数
# 2. 嵌套函数必须引用外部函数的变量
# 3. 外部函数的返回值必须是嵌套函数

# 闭包计数器
def make_counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

# 时间装饰器


# 正则清洗函数