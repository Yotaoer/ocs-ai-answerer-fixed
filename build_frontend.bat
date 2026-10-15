@echo off
chcp 65001 >nul

REM 始终在本脚本所在目录执行，避免从其他工作目录启动时找不到 frontend 目录
cd /d "%~dp0"

echo ===================================
echo    构建 OCS AI Answerer 前端
echo ===================================
echo.

cd frontend

echo [1/3] 检查 Node.js...
where node >nul 2>&1
if errorlevel 1 (
    echo ❌ 未找到 Node.js，请先安装: https://nodejs.org/
    pause
    exit /b 1
)

node -v
REM npm 在 Windows 上是 npm.cmd（批处理），不加 call 会把控制权交出去且不返回，
REM 导致后面的安装与构建全部不执行
call npm -v
echo.

echo [2/3] 安装依赖...
if not exist node_modules (
    call npm install
    if errorlevel 1 (
        echo ❌ 依赖安装失败
        pause
        exit /b 1
    )
) else (
    echo ✅ 依赖已安装，跳过
)
echo.

echo [3/3] 构建生产版本...
call npm run build
if errorlevel 1 (
    echo ❌ 构建失败
    pause
    exit /b 1
)
echo.

cd ..

echo ===================================
echo ✅ 构建成功！
echo.
echo 静态文件已输出到: dist/
echo 现在可以启动服务: start.bat
echo ===================================
pause
