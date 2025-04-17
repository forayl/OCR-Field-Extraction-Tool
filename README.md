# Glory OCR Demo

一个基于PaddleX的OCR演示应用程序，用于从图像中提取文本和表格数据。

## 功能特点

- 上传并处理图像文件
- 使用OCR技术识别图像中的文本
- 自动提取关键字段（如Recipe和BadgeNo.）
- 自动提取表格数据
- 可视化OCR结果
- 导出提取的数据

## 系统要求

- Windows 10/11 或 macOS 10.15+
- Python 3.7+（开发环境）

## 安装指南

### 方法1：直接运行可执行文件（推荐）

1. 下载最新的发布版本
2. 解压文件
3. 运行可执行文件 (`Glory_OCR_Demo.exe` 或 `Glory_OCR_Demo`)

### 方法2：从源代码运行

1. 克隆或下载本仓库
   ```
   git clone <repository-url>
   ```

2. 安装依赖项
   ```
   pip install -r requirements.txt
   ```

3. 运行应用程序
   ```
   python ocr_extraction_gui.py
   ```

## 构建可执行文件

本项目包含一个构建脚本，可以创建Windows和macOS平台的可执行文件。

1. 安装必要的构建工具
   ```
   pip install -r requirements.txt
   ```

2. 运行构建脚本
   ```
   python build.py
   ```

3. 构建完成后，可执行文件将位于`dist`目录中

### 平台特定说明

#### Windows
- 可执行文件将被创建为`dist/Glory_OCR_Demo.exe`
- 如果需要应用程序图标，请在项目根目录中放置名为`app_icon.ico`的图标文件

#### macOS
- 可执行文件将被创建为`dist/Glory_OCR_Demo`
- 如果需要应用程序图标，请在项目根目录中放置名为`app_icon.icns`的图标文件

## 使用说明

1. 启动应用程序
2. 点击"选择图片"按钮，选择要处理的图像文件
3. 点击"开始识别"按钮，开始OCR处理
4. 处理完成后，可以查看提取的字段和表格数据
5. 可以使用"导出结果"按钮导出JSON格式的数据

## 注意事项

- 首次运行时，应用程序可能需要下载OCR模型，这可能需要一些时间
- 为获得最佳结果，请使用清晰、对比度良好的图像
- 确保系统中有足够的磁盘空间用于存储OCR处理结果

## 故障排除

如果遇到问题：

1. 确保已安装所有必要的依赖项
2. 检查输出目录("./output")是否存在并可写入
3. 确保图像文件格式受支持（PNG、JPG、JPEG、BMP） 