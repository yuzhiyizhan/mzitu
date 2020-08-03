# extensions.py
import os
import time
from loguru import logger
from scrapy import signals
from twisted.internet import task
from scrapy.exceptions import NotConfigured

try:
    from .settings import LOG
except:
    LOG = False

if LOG:
    LOG_PATH = os.getcwd()
    LOG_NAME = os.path.join(LOG_PATH, 'extensions.log')
    if not os.path.exists(LOG_PATH):
        os.mkdir(LOG_PATH)
    logger.add(LOG_NAME, level='INFO', rotation="10 MB", retention="7 days", backtrace=True, diagnose=True,
               enqueue=True,
               serialize=False)


def ritian(fn):
    def inner(*args, **kwargs):
        start = time.time()
        req = fn(*args, **kwargs)
        end = time.time()
        logger.info(f"方法{fn.__name__}运行时间:%.2f秒" % (end - start))
        return req

    return inner


class GeneralExtensions:
    def __init__(self, stats, interval=60.0):
        self.down = 0
        self.items = 0
        self.request = 0
        self.callback = 0
        self.task = None
        self.stats = stats
        self.error_urls = []
        self.interval = interval
        self.multiplier = 60.0 / self.interval

    @classmethod
    def from_crawler(cls, crawler):
        interval = crawler.settings.getfloat('LOGSTATS_INTERVAL')
        if not interval:
            raise NotConfigured
        s = cls(crawler.stats, interval)

        crawler.signals.connect(s.item_scraped, signal=signals.item_scraped)
        crawler.signals.connect(s.item_dropped, signal=signals.item_dropped)
        crawler.signals.connect(s.spider_error, signal=signals.spider_error)
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)
        crawler.signals.connect(s.request_scheduled, signal=signals.request_scheduled)
        return s

    def spider_opened(self, spider):
        self.pagesprev = 0
        self.itemsprev = 0
        self.task = task.LoopingCall(self.log, spider)
        self.task.start(self.interval)
        spider.logger.info('Spider opened: %s' % spider.name)
        self.start = time.time()
        self.start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.start))  # 转化格式

    def log(self, spider):
        items = self.stats.get_value('item_scraped_count', 0)
        pages = self.stats.get_value('response_received_count', 0)
        self.pagesprev, self.itemsprev = pages, items

    def request_scheduled(self, request, spider):
        self.request = self.request + 1

    def spider_error(self, failure, response, spider):
        self.callback = self.callback + 1
        self.error_urls.append(response.url)

    def item_scraped(self, item, response, spider):
        self.items = self.items + 1

    def item_dropped(self, item, spider, exception):
        self.callback = self.callback + 1
        self.error_urls.append(spider.url)

    def spider_closed(self, spider):
        self.end = time.time()
        Total_time = self.end - self.start
        m, s = divmod(Total_time, 60)
        h, m = divmod(m, 60)
        items = self.stats.get_value('item_scraped_count', 0)
        pages = self.stats.get_value('response_received_count', 0)
        request_down = self.stats.get_value('downloader/request_bytes', 0)
        response_down = self.stats.get_value('downloader/response_bytes', 0)
        irate = (items - self.itemsprev) * self.multiplier
        prate = (pages - self.pagesprev) * self.multiplier
        self.pagesprev, self.itemsprev = pages, items
        finish_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.end))  # 转化格式
        logger.info(f'开始时间  --  {self.start_time}')
        logger.info(f'结束时间  --  {finish_time}')
        logger.info(f'成功请求网页  --  {self.request}次')
        logger.info(f'成功下载item  --  {self.stats.get_value("file_count", 0)}次')
        logger.info(f'失败请求  --  {self.callback}次')
        logger.info(f'总请求次数  --  {self.stats.get_value("downloader/request_count", 0)}次')
        for url in self.error_urls:
            logger.info(f'请求失败的url:  --  {url}')
        logger.info(f"每分钟请求页面 {pages}d pages ({prate} pages/min)")
        logger.info(f'每分钟下载 {items}d items ({irate} items/min)')
        logger.info(f'请求数据量  --  {self.gen_atta_size_count(request_down)}')
        logger.info(f'下载数据量  --  {self.gen_atta_size_count(response_down)}')
        logger.info(f'总耗时  --  {h}时:{m}分:{s}秒')
        logger.info(f'memusage/max:{self.gen_atta_size_count(self.stats.get_value("item_scraped_count", 0))}')

    def gen_atta_size_count(self, con):  # 参数可以是任意数据类型
        if con:
            size_b = con
            size = str(size_b) + 'B'
            size_k = size_b / 1024
            if size_k > 1:
                size = '%.1f' % size_k + 'K'
                size_m = size_k / 1024
                if size_m > 1:
                    size = '%.2f' % size_m + 'M'
                    size_g = size_m / 1024
                    if size_g > 1:
                        size = '%.3f' % size_g + 'G'
        else:
            size = "0B"
        return size