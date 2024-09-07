这个软件可以实现微信提示语音的修改。现在支持三种类型的提示音修改：消息、通话、通话关闭。
修改原理：
  微信的资源文件放在WeChatResource.dll文件中，其中118、119、130分别对应消息、通话、通话关闭提示音。

python代码中可以发现使用了ffmpeg、ResourceHacker两个软件。
  其中，ResourceHacker是必须的，用于修改WeChatResource.dll文件。
  ffmpeg仅用于将非wav格式的音频文件修改为wav格式。
