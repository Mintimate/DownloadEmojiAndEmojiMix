import json
import os
import random
import threading
from time import sleep

import requests

with open('errorJSON.json', 'r') as f:
    json_data_set = set()
    # 读取整个文件内容
    for line in f:
        element = line.strip()
        json_data_set.add(element)


def download_mix_png(json_object):
    root_png_dir = 'pngs/' + json_object['date'] + '/'
    if not os.path.exists(root_png_dir):
        os.makedirs(root_png_dir)
    left = "-".join(["u" + part.lower() for part in json_object['leftEmoji'].split("-")])
    right = "-".join(["u" + part.lower() for part in json_object['rightEmoji'].split("-")])
    date = json_object['date']
    download_url = f'https://www.gstatic.com/android/keyboard/emojikitchen/{date}/{left}/{left}_{right}.png'
    try:
        png = requests.get(download_url).content
        with open(root_png_dir + "{}_{}.png".format(left, right), 'wb') as f:
            f.write(png)
    except Exception as e:
        print("本次失败，失败任务内容{}".format(json_object))
        with open("./error.log", 'a') as f:
            f.write(json.dumps(json_object) + '\n')


def download(obj):
    download_mix_png(obj)
    print("任务编号{}: {}".format(count, obj))
    global thread_count
    thread_count -= 1


if __name__ == '__main__':
    count = 1
    threads = []
    MAX_THREADS = 30
    thread_count = 0
    for json_raw_data in json_data_set:
        obj = json.loads(json_raw_data)
        # 线程等待
        while thread_count >= MAX_THREADS:
            sleep(0.1)
        t = threading.Thread(target=download, args=(obj,))
        threads.append(t)
        thread_count += 1
        t.start()
        sleep_time = random.randint(1, 100) / 1000
        sleep(sleep_time)
        count += 1

    for t in threads:
        t.join()
