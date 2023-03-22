import os
import random
from PIL import Image
from flask import Flask, render_template, request

app = Flask(__name__)

messages = []
counter = 1
img_folder = 'E:\\桌面\\图片'

@app.route('/')
def index():
    # 获取图片文件夹中的所有图片
    img_files = os.listdir(img_folder)
    # 随机选择一张图片并降低分辨率以减小文件大小
    random_img_path = os.path.join(img_folder, random.choice(img_files))
    random_img = Image.open(random_img_path)
    random_img.thumbnail((1, 1))
    # 渲染模板并将随机选择的图片和留言信息传递给模板
    return render_template('index.html.jinja2', messages=messages, random_img_path=random_img_path)

@app.route('/submit', methods=['POST'])
def submit_message():
    global counter
    message = request.form['message']
    messages.append({'太对啦！': f'第{counter}位uu', '发送了': message})
    counter += 1
    # 获取图片文件夹中的所有图片
    img_files = os.listdir(img_folder)
    # 随机选择一张图片并降低分辨率以减小文件大小
    random_img_path = os.path.join(img_folder, random.choice(img_files))
    random_img = Image.open(random_img_path)
    random_img.thumbnail((1, 1))
    # 渲染模板并将随机选择的图片和留言信息传递给模板
    return render_template('index.html.jinja2', messages=messages, random_img_path=random_img_path)

if __name__ == '__main__':
    app.run()
