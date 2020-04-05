1.看到github上面开源的爬妹子图的项目,似乎没有爬取全站图片的项目,开源此项目,求轻喷

2.本项目使用的代理池地址:

如不用此代理池,请自行更改middlewares.py

此项目也是本人的,有问题请及时联系我QQ:1016682256

https://github.com/yuzhiyizhan/spidery

3.配置好代理池配置后安装本项目依赖的环境

pip install -r requirements.txt -i https://pypi.douban.com/simple/

4.命令行进入项目启动爬虫(建议不用其他方式)

scrapy crawl mezitu

5.使用本项目默认配置需要爬取20小时左右,本人测试环境如下:

Ubuntu 18.04.4 LTS

processor	: 0
vendor_id	: GenuineIntel
cpu family	: 6
model		: 42
model name	: Intel(R) Core(TM) i3-2350M CPU @ 2.30GHz
stepping	: 7
microcode	: 0x2f
cpu MHz		: 888.426
cache size	: 3072 KB
physical id	: 0
siblings	: 4
core id		: 0
cpu cores	: 2
apicid		: 0
initial apicid	: 0
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic popcnt tsc_deadline_timer xsave avx lahf_lm epb pti ssbd ibrs ibpb stibp tpr_shadow vnmi flexpriority ept vpid xsaveopt dtherm arat pln pts md_clear flush_l1d
bugs		: cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf mds swapgs itlb_multihit
bogomips	: 4589.41
clflush size	: 64
cache_alignment	: 64
address sizes	: 36 bits physical, 48 bits virtual
power management:

processor	: 1
vendor_id	: GenuineIntel
cpu family	: 6
model		: 42
model name	: Intel(R) Core(TM) i3-2350M CPU @ 2.30GHz
stepping	: 7
microcode	: 0x2f
cpu MHz		: 859.083
cache size	: 3072 KB
physical id	: 0
siblings	: 4
core id		: 1
cpu cores	: 2
apicid		: 2
initial apicid	: 2
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic popcnt tsc_deadline_timer xsave avx lahf_lm epb pti ssbd ibrs ibpb stibp tpr_shadow vnmi flexpriority ept vpid xsaveopt dtherm arat pln pts md_clear flush_l1d
bugs		: cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf mds swapgs itlb_multihit
bogomips	: 4589.41
clflush size	: 64
cache_alignment	: 64
address sizes	: 36 bits physical, 48 bits virtual
power management:

processor	: 2
vendor_id	: GenuineIntel
cpu family	: 6
model		: 42
model name	: Intel(R) Core(TM) i3-2350M CPU @ 2.30GHz
stepping	: 7
microcode	: 0x2f
cpu MHz		: 919.730
cache size	: 3072 KB
physical id	: 0
siblings	: 4
core id		: 0
cpu cores	: 2
apicid		: 1
initial apicid	: 1
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic popcnt tsc_deadline_timer xsave avx lahf_lm epb pti ssbd ibrs ibpb stibp tpr_shadow vnmi flexpriority ept vpid xsaveopt dtherm arat pln pts md_clear flush_l1d
bugs		: cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf mds swapgs itlb_multihit
bogomips	: 4589.41
clflush size	: 64
cache_alignment	: 64
address sizes	: 36 bits physical, 48 bits virtual
power management:

processor	: 3
vendor_id	: GenuineIntel
cpu family	: 6
model		: 42
model name	: Intel(R) Core(TM) i3-2350M CPU @ 2.30GHz
stepping	: 7
microcode	: 0x2f
cpu MHz		: 952.039
cache size	: 3072 KB
physical id	: 0
siblings	: 4
core id		: 1
cpu cores	: 2
apicid		: 3
initial apicid	: 3
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic popcnt tsc_deadline_timer xsave avx lahf_lm epb pti ssbd ibrs ibpb stibp tpr_shadow vnmi flexpriority ept vpid xsaveopt dtherm arat pln pts md_clear flush_l1d
bugs		: cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf mds swapgs itlb_multihit
bogomips	: 4589.41
clflush size	: 64
cache_alignment	: 64
address sizes	: 36 bits physical, 48 bits virtual
power management:

              总计         已用        空闲      共享    缓冲/缓存    可用
内存：        3909        2834         257         113         817         679
交换：        2047         167        1880

配置还是挺差的

6.效果图

![效果图](https://github.com/yuzhiyizhan/mzitu/blob/master/%E6%95%88%E6%9E%9C%E5%9B%BE.png)

7.本项目配置如下:

# 包括第一次下载，最多的重试次数(代理比较差,或者网络不稳时,此值应加大)
RETRY_TIMES = 5

#设置延迟(避免封ip)
DOWNLOAD_DELAY = 0

#要加快爬取速度下面的值适当加大

CONCURRENT_REQUESTS
默认: 16

Scrapy downloader 并发请求(concurrent requests)的最大值。

CONCURRENT_REQUESTS_PER_DOMAIN
默认: 16

对单个网站进行并发请求的最大值。

CONCURRENT_REQUESTS_PER_IP
默认: 16

对单个IP进行并发请求的最大值。如果非0，则忽略 CONCURRENT_REQUESTS_PER_DOMAIN 设定， 使用该设定。 也就是说，并发限制将针对IP，而不是网站。

该设定也影响 DOWNLOAD_DELAY: 如果 CONCURRENT_REQUESTS_PER_IP 非0，下载延迟应用在IP而不是网站上。

# 下载器超时时间(单位: 秒)
DOWNLOAD_TIMEOUT = 5

#图片保存的文件夹,如果不喜欢请自行修改pipelines的MZFilesPipline
FILES_STORE = 'image'

Q:我不想爬那么多只想爬一两页怎么办?

A:修改meizitu.py里的start_urls将下面的for循环注释掉(建议这么做,万一那天想通了怎么办)

将要爬的页数以列表形式放入start_url,只爬一个套图的建议用手采集

Q:我想爬全站的但是房东说明天断我的电怎么办?

A:参考scrapy的断点续爬 https://doc.scrapy.org/en/latest/topics/jobs.html?highlight=jobdir

或者:https://blog.csdn.net/weixin_44461123/article/details/98478256

Q:为什么爬的图片不全？

A:因为没钱所以使用免费的代理,建议将重试次数调大,延迟设置高点,下载器超时加长

有钱可以去买代理然后自行添加到中间件,或者添加至代理池中

Q:想顺着网线打你怎么办?

A:有意见的或者有其他好的想法可以加我QQ1016682256

或者直接再项目下面留言,怎么留言我也不会,日后添加

最后,如有问题或建议请及时联系,加好友留个备注
