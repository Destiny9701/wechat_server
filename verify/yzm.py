# __author:"Destiny"
# date: 2018/1/13

import os
import random
from functools import reduce

import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
import PIL.ImageFilter as ImageFilter
import PIL.ImageFont as ImageFont

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
TTF_PATH = os.path.join(CURRENT_PATH, "LiberationSerif-Bold.ttf")
IMG_PATH = os.path.join(CURRENT_PATH, "verify_img")

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))


# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

def list_to_str(i,j):
    return "%s%s" % (i,j)

def generate_verification_code(uuid):
    # 240 x 60:
    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建Font对象:
    font = ImageFont.truetype(TTF_PATH, 36)
    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())
    # 输出文字:
    char_list = [rndChar() for i in range(4)]
    print()
    for t in range(4):
        draw.text((60 * t + 10, 10), char_list[t], font=font, fill=rndColor2())
    # 模糊:
    image = image.filter(ImageFilter.BLUR)
    with open(os.path.join(IMG_PATH, "%s.jpg" % uuid), "w") as f:
        pass

    image.save(os.path.join(IMG_PATH, "%s.jpg" % uuid), 'jpeg')
    return reduce(list_to_str, char_list)
    pass


if __name__ == "__main__":
    #generate_verification_code("156154")
    print(CURRENT_PATH)
    pass