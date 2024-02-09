import json


def load_meta_data_to_set():
    """
    加载metadata
    :return:
    """
    with open('./keywords.json', 'r') as f:
        # 读取整个文件内容
        json_data = json.load(f)
        return json_data


if __name__ == '__main__':
    words_list_result = []
    words_list = load_meta_data_to_set()
    for item in words_list:
        words_list_result += words_list[item]
    with open("keywordsSource.json", "w") as file:
        # 将列表中的元素逐行写入文件
        for item in set(words_list_result):
            file.write(item + ',')