import platform
from scrapy import cmdline

if platform.system() == "Windows":
    import asyncio
    # asyncio.Semaphore(500)
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
cmdline.execute(['scrapy', 'crawl', 'mezitu'])
