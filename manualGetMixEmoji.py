import json
import os
from aria2p import API, Client
from custom_tools import add_mission_to_aria2, config_dict

USER_CONFIG = config_dict()
# 下载Webp的前缀
DOWNLOAD_PREFIX = "https://www.gstatic.com/android/keyboard/emojikitchen/"
# JOSN文件
JSON_FILE_LITE = USER_CONFIG['emoji_lite']['save_path'] + "./emojiOutput.json"
JSON_FILE_FULL = USER_CONFIG['metadata_json']['save_path']


def get_download_url_from_lite():
    with open(JSON_FILE_LITE, 'r') as f:
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
        root_png_dir = 'pngs/' + obj['date'] + '/'
        if not os.path.exists(root_png_dir):
            os.makedirs(root_png_dir)
        left = "-".join(["u" + part.lower() for part in obj['leftEmoji'].split("-")])
        right = "-".join(["u" + part.lower() for part in obj['rightEmoji'].split("-")])
        date = obj['date']
        add_mission_to_aria2(f'https://www.gstatic.com/android/keyboard/emojikitchen/{date}/{left}/{left}_{right}.png')


def get_download_url_from_metadata():
    with open(JSON_FILE_FULL, 'r') as f:
        # 读取整个文件内容
        json_data = json.load(f)['data']
    # 遍历"data"内的对象
    for obj in json_data.values():
        # 获取每个对象的"combinations"数组
        combinations = obj['combinations']
        # 遍历"combinations"数组
        for combination in combinations:
            # 获取每个组合的"gStaticUrl"属性
            static_url = combination['gStaticUrl']
            add_mission_to_aria2(static_url)


if __name__ == '__main__':
    get_download_url_from_metadata()
