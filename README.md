# Glory OCR 演示应用

这是一个基于PaddleX的OCR演示应用，用于从图像中提取文本和表格数据。

## 应用功能

- 加载图像并进行OCR识别
- 提取字段（如Recipe和Badge号码）
- 提取表格数据
- 支持图像查看和放大
- 可编辑识别结果
- 导出识别结果为JSON

## 打包为单一可执行文件

### 前提条件

确保您已安装所需的依赖：

```bash
pip install -r requirements.txt
```

### 打包步骤

1. 确保工作目录中包含以下文件：
   - `ocr_extraction_gui.py` - 主程序
   - `OCR.yaml` - OCR配置文件  
   - `models/` - 模型文件夹

2. 运行打包脚本：

```bash
python setup.py
```

3. 打包完成后，可执行文件将位于`dist`目录中。

### 使用打包后的应用

直接双击生成的可执行文件即可启动应用。应用包含所有必要的依赖和模型文件，可以离线运行。 