from bing_image_downloader import downloader

# 下载关键词为 "" 的图片，限制为  张
search_term = ("铭牌")
num_images = 5000
output_directory = 'bing_images_test'

# 调用下载器，下载图片并保存到指定目录
downloader.download(search_term, limit=num_images, output_dir=output_directory, adult_filter_off=True, force_replace=False, timeout=60)

print(f"下载 {search_term} 的 {num_images} 张图片到 {output_directory} 目录完成。")
