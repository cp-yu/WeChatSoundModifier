@echo off
:: ����Ƿ��Ѿ��ǹ���Ա
net session >nul 2>&1
if %errorLevel% == 0 (
    echo �Ѿ��ǹ���ԱȨ��.
) else (
    echo ���Թ���ԱȨ������...
    pause
    exit
)

:: �Թ���Ա�������Python�ű�
"d:/Document/Code/TEST/WeChatSoundModifier/.conda/python.exe" "d:/Document/Code/TEST/WeChatSoundModifier/wechat_beep_modify_ui.py"
pause
