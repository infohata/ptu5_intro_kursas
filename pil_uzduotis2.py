from PIL import Image, ImageEnhance
import os

def enhance_image(pic, contrast, color, sharpness, brightness, save=False):
    im = Image.open(pic)
    enh = ImageEnhance.Contrast(im)
    im = enh.enhance(contrast)
    enh = ImageEnhance.Color(im)
    im = enh.enhance(color)
    enh = ImageEnhance.Brightness(im)
    im = enh.enhance(brightness)
    enh = ImageEnhance.Sharpness(im)
    im = enh.enhance(sharpness)
    if save:
        loc = os.path.splitext(pic)[0]
        ext = os.path.splitext(pic)[1]
        im.save(f'{loc}_modified{ext}')
    im.show()

enhance_image('img/nenormaliai.jpg', 1.5, 0.25, 2, 1.5, True)

import os, psutil
process = psutil.Process(os.getpid())
print(process.memory_info().rss)
