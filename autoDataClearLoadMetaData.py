import json
import os

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


def make_lite_emoji_json(metaJsonFilePath, targetFilePath):
    keyword_dict = {}
    new_dict = {}
    emojiListCombinations = _load_meta_data_to_set(metaJsonFilePath)
    for one_raw in emojiListCombinations:
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
