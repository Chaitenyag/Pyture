from PIL import Image
import argparse
import glob
import os

# The following function converts all file in original format
# into new format.
def fileConverter(originalFormat, newFormat):
    for file in glob.glob("*." + str(originalFormat)):
        image = Image.open(file)
        rgbImage = image.convert('RGB')
        rgbImage.save(file.replace(str(originalFormat), str(newFormat)), quality=100)

# The following function calls fileConverter and also deletes the original
# file if needed
def start(originalFormat, newFormat, ans = 'no'):
    print('Welcome to Pyture - Python-Image-Converter!')
    fileConverter(originalFormat, newFormat)
    print('Your file is converted from ' + originalFormat + ' to ' + newFormat)
    
    if ans in ['Yes', 'yes', '  Y', 'y']:
        fileDeletion(originalFormat)
        print('Deleted!')
        print('Thank you for using Pyture')

# Function called if original file needs to be deleted
def fileDeletion(originalFormat):
    for file in glob.glob("*." + originalFormat):
        os.remove(file)

# Function which acts as a CLI for this tool
def main():
    parser = argparse.ArgumentParser(prog='Pyture',
                                     usage='''
                                         Usage:
                                         Enter the command in ther following format:
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
        
                                     parser.add_argument("original", type=str, help="Enter original extension. (e.g. png)", metavar="Original Extension")
                                     parser.add_argument("new", type=str, help="Enter new extension. (e.g. jpg)", metavar="New Extension")
                                     parser.add_argument("-delete", "-d", type=str,
                                                         help="Optional: Enter yes to delete original file OR no to keep original file", default='no',
                                                         required=False)
                                     
                                     arg = parser.parse_args()
                                     start(arg.original, arg.new, arg.delete)

if __name__ == '__main__':
    main()
