# 网易云音乐歌曲批量下载,免VIP,仅供测试用
网易云音乐歌曲批量下载目前支持歌单和排名榜，只要使用正确的URL则可以使用。

## 更新：
* 20180807 项目上传

## 要求（py脚本）
* python3+requests+wxpython+BeautifulSoup4+lxml+tqdm

## 文件结构：
```bash
├── dist
│   └── main.exe
├── GUI
│   └── pro-gui.fbp
├── images
│   ├── example.gif
├── README.md
├── src
│   ├── main.py
│   ├── main_noCli.py
```

## 使用方法
* main_noCli.py 是无界面命令行版
* 可从 dist 文件中直接下载 main.exe 使用或者直接 main.py

```
python3 src_noCli.py
# input examples
# playlist url:
# https://music.163.com/#/playlist?id=386407930
# save music path:
# /Volumes/HHD/Music/music
```
   
![](./images/example.gif)

## URL获取
![](./images/url.png)
