import json
import os
from aria2p import API, Client
from custom_tools import add_mission_to_aria2

# 下载Webp的前缀
DOWNLOAD_PREFIX = "https://www.gstatic.com/android/keyboard/emojikitchen/"
# JOSN文件
JSON_FILE = "./emojiOutputNew.json"


def get_download_url(json_object):
    root_png_dir = 'pngs/' + json_object['date'] + '/'
    if not os.path.exists(root_png_dir):
        os.makedirs(root_png_dir)
    left = "-".join(["u" + part.lower() for part in json_object['leftEmoji'].split("-")])
    right = "-".join(["u" + part.lower() for part in json_object['rightEmoji'].split("-")])
    date = json_object['date']
    return f'https://www.gstatic.com/android/keyboard/emojikitchen/{date}/{left}/{left}_{right}.png'


if __name__ == '__main__':
    with open(JSON_FILE, 'r') as f:
        json_data_set = set()
        data_of_source_json = json.load(f)
        # 读取整个文件内容
        for line in data_of_source_json:
            element = data_of_source_json[line]
            for item in element:
                json_data_set.add(json.dumps(item))
    for json_raw_data in json_data_set:
        # 解析JSON数据
        obj = json.loads(json_raw_data)
        # 获取下载链接
        download_url = get_download_url(obj)
        # 添加下载任务
        add_mission_to_aria2(download_url)
