import os,sys,io
import logging
from PIL import Image, ImageFont, ImageDraw

'''
Takes a single files, list of files or a directory and returns a list of files
'''
def gather_files(images):
    return [images]

def watermark(images, watermark, output_dir, opacity=50):
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

                txt = Image.new('RGBA', im.size, (255,255,255,0))

                draw = ImageDraw.Draw(txt)
                font = ImageFont.truetype('./Open_Sans/OpenSans-Regular.ttf', 72)
                start = (20,20)
                fill = (255,255,255,int(opacity/100 * 255))
                print(watermark["text"])
                draw.text(start, watermark["text"], font=font, fill=fill)
                
                out = Image.alpha_composite(im,txt)
                out.show()
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