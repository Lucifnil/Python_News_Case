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