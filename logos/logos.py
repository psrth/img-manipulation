from PIL import Image, ImageOps
import os

# max size of logo
size_300 = (300, 300)

# max size of final image
new_size = (400, 400)

for f in os.listdir('/Users/Parth/development/github/img-manipulation/logos'):
    # load files that are image types
    if (f.endswith('.jpg') or f.endswith('.png') or f.endswith('.webp') or f.endswith('.JPG') or f.endswith('.PNG') or f.endswith('.WEBP')):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)

        # convert PNGs to JPGs with a white background
        new_image = Image.new("RGBA", i.size, "WHITE") 
        new_image.paste(i, (0, 0), i.convert("RGBA")) 
        i = new_image
        i = i.convert("RGB")
        
        # resize images to max value of 300x300
        i.thumbnail(size_300)
        old_size = i.size

        # apply uniform border on new image
        new_im = Image.new("RGB", new_size, "white")
        new_im.paste(i, ((new_size[0]-old_size[0])//2,
                      (new_size[1]-old_size[1])//2))

        # save image
        new_im.save('/Users/Parth/development/github/img-manipulation/logos/logo/{}.png'.format(fn))
        
        




# i = Image.open(f)
#         fn, fext = os.path.splitext(f)

#         i.thumbnail(size_300)
#         img = ImageOps.expand(i, border=25,fill='white')
#         img.save('/Users/Parth/development/github/img-manipulation/logos/logo/{}.png'.format(fn))