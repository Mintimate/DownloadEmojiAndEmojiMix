"""
用于手动解析Emoji Kitchen（https://emojikitchen.dev/）的 Emoji SVG文件

@author: Mintimate
@createTime: 2024/02/08
"""
import os
import re
import time

import requests
from custom_tools import add_mission_to_aria2, config_dict, say_somethings
from bs4 import BeautifulSoup
from selenium import webdriver

USER_CONFIG = config_dict()
# SVG 的保存地址（手动下载的情况下）
SVG_DIC = USER_CONFIG['svg_raw']
SVG_TARGET = USER_CONFIG['svg_target']


def download_svg_main():
    with open(SVG_DIC, 'r') as f:
        # 读取整个文件内容
        SVG_RAW = f.read()
    pattern = r'src="(.*?\.svg)"'
    matches = re.findall(pattern, SVG_RAW)
    count = 1
    for src_path in matches:
        say_somethings("{}下载文件: {}".format(count, src_path.split('/')[-1]))
        count = count + 1
        # _download_svg(src_path)
        # 使用 Aria2 进行多线程的异步下载
        add_mission_to_aria2(src_path, None)


def _download_svg(src_path):
    """
    使用 requests 手动下载
    :param src_path:
    :return:
    """
    os.makedirs(os.path.dirname(SVG_TARGET), exist_ok=True)
    if not os.path.exists(SVG_TARGET):
        os.makedirs(SVG_TARGET)
    svg = requests.get(src_path).content
    with open(SVG_TARGET + src_path.split('/')[-1], 'wb') as f:
        f.write(svg)


def scan_svg_raw():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("https://emojikitchen.dev/")
    # 等待5秒让页面完全渲染
    time.sleep(5)
    # 获取页面源代码
    page_source = driver.page_source
    # 关闭浏览器
    driver.quit()
    soup = BeautifulSoup(page_source, 'html.parser')
    # 找到第一个 class 为 "MuiBox-root css-1uithqi" 的 div
    target_div = soup.find('div', class_='MuiBox-root css-1uithqi')
    # 获取该 div 内的全部内容
    content = target_div.prettify()
    # 将内容写入文件
    with open('source/svg_raw.txt', 'w', encoding='utf-8') as file:
        file.write(content)


if __name__ == '__main__':
    scan_svg_raw()
