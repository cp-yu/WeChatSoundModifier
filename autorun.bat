@echo off
:: 检查是否已经是管理员
net session >nul 2>&1
if %errorLevel% == 0 (
    echo 已经是管理员权限.
) else (
    echo 请以管理员权限运行...
    pause
    exit
)

:: 以管理员身份运行Python脚本
"d:/Document/Code/TEST/WeChatSoundModifier/.conda/python.exe" "d:/Document/Code/TEST/WeChatSoundModifier/wechat_beep_modify_ui.py"
pause
