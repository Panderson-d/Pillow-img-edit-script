import os, sys
from PIL import Image
#  enter directory of image files in save dir output in place of x
savedir = "x"
filedir = os.listdir()

for infile in filedir:
    if os.path.isdir(infile):
        continue
    f, e = os.path.splitext(infile)
    #  converts to .jpg, replace for other files
    outfile = os.path.join(savedir, f + ".jpg")
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                if im.mode != 'RGB':
                    im = im.convert('RGB')
                rgb_im = im.convert('RGB') 
                rot_img = im.transpose(Image.ROTATE_90) 
                #  rotates image 90 degrees,
                resize_img = rot_img.resize((128,128))
                #  resizes images to specified paramets
                resize_img.save(outfile)
        except OSError as e:
            print(f"{e}")