import os, sys
from PIL import Image
#  Replace x in save dir with directory where you want new files to be saved
savedir = "x"
# Replace y with directory of files
os.chdir('y')
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