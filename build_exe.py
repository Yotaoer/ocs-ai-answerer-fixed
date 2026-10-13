#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OCS AI Answerer - EXE打包脚本
使用PyInstaller将项目打包成独立的exe文件
"""

import os
import sys
import shutil
import subprocess

def check_pyinstaller():
    """检查PyInstaller是否已安装"""
    try:
        import PyInstaller
        print("✅ PyInstaller 已安装")
        return True
    except ImportError:
        print("❌ PyInstaller 未安装")
        print("正在安装 PyInstaller...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
            print("✅ PyInstaller 安装成功")
            return True
        except Exception as e:
            print(f"❌ 安装失败: {e}")
            return False

def create_spec_file():
    """创建PyInstaller配置文件"""
    spec_content = """# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# 需要包含的数据文件
added_files = [
    ('env.template', '.'),
    ('ocs_config.json', '.'),
    ('ocs_answers_viewer.html', '.'),
    ('chart.js.min.js', '.'),
]

a = Analysis(
    ['ocs_ai_answerer_advanced.py'],
    pathex=[],
    binaries=[],
    datas=added_files,
    hiddenimports=[
        'flask',
        'flask_cors',
        'openai',
        'dotenv',
        'httpx',
        'requests',
        'csv',
        'datetime',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='OCS-AI-Answerer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)
"""
    
    with open('OCS-AI-Answerer.spec', 'w', encoding='utf-8') as f:
        f.write(spec_content)
    print("✅ 已创建配置文件: OCS-AI-Answerer.spec")

def build_exe():
    """执行打包"""
    print("\n" + "="*60)
    print("开始打包 OCS AI Answerer...")
    print("="*60 + "\n")
    
    try:
        # 使用spec文件打包
        cmd = [sys.executable, "-m", "PyInstaller", "--clean", "OCS-AI-Answerer.spec"]
        subprocess.check_call(cmd)
        
        print("\n" + "="*60)
        print("✅ 打包成功！")
        print("="*60)
        print("\n📦 可执行文件位置:")
        print("   dist/OCS-AI-Answerer.exe")
        print("\n📝 使用说明:")
        print("   1. 将 dist/OCS-AI-Answerer.exe 复制到任意目录")
        print("   2. 在同目录下创建 .env 文件并配置API密钥")
        print("   3. 双击 OCS-AI-Answerer.exe 运行")
        print("\n⚠️  注意事项:")
        print("   - 首次运行会自动创建 env.template 模板文件")
        print("   - 请根据模板配置 .env 文件")
        print("   - 确保 .env 文件与 exe 在同一目录")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"\n❌ 打包失败: {e}")
        return False
    except Exception as e:
        print(f"\n❌ 发生错误: {e}")
        return False

def main():
    print("="*60)
    print("  OCS AI Answerer - EXE打包工具")
    print("="*60 + "\n")
    
    # 检查并安装PyInstaller
    if not check_pyinstaller():
        print("\n❌ 无法继续，请手动安装 PyInstaller:")
        print("   pip install pyinstaller")
        return
    
    # 创建spec文件
    create_spec_file()
    
    # 执行打包
    if build_exe():
        print("\n🎉 打包完成！")
    else:
        print("\n❌ 打包失败，请检查错误信息")

if __name__ == '__main__':
    main()


