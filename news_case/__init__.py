"""
    __init__.py 是包标记。有了它，才能写 from news_case.db import NewsDatabase 这种导入。
    1. 存在 __init__.py 的文件夹，会被 Python 识别为【包（package）】，而不是普通文件夹
    2. 控制包对外暴露的内容（__all__）
    3. 包初始化逻辑（import 包时自动执行里面代码）
    4. 子包 / 模块导入重导出（简化外部导入路径）
"""