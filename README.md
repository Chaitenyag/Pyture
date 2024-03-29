# Introduction
Pyture is a tool which helps convert images to any format. e.g. from jpg to png etc. Follow the instructions provided in usage to use this tool.

# Inspiration
It is time consuming to access websites which help convert images from one format to another. This is where Pyture steps in. 
Without internet you can now convert your images into any format you like using the command line. 

# Requirements
- Pillow
- argparse
- The above dependencies can be easily installed using the steps mentioned in usage. (They have been provided in setup.sh)

# Usage
- First, you need to open up terminal and clone this repository using the command 'git clone https://github.com/Chaitenyag/Pyture'  
- Then `cd` into the repository and type the command `./setup.sh` (If there is a message about permissions, you would the need to type the command `chmod 777 setup.sh`)

**1) For converting images by changing format:-**
- You can simply type `python3 image_converter.py jpg png -delete yes`
- Hit enter and all jpg will now be converted to png and the jpg's might be deleted depending on the argument yes or no.
- This works for all formats and you can now convert your images into pdf as well.
- NOTE: -delete is optional and is `no` by default.

**2) For resizing images:-**
- You can simply type `python3 image_converter.py flower.jpg 500 500`
- Hit enter and image would be resized.
- This works for all formats.

# Contributions
Chaitenya Gupta
