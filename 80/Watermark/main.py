#  Created by Simone Margio
#  www.simonemargio.im

# Watermark image

import os
from PIL import Image, ImageFont, ImageDraw

WATERMARK_NAME = "simonemargio.im"

print("Watermark image!\n\n")

try:
    print("Process images...")
    for image_name in os.listdir("in"):
        img = Image.open("in/" + image_name)
        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default()
        draw.text((0, 0), WATERMARK_NAME, (255, 255, 255), font=font)
        img.save("out/Watermark" + image_name)
    print("Done!")
except:
    print(f"Incorrect image!\n({image_name})\nCheck it out.")
    exit(1)
