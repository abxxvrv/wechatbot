import pyautogui
import cv2
import numpy as np
import time
from openai import OpenAI
from cnocr import CnOcr
import pyperclip
client = OpenAI(api_key="输入你的API", base_url="https://api.deepseek.com")

# 定义微信聊天窗口的区域（需要根据实际情况调整）
wechat_chat_region = (834, 809, 882, 304)  # (左, 上, 宽, 高)

# 截图微信聊天窗口
def screenshot_wechat_chat():
    return pyautogui.screenshot(region=wechat_chat_region)

# 比较两张截图的变化
def compare_images(img1, img2):
    # 将截图转换为灰度图
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # 计算两张图片的差异
    diff = cv2.absdiff(gray1, gray2)

    # 阈值处理
    _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    # 计算非零像素点的数量
    non_zero = cv2.countNonZero(thresh)

    return non_zero

# 基于 Deepseek-V3 的回复
def chat(message):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content":
            """
            你要扮演一名INTP和我对话，身份是我的朋友，每次说话的内容不要太长。
            """},
            {"role": "user", "content": message},
        ],
        stream=False
    )

    return response.choices[0].message.content



def detect_new_message():
    last_screenshot = None
    ocr = CnOcr()

    while True:
        # 截图微信聊天窗口
        current_screenshot = np.array(pyautogui.screenshot(region=wechat_chat_region))

        if last_screenshot is not None:
            # 比较当前截图和上一次截图的变化
            diff = compare_images(last_screenshot, current_screenshot)
            if diff > 1000:
                print("检测到新消息！")

                # OCR识别处理
                result = ocr.ocr(current_screenshot)
                text_list = [item['text'] for item in result]
                message = " ".join(text_list).strip()
                print(f"识别内容：{message}")

                # 生成回复并发送
                huifuxinxi = chat(message)
                pyperclip.copy(huifuxinxi)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.press('enter')


                time.sleep(1.5)
                last_screenshot = np.array(pyautogui.screenshot(region=wechat_chat_region))


                continue


        last_screenshot = current_screenshot
        time.sleep(10)


detect_new_message()
