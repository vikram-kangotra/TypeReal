#!/bin/env python3

from PIL import Image, ImageDraw, ImageFont
from os.path import isfile
import argparse

parser = argparse.ArgumentParser(description="Text to hand-writing converter")
parser.add_argument('-i', '--ifile', type=str, required=True, help="The input file")
parser.add_argument('-o', '--ofile', type=str, required=True, help="The output file")
parser.add_argument('-f', '--font', type=str, required=False, help="The font file to use")
parser.add_argument('-b', '--background', type=str, required=False, help="The background image file")

args = parser.parse_args()

inputfile = args.ifile
outputfile = args.ofile
fontfile = 'Vikram-Regular.ttf' if args.font is None else args.font
bgImageFile = 'A4sheet.jpg' if args.background is None else args.background

if not isfile(inputfile):
    raise exception("{} coesn't exist".format(inputfile))
if not isfile(fontfile):
    raise Exception("{} doesn't exist".format(fontfile))
if not isfile(bgImageFile):
    raise Exception("{} doesn't exist".format(bgImageFile))

img = Image.open(bgImageFile)
d = ImageDraw.Draw(img)

fontSize = 40
fnt = ImageFont.truetype(fontfile, size = fontSize)

LinesOnPage = int(img.height / fontSize) - 2

with open(inputfile, mode='r') as f:
    text = f.read()
    lines = text.split('\n')
    TotalLines = len(lines)
    imgCount = 0
    out = outputfile.split('.')
    for idx, line in enumerate(lines):
        lineCount = idx % LinesOnPage + 1
        if lineCount == LinesOnPage or idx == TotalLines - 1:
            img.save("{}_{}.{}".format(out[0], imgCount, out[1]))
            img.close()
            img = Image.open(bgImageFile)
            d = ImageDraw.Draw(img)
            imgCount += 1

        d.text((50, 40 + 40*lineCount), line, font = fnt, fill = (0, 0x2b, 0x59))
