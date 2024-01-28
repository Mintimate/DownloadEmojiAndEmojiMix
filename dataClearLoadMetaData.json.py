import json

"""
desc: 加载MetaData数据，解析为Lite版本的EmojiOut.json
author: @Mintimate
authorLink: https://github.com/Mintimate
"""


def load_meta_data_to_set():
    """
    加载metadata
    :return:
    """
    with open('./metadata.json', 'r') as f:
        # 读取整个文件内容
        json_data = json.load(f)['data']
        return json_data


def key_value_reverse(emojis):
    index = {}
    for key, value in emojis.items():
        for word in value:
            if word not in index:
                index[word] = []
            index[word].append(key)
    return index


if __name__ == '__main__':
    keyword_dict = {}
    new_dict = {}
    emojiListCombinations = load_meta_data_to_set()
    for one_raw in emojiListCombinations:
        one_emoji_list = []
        emojiCombinations = emojiListCombinations[one_raw]['combinations']
        keyword_dict[one_raw] = emojiListCombinations[one_raw]['keywords']
        for emojiCombination in emojiCombinations:
            child_dict = {"leftEmoji": emojiCombination['leftEmojiCodepoint'],
                          "rightEmoji": emojiCombination['rightEmojiCodepoint'],
                          "date": emojiCombination['date']}
            one_emoji_list.append(child_dict)
        new_dict[one_raw] = one_emoji_list
    with open("keywords.json", "w") as file:
        keyword_dict = key_value_reverse(keyword_dict)
        json.dump(keyword_dict, file)
    with open('emojiOutputNew.json', 'w') as f:
        json.dump(new_dict, f)
