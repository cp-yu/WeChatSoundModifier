这个软件可以实现微信提示语音的修改。现在支持三种类型的提示音修改：消息、通话、通话关闭。
修改原理：
  微信的资源文件放在WeChatResource.dll文件中，其中118、119、130分别对应消息、通话、通话关闭提示音。

python代码中可以发现使用了ffmpeg、ResourceHacker两个软件。
  其中，ResourceHacker是必须的，用于修改WeChatResource.dll文件。
  ffmpeg仅用于将非wav格式的音频文件修改为wav格式。

bat文件：方便以管理员身份运行。因为微信安装文件夹有权限保护，使用管理员身份更方便。bat里面的路径按需更改。

## Third-Party Software

This software utilizes the following third-party tools:

### FFmpeg

This software uses FFmpeg for audio processing.

FFmpeg is a free software project that produces libraries and programs for handling multimedia data. FFmpeg is licensed under the GNU Lesser General Public License (LGPL) or the GNU General Public License (GPL) depending on your build configuration. 

For more information about FFmpeg, please visit [https://ffmpeg.org/](https://ffmpeg.org/).

#### Copyright Notice for FFmpeg:

```
FFmpeg is licensed under LGPLv2.1 or later. The license can be found in the FFmpeg source code repository or at https://ffmpeg.org/legal.html.

```
Disclaimer: This project uses FFmpeg as an external tool, and it is not bundled with the software. Users must download and install FFmpeg separately according to the terms of the LGPL or GPL license. The authors of this software are not affiliated with the FFmpeg project, and any issues related to FFmpeg should be directed to its respective maintainers.

### ResourceHacker

This software makes use of ResourceHacker to modify DLL files for replacing notification sounds.

ResourceHacker is a free program designed to allow users to view, modify, rename, add, delete and extract resources in 32-bit and 64-bit Windows executables. ResourceHacker is a proprietary tool developed by Angus Johnson.

For more information about ResourceHacker, please visit [http://www.angusj.com/resourcehacker/](http://www.angusj.com/resourcehacker/).

#### Copyright Notice for ResourceHacker:

```
ResourceHacker is a proprietary software tool developed and maintained by Angus Johnson. Please refer to the ResourceHacker website for licensing details.
```
Disclaimer: This project uses ResourceHacker as an external tool, and it is not bundled with the software. Users must download and install ResourceHacker separately according to its respective terms and conditions. The authors of this software are not affiliated with ResourceHacker or Angus Johnson. Any issues related to ResourceHacker should be directed to its original developer.
```

### 4. **MIT License Reminder**



