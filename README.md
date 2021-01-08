# PowerSpider

![](https://img.shields.io/badge/python-3.6%2B-brightgreen)

PowerSpider基于requests、lxml、封装成简单的爬虫。将给您避免大量的重复工作

便捷易用的PowerSpider提供以下功能

* 智能化解析编码(二进制、中文、英文更多)
* 解放双手，开箱即用。

PowerSpider 原理可参见[释放双手，封装爬虫](https://mp.weixin.qq.com/s/pMnqFtTff93teAR81MrTZw)

## 使用要求

* Python 版本不低于3.6
* gcc 正常且完成安装

### 安装依赖包

强烈推荐使用 [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands)
或 [virtualenv](https://virtualenv.pypa.io/en/latest/user_guide.html) 创建虚拟环境，Python 版本不低于 3.6。

```shell
# 推荐使用
sh installScript.sh
# pip 常规安装依赖
pip install -r requirements.txt
# 使用清华源镜像安装
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 运行示例

```python3
from powerspider.Download import downloader

print(downloader("https://www.baidu.com")[:100])

# 2020-11-09 16:08:35.365 | INFO     | powerspider.Download:downloader:7 - Scraping https://www.baidu.com
# <!DOCTYPE html>
# <!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charse
# 2020-11-09 16:08:37.744 | INFO     | powerspider.Download:downloader:18 - Redirect_URL: https://www.baidu.com/
```

## 待开发
- [ ] 模块化解析
- [ ] 存储封装

欢迎大家start,issue,fork


