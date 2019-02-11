import os,sys, math
import logging
from PIL import Image, ImageFont, ImageDraw

'''
Takes a single files, list of files or a directory and returns a list of files
'''
def gather_files(images):
    if os.path.isdir(images):
        print("Images is Dir")
    return [images]

def process_images(images, watermark, output_dir, font_size=72, opacity=50):
    #log level debug: 
    # print(images)
    files_to_watermark = gather_files(images)
    #TODO: Parse Directories to List of Files
    #if os.path.isdir(passed_argv[1]):
    #    print('its a path')
    for infile in files_to_watermark:
        try:
            with Image.open(infile).convert('RGBA') as im:
                print(infile, im.format, "%dx%d" % im.size, im.mode)

                #if(im[0] > im[1]):
                txt = Image.new('RGBA', im.size, (255,255,255,0))
                #Constants
                draw = ImageDraw.Draw(txt)
                font = ImageFont.truetype('./Open_Sans/OpenSans-Regular.ttf', font_size)
                fill = (255,255,255,int(opacity/100 * 255))
                textsize = draw.textsize(watermark["text"], font=font)
                start = ( int((im.size[0]-textsize[0])/2), int((im.size[1]-textsize[1])/2))
                draw.text(start, watermark["text"], font=font, fill=fill)
                # Layer Text on Origional Image at <angle>
                rot = txt.rotate(-35)
                out = Image.alpha_composite(im,rot)

                # Save Out Image
                if not os.path.isdir(output_dir):
                    os.mkdir(output_dir)
                file_split = os.path.basename(infile).split('.')
                file_split[-1]='png'
                output_file = output_dir +'/'+'.'.join(file_split)
                out.save(output_file, format="PNG", optimize=True)
                out.thumbnail( ( int(im.size[0]*.2), int(im.size[1]*.2)) )
                file_split = os.path.basename(infile).split('.')
                file_split.append(file_split[-1])
                file_split[-2]='thumbnail'
                file_split[-1]='png'
                output_file = output_dir +'/'+ '.'.join(file_split)
                out.save(output_file, 'PNG', optimize=True)
        except IOError:
            # Log Failed to open infile
            pass    