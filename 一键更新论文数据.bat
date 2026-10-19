@echo off
chcp 65001 >nul
cd /d "%~dp0"
title 许晖课题组 ORCID 论文全自动同步系统
echo =======================================================
echo        许晖课题组 学术成果全自动同步更新工具
echo =======================================================
echo.
echo 正在连接 ORCID 官方 API 检查并同步最新论文...
echo.

python "%~dp0sync_orcid.py"

echo.
echo =======================================================
echo [同步完成] 
echo 1. 本地预览：即将为您自动打开 preview_publications.html
echo 2. 凡科更新：若已配置 GitHub 联动，推送后网站自动生效
echo =======================================================
echo.

start "" "%~dp0preview_publications.html"

pause
