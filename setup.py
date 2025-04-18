import os
import sys
import site
import glob
from PyInstaller.__main__ import run

# 设置应用名称
app_name = "Glory_OCR_Demo"

# 确保当前目录在路径中
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
    os.chdir(application_path)
    sys.path.insert(0, application_path)

# PaddleOCR必需的依赖列表
required_dependencies = [
    'paddle',
    'paddleocr',
    'pyclipper',  # OCR文本框处理
    'shapely',    # 几何形状处理
]

# 打印安装建议
print("如果打包失败，请确保已安装所有必要的依赖:")
print("pip install pyclipper shapely paddleocr")

# 查找Cython包路径
site_packages = site.getsitepackages()
cython_path = None

for path in site_packages:
    potential_cython_path = os.path.join(path, 'Cython')
    if os.path.exists(potential_cython_path):
        cython_path = potential_cython_path
        print(f"找到Cython路径: {potential_cython_path}")
        break

# 配置基本的PyInstaller选项
opts = [
    'ocr_extraction_gui.py',  # 主脚本
    '--name=%s' % app_name,
    '--windowed',             # 无控制台窗口
    '--onedir',               # 目录模式，更稳定
    '--noupx',                # 禁用UPX压缩
    '--debug=all',            # 启用调试
    
    # 添加数据文件
    '--add-data=OCR.yaml:.',  # 添加OCR.yaml配置文件
    '--add-data=models:models',  # 添加models文件夹
    
    # 关键依赖包
    '--collect-all=paddle',
    '--collect-all=paddleocr',
    '--collect-all=pyclipper',
    '--collect-all=shapely',
    '--collect-all=Cython',
    
    # 关键隐式导入
    '--hidden-import=paddle',
    '--hidden-import=paddle.base',
    '--hidden-import=paddle.utils',
    '--hidden-import=paddle.utils.cpp_extension',
    '--hidden-import=paddleocr',
    '--hidden-import=pyclipper',
    '--hidden-import=shapely',
    '--hidden-import=shapely.geometry',
    '--hidden-import=shapely.ops',
]

# 特别处理Cython，确保包含Utility目录及其C文件
if cython_path:
    cython_utility = os.path.join(cython_path, 'Utility')
    if os.path.exists(cython_utility):
        print(f"找到Cython Utility目录: {cython_utility}")
        opts.append(f'--add-data={cython_utility}:Cython/Utility')
        
        # 收集Utility目录下的所有.c文件
        c_files = glob.glob(os.path.join(cython_utility, '*.c'))
        for c_file in c_files:
            if 'StringTools.c' in c_file:
                print(f"找到StringTools.c文件: {c_file}")
            opts.append(f'--add-data={c_file}:Cython/Utility')

print("开始打包应用...")
print(f"使用以下选项: {opts}")

# 清理旧的构建目录，避免符号链接错误
import shutil
for dir_to_remove in ['build', 'dist']:
    if os.path.exists(dir_to_remove):
        print(f"清理目录: {dir_to_remove}")
        shutil.rmtree(dir_to_remove)

# 运行PyInstaller打包
run(opts) 