import os
import subprocess
import shutil
import psutil


ffmpeg_path = r'D:\Download\resource_hacker\ffmpeg.exe'
# Resource Hacker的路径
resource_hacker_path = r'D:\Download\resource_hacker\ResourceHacker.exe'

# WeChatResource.dll的路径
dll_path = r'D:\Download\resource_hacker\WeChat.dll'    
dll_new_path = r'D:\Download\resource_hacker\temp.dll'    



def audio2wav(audio_path, wav_path):
    # 音频转wav
    command = f'{ffmpeg_path} -i "{audio_path}" -acodec pcm_s16le -ar 44100 -ac 2 "{wav_path}"'
    try:
        subprocess.run(command, shell=True, check=True)
        print("音频转wav成功!")
    except subprocess.CalledProcessError as e:
        print("Error ", f"音频转wav失败: {e}")

def is_wav(file_path):
    return file_path.endswith('.wav')

def audiopath2wavpath(audio_path):
    audio_name = os.path.basename(audio_path)
    wav_name = os.path.splitext(audio_name)[0] + '.wav'
    wav_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), wav_name)
    return wav_path


def get_wechat_running_path():
    # 遍历所有正在运行的进程
    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        try:
            # 检查进程名称是否包含 WeChat 或 WeChat.exe
            if proc.info['name'].lower() == 'wechat.exe':
                return os.path.dirname(proc.info['exe'])  
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    raise Exception("WeChat is not running or could not be found.")

def find_wechat_resource_dll(directory,file_name):
    for root, dirs, files in os.walk(directory):
        if 'WeChatResource.dll' in files:
            return os.path.join(root, file_name)
    return "NotFound"

def autoget_wechat_path():
    try:
        wechat_path = get_wechat_running_path()
        wechat_dll_path = find_wechat_resource_dll(wechat_path,'WeChatResource.dll')
        # wechat_dll_backup_path = find_wechat_resource_dll(wechat_path,'WeChatResource_backup.dll')
    except Exception as e:
        wechat_dll_path = ""
    return wechat_dll_path

def autosave_wechat_resouce_dll(wechat_dll_path):
    backup_dll_path = wechat_dll_path.replace('WeChatResource.dll','WeChatResource_backup.dll')
    if os.path.exists(backup_dll_path):
        return
    try:
        shutil.copy(wechat_dll_path, backup_dll_path)
    except Exception as e:
        print("Error ", f"备份WeChatResource.dll失败: {e}\n请手动备份")


def generate_replace_command(dll_path, new_sound_path, dll_new_path, sound_type):
    return f'"{resource_hacker_path}" -open "{dll_path}" -save "{dll_new_path}" -action addoverwrite -res "{new_sound_path}" -mask WAVE,{sound_type}'


def main():
    # 新的提示音路径
    new_sound_path = r'D:\Download\resource_hacker\attack_button_click.mp3'

    if(not is_wav(new_sound_path)):
        wav_path = audiopath2wavpath(new_sound_path)
        audio2wav(new_sound_path, wav_path)
    else:
        wav_path = new_sound_path


    replace_command = f'"{resource_hacker_path}" -open "{dll_path}" -save "{dll_new_path}" -action addoverwrite -res "{wav_path}" -mask WAVE,118'

    # 调用Resource Hacker命令行
    try:
        subprocess.run(replace_command, shell=True, check=True)
        print("提示音替换成功!")
    except subprocess.CalledProcessError as e:
        print(f"替换提示音失败: {e}")

if __name__ == "__main__":
    main()