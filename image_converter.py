from PIL import Image
import argparse
import glob
import os
import sys
from PIL import Image

# The following function converts all file in original format
# into new format.
def file_converter(original_format, new_format):
    for file in glob.glob("*." + str(original_format)):
        image = Image.open(file)
        rgbImage = image.convert('RGB')
        rgbImage.save(file.replace(str(original_format), str(new_format)), quality=100)

# The following function calls file_converter and also deletes the original
# file if needed
def start(original_format, new_format, ans='no'):
    print('Welcome to Pyture - Python-Image-Converter!')
    file_converter(original_format, new_format)
    print('Your file is converted from ' + original_format + ' to ' + new_format)

    if ans in ['Yes', 'yes', '  Y', 'y']:
        file_deletion(original_format)
        print('Deleted!')
        print('Thank you for using Pyture')

# Function called if original file needs to be deleted
def file_deletion(original_format):
    for file in glob.glob("*." + original_format):
        os.remove(file)

# The following function resizes an image.
def file_resize(file_name, width, height):
    img_org = Image.open(file_name)
    img_new = img_org.resize((int(width), int(height)), Image.NEAREST)
    name, ext = os.path.splitext(file_name)
    img_new.save(name + ext)

# Function which acts as a CLI for this tool
def convert_main():
    parser = argparse.ArgumentParser(prog='Pyture',
                                     usage='''
                                    Usage:
                                    Enter the command in the following format:
                                    python3 image_converter.py [Original extension. (e.g. png)] [New extension. (e.g. jpg)] [Yes/No]

                                    e.g. python3 image_converter.py png jpg --del yes
                                    ''',
                                     description='''
                                    -----------------------------------------------
                                    Description:
                                    This tool will convert your image files
                                    -----------------------------------------------
                                    ''',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     add_help=True
                                     )

    parser.add_argument("original", type=str, help="Enter original extension. (e.g. png)"
                        , metavar="Original Extension")
    parser.add_argument("new", type=str, help="Enter new extension. (e.g. jpg)",
                        metavar="New Extension")
    parser.add_argument("-delete", "-d", type=str,
                        help="Optional: Enter yes to delete original" + "file OR no to keep original file",
                        default='no',
                        required=False)

    arg = parser.parse_args()
    start(arg.original, arg.new, arg.delete)

# Function which acts as a CLI for this tool
def resize_main():
    parser = argparse.ArgumentParser(prog='Pyture',
                                     usage='''
                                         Usage:
                                         Enter the command in the following format:
                                         python3 image_converter.py [File Name (e.g. Flower.jpg)] [Width (e.g. 500)] [Height (e.g. 500)]

                                         e.g. python3 image_converter.py Flower.jpg 500 500
                                         ''',
                                     description='''
                                         -----------------------------------------------
                                         Description:
                                         This tool will resize your image file
                                         -----------------------------------------------
                                         ''',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     add_help=True
                                     )
    parser.add_argument("file_name", type=str,
                        help="Enter the file name (e.g. Flower.jpg)"
                        , metavar="File Name")

    parser.add_argument("width", type=str, help="Enter the width. (e.g. 500)"
                        , metavar="Width")
    parser.add_argument("height", type=str, help="Enter the height. (e.g. 500)",
                        metavar="Height")


    arg = parser.parse_args()
    file_resize(arg.file_name, arg.width, arg.height)

if __name__ == '__main__':
    print(len(sys.argv))
    if len(sys.argv) == 4:
        resize_main()
