import os
import re
from custom_tools import add_mission_to_aria2

# 下载Webp的前缀
DOWNLOAD_PREFIX = "https://fonts.gstatic.com/s/e/notoemoji/latest/"
# SVG File Fir
SVG_DIR = "./svgs/"


def scan_svg_from_dir():
    """
    扫描目录下的svg文件
    :return:
    """
    svg_filename_list = []
    for dirpath, dirnames, filenames in os.walk(SVG_DIR):
        for filename in filenames:
            if filename.lower().endswith('.svg'):
                svg_filename_list.append(filename)
    return svg_filename_list


if __name__ == '__main__':
    svg_filename_list = set(scan_svg_from_dir())
    for item in svg_filename_list:
        # 下载SVG文件
        match = re.search(r"emoji_u([0-9a-f]+(?:_[0-9a-f]+)*)\.svg", item)
        if match:
            result = match.group(1)
            add_mission_to_aria2(DOWNLOAD_PREFIX + result + "/512.webp", output_name=result + ".webp")
