from autoDownloadSourceJsonFile import download_metadata
from autoDataClearLoadMetaData import make_lite_emoji_json
from manualGetSvgEmoji import scan_svg_raw
from custom_tools import config_dict,say_somethings

USER_CONFIG = config_dict()
# metaData下载地址
metadata_url = USER_CONFIG['metadata_json']['download_url']
metadata_save = USER_CONFIG['metadata_json']['save_path']
# 解析为Lite版本EmojiMetaJson和KeywordsJson
lite_emoji_save = USER_CONFIG['emoji_lite']['save_path']

if __name__ == '__main__':
    say_somethings("下载元数据中……")
    download_metadata(metadata_url, metadata_save)
    say_somethings("解析为Lite版本EmojiMetaJson和KeywordsJson")
    make_lite_emoji_json(metadata_save, lite_emoji_save)
    say_somethings("解析SVG文件字典")
    scan_svg_raw()