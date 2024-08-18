import json
import os
import re

from bs4 import BeautifulSoup

"""
desc: 加载MetaData数据，解析为Lite版本的EmojiOut.json
author: @Mintimate
authorLink: https://github.com/Mintimate
"""


def _load_meta_data_to_set(metaJsonFilePath):
    """
    加载metadata
    :return:
    """
    with open(metaJsonFilePath, 'r',encoding='utf-8') as f:
        # 读取整个文件内容
        json_data = json.load(f)['data']
        return json_data


def _key_value_reverse(emojis):
    index = {}
    for key, value in emojis.items():
        for word in value:
            if word not in index:
                index[word] = []
            index[word].append(key)
    return index


def __scan_available_emoji(svg_raw):
    with open(svg_raw, 'r', encoding='utf-8') as file:
        content = file.read()
    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(content, 'html.parser')
    # 查找所有的 img 标签
    imgs = soup.find_all('img')

    # 提取并返回所有 img 标签的 src 属性中的 emoji 代码
    emoji_codes = []
    for img in imgs:
        src = img.get('src')
        match = re.search(r'u([\w+]+)\.svg', src)  # 正则表达式匹配 u 后面的字符直到 .svg
        if match:
            emoji_code = match.group(1)  # 获取匹配到的组
            emoji_codes.append(emoji_code)

    return emoji_codes


def __check_string_against_set(s, check_set):
    """
    检查字符串是否包含在集合中
    :param s:
    :param check_set:
    :return:
    """
    # 使用 '-' 分割字符串
    parts = s.split('-')

    # 特殊处理：如果字符串中包含 'fe0f'直接返回True
    check_set.append('fe0f')

    # 检查分割后的每个部分是否在集合中
    for part in parts:
        if part in check_set:
            return True

    # 如果没有找到任何匹配项
    return False


def make_lite_emoji_json(metaJsonFilePath, targetFilePath):
    keyword_dict = {}
    new_dict = {}
    scan_available_emoji = __scan_available_emoji("./source/svg_raw.txt")
    emojiListCombinations = _load_meta_data_to_set(metaJsonFilePath)
    for one_raw in emojiListCombinations:
        if not __check_string_against_set(one_raw,scan_available_emoji):
            continue
        one_emoji_list = []
        emojiCombinations = emojiListCombinations[one_raw]['combinations']
        keyword_dict[one_raw] = emojiListCombinations[one_raw]['keywords']
        for emojiCombination in emojiCombinations:
            for emojiItem in emojiCombinations[emojiCombination]:
                child_dict = {"leftEmoji": emojiItem['leftEmojiCodepoint'],
                              "rightEmoji": emojiItem['rightEmojiCodepoint'],
                              "date": emojiItem['date']}
                one_emoji_list.append(child_dict)
        new_dict[one_raw] = one_emoji_list
    # 创建保存目录
    os.makedirs(os.path.dirname(targetFilePath), exist_ok=True)
    with open(targetFilePath + "keywords.json", "w") as file:
        keyword_dict = _key_value_reverse(keyword_dict)
        json.dump(keyword_dict, file)
    with open(targetFilePath + 'emojiOutput.json', 'w') as f:
        json.dump(new_dict, f)


if __name__ == '__main__':
    make_lite_emoji_json("./source/metadata.json", "./target/")
