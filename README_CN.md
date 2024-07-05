# Bing 图像下载爬虫

本项目使用 `bing_image_downloader` 库从 Bing 下载指定搜索词的图像。目标是下载大量与给定关键字相关的图像。

## 要求

- Python 3.x
- bing_image_downloader

## 安装

1. 使用 pip 安装所需的库：

   ```bash
   pip install bing_image_downloader
   ```

## 使用方法

脚本根据指定的搜索词下载图像，并将其保存到指定的目录。

```python
from bing_image_downloader import downloader

# 定义搜索词和下载图像的数量
search_term = "铭牌"
num_images = 5000
output_directory = 'bing_images_test'

# 下载图像并保存到指定目录
downloader.download(search_term, limit=num_images, output_dir=output_directory, adult_filter_off=True, force_replace=False, timeout=60)

print(f"下载 {search_term} 的 {num_images} 张图片到 {output_directory} 目录完成。")
```

## 参数说明

- `search_term`：在 Bing 上搜索图像的关键字。
- `num_images`：要下载的图像数量。
- `output_directory`：保存下载图像的目录。
- `adult_filter_off`：布尔值，是否关闭成人内容过滤。
- `force_replace`：布尔值，是否强制替换现有文件。
- `timeout`：每次下载请求的超时时间（秒）。

## 注意事项

确保在下载图像时有稳定的网络连接，因为下载大量图像可能需要一些时间。

## 许可证

本项目采用 MIT 许可证。
