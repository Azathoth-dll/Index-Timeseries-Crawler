# 脚本说明
## 1.运行环境
### 1.1 python版本
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;此脚本编写时运行在python3.11.6版本下，请保证电脑中可用的python版本在此版本以上。
### 1.2 Chromium
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Chromium是谷歌发布的Chrome浏览器的内核，相当于一个简化的浏览器，此脚本运行在**1132420**版本上，请保证电脑中的本地Chromium版本在此版本以上。
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;由于此脚本中使用的爬虫框架Pyppeteer的特性，在第一次启动时会自动从googleAPI下载并安装Chromium，但是因为地理因素总会下载失败，所以作者提供了两种替代方法作为替代：
1. 使用国内镜像源。作者也给出了配置国内镜像源的方法，在source_pyppeteer.py文件的头部插入如下部分：
    ```python
    # Chromium initialize
    import Chromium_Initialize
    Chromium_Initialize.download_chromium()
    ```
    通过IDE运行此文件或者通过在命令行工具中键入`python source_pyppeteer`即可初始化Chromium。完成安装后，**命令行中会显示Chromium的安装路径**，将此路径填入`source_pyppeteer.py`文件中`chromium_path`变量。
2. 使用作者提供的Chromium组件，作者在此脚本的相同目录下提供了`Chromium_1132420_win_x64.zip`压缩包，将其解压后，获取`Chrome.exe`的路径并将其填入`source_pyppeteer.py`文件中`chromium_path`变量。

`chromium_path`例：
```python
chromium_path = "$Path$"
```
### 1.3 依赖包
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;本脚本中`pyppeteer`,`asyncio`并非为python自带的模块，需要手动安装。通过在命令行中逐行键入一下命令安装：
```
pip install pyppeteer
pip install asyncio
```
