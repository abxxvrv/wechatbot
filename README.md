# wechatbot

## 项目介绍
这是一个基于 Python 实现的微信聊天自动回复工具。它通过截取微信聊天窗口的屏幕区域，利用 OCR 技术识别新的聊天消息，并根据识别到的消息内容，结合 Deepseek 的语言模型生成回复内容，然后模拟按键操作将回复发送到微信聊天窗口中。该工具可以帮助用户更便捷地自动处理一些重复性或简单的微信聊天消息。

## 使用方法
### 环境依赖
- Python 3.x
- 安装以下 Python 库：
    - `pyautogui`
    - `opencv-python`
    - `numpy`
    - `openai`（用于与 Deepseek API 交互）
    - `cnocr`

可以通过以下命令安装这些库（根据实际情况选择合适的命令）：
```bash
pip install pyautogui opencv-python numpy openai cnocr
```

### 配置
1. **Deepseek API 配置**：将代码中的 `api_key` 替换为你的 Deepseek API 密钥。
2. **微信聊天窗口区域配置**：根据你实际电脑屏幕上微信聊天窗口的位置和大小，调整 `wechat_chat_region` 的值（格式为 `(左, 上, 宽, 高)`）。可以使用截图工具，如QQ，鼠标在的位置会显示坐标。

### 运行
运行该 Python 脚本即可开始自动检测微信聊天窗口中的新消息并进行回复。你可以通过在终端中切换到项目目录并运行以下命令来启动脚本：
```bash
python wechatbot.py
```
脚本会持续运行并监控微信聊天窗口的变化，当检测到新消息时会执行 OCR 识别、内容回复等操作。

### 注意事项
- 请确保在运行脚本时，微信客户端已经开启且聊天窗口处于你设置的监控区域内。
- 该工具可能无法完美识别和处理所有类型的聊天内容（如复杂的表情符号、图片信息等），且自动回复的内容质量可能受限于 Deepseek 模型的表现以及 OCR 识别的准确性。
- 使用该工具时，请遵守相关法律法规以及微信使用规范，避免滥用导致违反规定或对他人造成困扰。
