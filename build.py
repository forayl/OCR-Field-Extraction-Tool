#!/usr/bin/env python
import os
import sys
import subprocess
import platform
import shutil
from pathlib import Path

def check_requirements():
    """Check if required packages are installed, and install them if not"""
    required_packages = ["pyinstaller", "pillow", "paddlex"]
    
    print("Checking and installing required packages...")
    for package in required_packages:
        try:
            __import__(package)
            print(f"✓ {package} is already installed")
        except ImportError:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def build_for_windows():
    """Build the application for Windows"""
    print("\nBuilding executable for Windows...")
    
    # Create spec for Windows
    icon_path = "app_icon.ico" if os.path.exists("app_icon.ico") else None
    icon_param = f"--icon={icon_path}" if icon_path else ""
    
    # Build command
    build_cmd = [
        "pyinstaller",
        "--name=Glory_OCR_Demo",
        "--windowed",
        "--onefile",
        icon_param,
        "--clean",
        "--add-data=output;output",
        "ocr_extraction_gui.py"
    ]
    
    # Remove empty parameters
    build_cmd = [cmd for cmd in build_cmd if cmd]
    subprocess.check_call(build_cmd)
    
    print("Windows build completed!")
    print(f"Executable location: {os.path.abspath('dist/Glory_OCR_Demo.exe')}")

def build_for_macos():
    """Build the application for macOS"""
    print("\nBuilding executable for macOS...")
    
    # Create spec for macOS
    icon_path = "app_icon.icns" if os.path.exists("app_icon.icns") else None
    icon_param = f"--icon={icon_path}" if icon_path else ""
    
    # Build command
    build_cmd = [
        "pyinstaller",
        "--name=Glory_OCR_Demo",
        "--windowed",
        "--onefile",
        icon_param,
        "--clean",
        "--add-data=output:output",
        "ocr_extraction_gui.py"
    ]
    
    # Remove empty parameters
    build_cmd = [cmd for cmd in build_cmd if cmd]
    subprocess.check_call(build_cmd)
    
    print("macOS build completed!")
    print(f"Executable location: {os.path.abspath('dist/Glory_OCR_Demo')}")

def create_output_dir():
    """Create output directory if it doesn't exist"""
    output_dir = Path("output")
    if not output_dir.exists():
        output_dir.mkdir()
        print("Created output directory")

def main():
    """Main build function"""
    print("=" * 60)
    print(f"Glory OCR Demo - Build Script")
    print("=" * 60)
    print(f"Operating System: {platform.system()} {platform.release()}")
    print("-" * 60)
    
    # Check and install requirements
    check_requirements()
    
    # Create output directory
    create_output_dir()
    
    # Build for the current platform
    current_platform = platform.system().lower()
    
    if current_platform == "windows":
        build_for_windows()
    elif current_platform == "darwin":  # macOS
        build_for_macos()
    else:
        print(f"Unsupported platform: {current_platform}")
        print("This build script supports Windows and macOS only.")
        return
    
    print("\nBuild completed successfully!")
    print("-" * 60)
    print("Usage instructions:")
    print("1. Locate the executable in the 'dist' folder")
    print("2. Copy the executable to your desired location")
    print("3. Run the executable")
    print("-" * 60)

if __name__ == "__main__":
    main() 