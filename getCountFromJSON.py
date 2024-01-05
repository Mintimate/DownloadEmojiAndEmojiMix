import json

with open('emojiOutput.json', 'r') as f:
    # 读取整个文件内容
    data = f.read()
    # 解析JSON数据
    json_data = json.loads(data)

if __name__ == '__main__':
    for one_raw in json_data:
        print("Hello, Emoji: emoji_u{}".format(one_raw))