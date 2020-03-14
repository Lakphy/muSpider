# muSpider

QQ音乐榜单爬取程序

声明： 仅供学习交流使用，转发请注明出处

为保证所有使用者利益，请控制使用频率！！！

## 快速开始

### 必要的准备

环境：Python

版本：>=3.5

相关库安装：对于大部分用户，一般情况不需要安装多余的库

若您使用过程中出现了因缺少库产生的问题，尝试在 shell / cmd / Powershell 中运行以下命令以安装缺少的库

```
pip insatll urllib
pip insatll time
pip insatll requests
pip install sys
pip insatll os
pip insatll datetime
pip insatll random
pip insatll pip
```

### 开始运行

下载文件并解压

在文件所在目录打开 shell / cmd / Powershell 运行

```
python music.pyc
```

即可开始运行

### 关于使用密码 (此功能已废除)

为防止被搬运，软件内设有动态密码验证，变化周期为小时

动态密码计算公式：

```python
key = str(int(int(datetime.date.today().strftime('%y%m%d'))%10+(int(datetime.date.today().strftime('%y%m%d'))%1000-int(datetime.date.today().strftime('%y%m%d'))%100)/100+(int(datetime.date.today().strftime('%y%m%d'))%100000-first%10000)/10000))+str(datetime.datetime.now().hour%10)+str((int(datetime.date.today().strftime('%y%m%d'))%10+datetime.datetime.now().hour%10)%10)
```

公式解释：

密码为三个数字的组合，中间无间隔；

第一个数为 当前月份的个位数 + 当前日期的个位数 + 当前年份的个位数；

第二个数为 当前小时数的个位数

第三个数为 ( 当前小时的个位数 + 当前日期的个位数 ) 除以10的余数

## FAQ   (常见问题及解答)

问：运行中间出现突然报错跳出？

答：可能是因为代理服务器不稳定或者您的网络不稳定所致，建议检测网络并重新打开程序



## 可以爬取的榜单

- [x] 流行指数榜

- [x] 欧美榜

- [x] 内地榜

- [x] iTunes榜

- [x] 香港地区榜

- [x] 台湾地区榜

- [x] 美国公告牌榜

- [x] 英国UK榜

- [x] YouTube榜

- [ ] 抖音排行榜

- [ ] 网络歌曲榜

- [ ] 电音榜

- [ ] 说唱榜

- [ ] ACG新歌榜

- [ ] 达人音乐榜

- [ ] K歌金曲榜

- [ ] JOOX本地热播榜

- [ ] 台湾KKBOX榜

## 榜单适配进度

由于每个榜单的爬取规则不同，请求参数不同，所以需要人工适配每一个榜单，工作量不小

学业繁忙，无法全部适配，望谅解

## 参与适配榜单

您不需要会编程即可参与适配

如果想要参与适配，您需要具备以下能力：

- 会进行网络抓包
- 能够分析抓包内容

仅需要这两样能力，您便可以贡献适配榜单

目前，我可以为您提供以下信息以减轻贡献适配榜单的工作量：

- 目标网页 [https://y.qq.com/n/yqq/toplist/4.html](https://y.qq.com/n/yqq/toplist/4.html)
- 包含榜单音乐id的文件为 musicu.fcg文件
- 上述大约在网页打开后3000-5000ms内出现

贡献者需要向我提供以下内容

- 请求url及参数
- 返回内容分析方法

贡献方式

1. 通过邮箱发给我，可以在[我的网站](https://lakphy.github.io)找到我的邮箱

2. 在本仓库下发布 issue

3. 通过各种可以联系到我本人的方式

