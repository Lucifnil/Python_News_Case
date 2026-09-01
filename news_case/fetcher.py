# 爬虫请求核心
from urllib.request import Request, urlopen
import  ssl


# 1.Request 构建请求对象
# 2.urlopen 用来发起请求

class BaseFetcher(object):
    # 网络请求的核心方法
    def load(self, url):
        # 1.构建request对象
        # 有的网站判断UA-User-Agent
        # 判断来源是不是正常的属性
        # 关闭ssl的证书校验
        ctx = ssl.create_default_context()
        # 关闭证书校验
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        req = Request(url, headers={
            # 模拟真实的浏览器UA
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })
        # 2.发起网络请求 TCP协议
        # 使用with可以自动释放占用的文件资源
        with urlopen(req, context=ctx, timeout=10) as f:
            # errors="ignore" 遇到无法解码的字符直接忽略
            return f.read().decode("utf-8", errors="ignore")


class NewsFetcher(BaseFetcher):
    pass


# 基础BaseFetcher负责网络爬取内容

# NewsFetcher继承BaseFetcher,负责数据协程并发 网络发起，正则匹配，垃圾处理
print(NewsFetcher().load("https://www.163.com"))
# 证书 mac版本 没有ssl证书
