from PIL import Image
import os

for f in os.listdir('/Users/Parth/development/github/img-manipulation/img2png'):
    if f.endswith('.jpg'):
        i = Image.open(f)
        fn, fnext = os.path.splitext(f)
        i.save('/Users/Parth/development/github/img-manipulation/img2png/pngs/{}.png'.format(fn))
        print('pngs/{}.png'.format(fn))