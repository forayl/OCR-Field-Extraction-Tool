#!/usr/bin/env python
"""
Glory OCR Demo - Build Script for All Platforms
This script generates executables for both Windows and macOS,
regardless of which platform you're currently on.
Requires Docker to be installed.
"""

import os
import sys
import subprocess
import platform
import argparse
from pathlib import Path

def setup_workspace():
    """Create necessary directories"""
    os.makedirs("dist", exist_ok=True)
    os.makedirs("output", exist_ok=True)
    print("Workspace setup complete.")

def build_windows():
    """Build Windows executable using Docker"""
    print("\n=== Building Windows executable ===")
    
    # Windows build using Docker
    docker_cmd = [
        "docker", "run", "--rm",
        "-v", f"{os.path.abspath('.')}:/src",
        "cdrx/pyinstaller-windows",
        "python -m pip install --upgrade pip",
        "&&",
        "pip install -r requirements.txt",
        "&&",
        "pyinstaller --name=Glory_OCR_Demo --windowed --onefile --add-data=output;output ocr_extraction_gui.py"
    ]
    
    try:
        subprocess.run(" ".join(docker_cmd), shell=True, check=True)
        print("Windows build completed successfully!")
        print(f"Executable location: {os.path.abspath('dist/Glory_OCR_Demo.exe')}")
    except subprocess.CalledProcessError:
        print("Error: Windows build failed.")
        print("Make sure Docker is running and you have internet access.")
        return False
    
    return True

def build_macos():
    """Build macOS executable using PyInstaller locally or in Docker"""
    print("\n=== Building macOS executable ===")
    
    if platform.system() == "Darwin":  # If running on macOS
        # Build locally
        try:
            # Ensure requirements are installed
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
            
            # Run PyInstaller
            pyinstaller_cmd = [
                "pyinstaller",
                "--name=Glory_OCR_Demo",
                "--windowed",
                "--onefile",
                "--add-data=output:output",
                "ocr_extraction_gui.py"
            ]
            subprocess.run(pyinstaller_cmd, check=True)
            print("macOS build completed successfully!")
            print(f"Executable location: {os.path.abspath('dist/Glory_OCR_Demo')}")
            return True
        except subprocess.CalledProcessError:
            print("Error: macOS build failed.")
            return False
    else:
        print("Note: Building macOS executable from non-macOS system is not supported.")
        print("To build for macOS, run this script on a macOS system.")
        return False

def main():
    parser = argparse.ArgumentParser(description="Build Glory OCR Demo for multiple platforms")
    parser.add_argument("--windows", action="store_true", help="Build for Windows")
    parser.add_argument("--macos", action="store_true", help="Build for macOS")
    parser.add_argument("--all", action="store_true", help="Build for all supported platforms")
    
    args = parser.parse_args()
    
    # If no arguments provided, build for all platforms
    if not (args.windows or args.macos or args.all):
        args.all = True
    
    print("=" * 60)
    print("Glory OCR Demo - Multi-Platform Build Script")
    print("=" * 60)
    print(f"Current platform: {platform.system()} {platform.release()}")
    print("-" * 60)
    
    setup_workspace()
    
    build_results = {}
    
    if args.windows or args.all:
        build_results["windows"] = build_windows()
    
    if args.macos or args.all:
        build_results["macos"] = build_macos()
    
    print("\n" + "=" * 60)
    print("Build Summary")
    print("-" * 60)
    
    for platform_name, success in build_results.items():
        status = "✅ Success" if success else "❌ Failed"
        print(f"{platform_name.capitalize()}: {status}")
    
    print("\nTo run the build script on a specific platform for native builds:")
    print("- Windows: python build.py")
    print("- macOS: python build.py")
    print("-" * 60)

if __name__ == "__main__":
    main() 