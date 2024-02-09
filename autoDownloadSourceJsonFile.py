import os
import requests


def download_metadata(url, save_path):
    """
    从给定的URL下载元数据并将其保存到指定路径。

    参数:
        url (str): 要下载的文件的URL。
        save_path (str): 下载文件将保存的路径。

    异常:
        Exception: 如果对URL的GET请求失败。

    返回值:
        None
    """

    # 创建保存目录
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # 发起GET请求并下载文件
    response = requests.get(url)
    response.raise_for_status()  # 检查请求是否成功

    # 保存文件
    with open(save_path, 'wb') as file:
        file.write(response.content)
