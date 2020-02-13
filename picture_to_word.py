#!/usr/bin/env python

# -*- coding: utf-8 -*- 

"""
@File: picture_to_word.py

Created on 02 13 18:19 2020

@Authr: zhf12341 from Mr.Zhao

"""

from PIL import Image, ImageDraw, ImageFont
import PySimpleGUI as sg
import os
import time

sg.ChangeLookAndFeel('TealMono')

layout = [
    [sg.Text('欢迎来到情人节必杀器：图片文本转换器，我是zhfbloodz')],
    [sg.Text('选择要转换的图片', size=(15, 1), auto_size_text=False),
     sg.InputText(os.getcwd(), key='PATH'), sg.FolderBrowse()],
    [sg.Text('请输入要图片名+后缀名'), sg.InputText('5.jpg', key='IMG')],
    [sg.Text('选择生成图片文件夹', size=(15, 1), auto_size_text=False),
     sg.InputText(os.getcwd(), key='SAVE_PATH'), sg.FolderBrowse()],
    [sg.Text('请输入要转换的内容'), sg.InputText('我喜欢你', key='TEXT')],
    [sg.Text('请输入字体大小'), sg.InputText('15', key='FONT')],
    [sg.Button('开始转换'), sg.Button('退出')],

]

"""创建GUI窗口"""
window = sg.Window('图片文本转换器', layout=layout)

while True:

    """读取用户输入"""
    event, values = window.read()

    if event in (None,'退出'):
        break

    if event == '开始转换':

        print("=====================================")
        print("开始转换！！！请耐心等待！！！")
        print("=====================================")
        start = time.time()
        text, img_path, font_size, save_path , img_name = values['TEXT'], values['PATH'], int(values['FONT']), values['SAVE_PATH'], values['IMG']
        img_raw = Image.open(os.path.join(img_path,img_name))
        img_array = img_raw.load()

        img_new = Image.new("RGB", img_raw.size, (0, 0, 0))
        draw = ImageDraw.Draw(img_new)
        font = ImageFont.truetype('C:/Windows/fonts/Dengl.ttf', font_size)

        def character_generator(text):
            while True:
                for i in range(len(text)):
                    yield text[i]

        ch_gen = character_generator(text)

        for y in range(0, img_raw.size[1], font_size):
            for x in range(0, img_raw.size[0], font_size):
                draw.text((x, y), next(ch_gen), font=font, fill=img_array[x, y], direction=None)

        img_new.convert('RGB').save(os.path.join(save_path,("new_{}".format(img_name))))
        end = time.time()
        print("=====================================")
        print("转换完成！！！用时 {:.2f} s！！！您可以继续进行转换操作！！！".format(end-start))
        print("=====================================")



window.close()