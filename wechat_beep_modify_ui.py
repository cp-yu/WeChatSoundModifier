import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinterdnd2 import TkinterDnD, DND_FILES 
from wechat_beep_modify import audio2wav, is_wav, audiopath2wavpath, autosave_wechat_resouce_dll,generate_replace_command,autoget_wechat_path

# 118消息提示音
# 119来电提示音
# 130来电结束提示音

# 路径配置
ffmpeg_path = r'.\ffmpeg.exe'
resource_hacker_path = r'.\ResourceHacker.exe'

is_generate_wav = False


def replace_audio_in_dll(dll_path, new_sound_path, dll_new_path):
    if not is_wav(new_sound_path):
        global is_generate_wav
        is_generate_wav = True
        wav_path = audiopath2wavpath(new_sound_path)
        audio2wav(new_sound_path, wav_path)
    else:
        wav_path = new_sound_path

    replace_command = generate_replace_command(dll_path, wav_path, dll_new_path, selected_sound.get())

    # 调用Resource Hacker命令行
    try:
        subprocess.run(replace_command, shell=True, check=True)
        messagebox.showinfo("Success", "提示音替换成功!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"替换提示音失败: {e}")
    finally:
        if is_generate_wav:
            is_generate_wav = False
            os.remove(wav_path)

def select_file(entry):
    file_path = filedialog.askopenfilename()
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)
        if entry == dll_entry:
            new_dll_entry.delete(0, tk.END)
            new_dll_entry.insert(0, dll_entry.get())

def save_file(entry):
    file_path = filedialog.asksaveasfilename(defaultextension=".dll", filetypes=[("DLL Files", "*.dll")])
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

def on_replace_click():
    dll_path = dll_entry.get()
    new_sound_path = sound_entry.get()
    dll_new_path = new_dll_entry.get()

    if not os.path.exists(dll_path):
        messagebox.showerror("Error", "DLL 文件路径无效")
        return

    if not os.path.exists(new_sound_path):
        messagebox.showerror("Error", "提示音文件路径无效")
        return

    replace_audio_in_dll(dll_path, new_sound_path, dll_new_path)

def drop_file(event, entry):
    # 拖动文件到输入框处理
    file_path = event.data.strip()
    entry.delete(0, tk.END)
    entry.insert(0, file_path)
    if entry == dll_entry:
        new_dll_entry.delete(0, tk.END)
        new_dll_entry.insert(0, dll_entry.get())

if __name__ == "__main__":
    
    # GUI界面
    root = TkinterDnD.Tk()  # 使用TkinterDnD以支持拖拽
    root.title("微信提示音替换工具")

    # DLL文件路径输入
    tk.Label(root, text="DLL 文件路径:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    dll_entry = tk.Entry(root, width=50)
    dll_entry.grid(row=0, column=1, padx=10, pady=5)
    dll_entry.drop_target_register(DND_FILES)
    dll_entry.dnd_bind('<<Drop>>', lambda event: drop_file(event, dll_entry))
    tk.Button(root, text="选择文件", command=lambda: select_file(dll_entry)).grid(row=0, column=2, padx=10, pady=5)

    # 新提示音路径输入
    tk.Label(root, text="新提示音路径:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    sound_entry = tk.Entry(root, width=50)
    sound_entry.grid(row=1, column=1, padx=10, pady=5)
    sound_entry.drop_target_register(DND_FILES)
    sound_entry.dnd_bind('<<Drop>>', lambda event: drop_file(event, sound_entry))
    tk.Button(root, text="选择文件", command=lambda: select_file(sound_entry)).grid(row=1, column=2, padx=10, pady=5)

    # 新DLL保存路径输入
    tk.Label(root, text="保存新的DLL路径:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    new_dll_entry = tk.Entry(root, width=50)
    new_dll_entry.grid(row=2, column=1, padx=10, pady=5)
    tk.Button(root, text="选择保存路径", command=lambda: save_file(new_dll_entry)).grid(row=2, column=2, padx=10, pady=5)

    # 替换按钮
    replace_button = tk.Button(root, text="替换提示音", command=on_replace_click)
    replace_button.grid(row=3, column=1, pady=20)

    # 单选框部分
    tk.Label(root, text="选择提示音类型:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
    selected_sound = tk.StringVar()
    selected_sound.set("消息提示音")

    sound_types = [("消息提示音", "118"), ("来电提示音", "119"), ("通话结束提示音", "130")]

    for i, (sound_label, sound_value) in enumerate(sound_types):
        tk.Radiobutton(root, text=sound_label, variable=selected_sound, value=sound_value).grid(row=4+i, column=1, padx=10, pady=5, sticky="w")
        # 设置默认选择消息提示音
    selected_sound.set("118")


    wechat_dll_path=autoget_wechat_path()
    if wechat_dll_path!="":
        autosave_wechat_resouce_dll(wechat_dll_path)


    # 填充到两个dllentry输入框中
    dll_entry.delete(0, tk.END)
    dll_entry.insert(0, wechat_dll_path)
    new_dll_entry.delete(0, tk.END)
    new_dll_entry.insert(0, wechat_dll_path)


    root.mainloop()

