import json

with open('emojiOutput.json', 'r') as f:
    # 读取整个文件内容
    data = f.read()
    # 解析JSON数据
    json_data = json.loads(data)

if __name__ == '__main__':
    new_set = set()
    for src_path in json_data:
        for obj in json_data[src_path]:
            new_set.add(json.dumps(obj))
    with open("emojiOutputSet.json", "w") as file:
        for element in new_set:
            file.write(element + "\n")
