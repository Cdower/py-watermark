import os,sys
from PIL import Image

'''
Takes a single files, list of files or a directory and returns a list of files
'''
def gather_files(passed_argv):
    return []

def watermark(passed_argv):
    #passed_argv[1:]
    files_to_watermark = gather_files(passed_argv[1:])
    #TODO: Parse Directories to List of Files
    #if os.path.isdir(passed_argv[1]):
    #    print('its a path')
    for infile in files_to_watermark:
        try:
            with Image.open(infile) as im:
                print(infile, im.format, "%dx%d" % im.size, im.mode)
        except IOError:
            pass