from datetime import datetime

import yaml
from aria2p import Client, API


def config_dict():
    """
    加载配置文件
    :return:
    """

    # 读取配置文件
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
        return config


def say_somethings(message, print_time=True):
    """
    打印信息
    :return:
    """
    if print_time:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{current_time}] {message}")
    else:
        print(message)


def add_mission_to_aria2(mission_url, output_name, print_mission_GID=True):
    """
    添加下载任务到Aria2
    :param mission_url:
    :param output_name: 文件的输出名称(需要包含文件名的后缀，e.g. Emoji.webp)
    :param print_mission_GID: 是否打印当前任务的GID
    :return:
    """
    config = config_dict()
    aria2_host = config['aira2']['host']
    aria2_port = config['aira2']['port']
    aria2_secret = config['aira2']['secret']
    # 创建 Aria2p client 实例
    aria2p_client = Client(host=aria2_host, port=aria2_port, secret=aria2_secret)
    api = API(aria2p_client)
    # 添加下载任务
    download = api.add_uris([mission_url], {'out': output_name})
    if print_mission_GID:
        say_somethings(f"Download Mission Added With GID: {download.gid}")