# -*- coding: utf-8 -*-

# Scrapy settings for mztu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
BOT_NAME = 'mztu'

SPIDER_MODULES = ['mztu.spiders']
NEWSPIDER_MODULE = 'mztu.spiders'
# TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'mztu (+http://www.yourdomain.com)'
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# 是否启用logging
# LOG_ENABLED = False
# MEMUSAGE_NOTIFY_MAIL = ['1016682256@qq.com']
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# Scrapy downloader 并发请求(concurrent requests)的最大值
# CONCURRENT_REQUESTS = 100
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32
# 包括第一次下载，最多的重试次数
RETRY_TIMES = 100
# CONCURRENT_ITEMS = True
# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS = 64
CONCURRENT_REQUESTS_PER_DOMAIN = 64
CONCURRENT_REQUESTS_PER_IP = 64

# Disable cookies (enabled by default)
COOKIES_ENABLED = False
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'referer': 'https://www.mzitu.com/japan/',
}
# 下载器超时时间(单位: 秒)
DOWNLOAD_TIMEOUT = 10
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'mztu.middlewares.MztuSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html

DOWNLOADER_MIDDLEWARES = {
    # 'mztu.middlewares.UserAgentDownloadMiddleware': 99,
    'mztu.middlewares.IPProxyDownloadMiddleware': 543,
    'mztu.middlewares.RequestLOGDownloadMiddleware': 544,
}
# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
    # 'scrapy.extensions.telnet.TelnetConsole': None,
    'mztu.extensions.GeneralExtensions': 300,
}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'scrapy.pipelines.images.ImagesPipeline': 1,
    # 'scrapy.pipelines.files.FilesPipeline': 1,
    'mztu.pipelines.MztuPipeline': 1,
}
# IMAGES_STORE = 'MZtu'
FILES_STORE = 'image'
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
