import os
import re
from time import sleep

import requests

with open('svg_raw.txt', 'r') as f:
    # 读取整个文件内容
    SVG_RAW = f.read()


def download_svg(src_path):
    svg_dir = 'svgs/'
    if not os.path.exists(svg_dir):
        os.makedirs(svg_dir)
    svg = requests.get(src_path).content
    with open(svg_dir + src_path.split('/')[-1], 'wb') as f:
        f.write(svg)


if __name__ == '__main__':
    pattern = r'src="(.*?\.svg)"'
    matches = re.findall(pattern, SVG_RAW)
    count = 1
    for src_path in matches:
        print("{}下载文件: {}".format(count, src_path.split('/')[-1]))
        count = count + 1
        download_svg(src_path)
