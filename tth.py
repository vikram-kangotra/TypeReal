#!/bin/env python3

from PIL import Image, ImageDraw, ImageFont
import argparse

parser = argparse.ArgumentParser(description="Text to Handwriting converter")
parser.add_argument('-i', '--ifile', type=str, required=True, help="The input file")
parser.add_argument('-o', '--ofile', type=str, required=True, help="The output file")

args = parser.parse_args()

inputfile = args.ifile
outputfile = args.ofile

img = Image.open("A4sheet.jpg")
d = ImageDraw.Draw(img)

fontSize = 40
fnt = ImageFont.truetype('Vikram-Regular.ttf', size = fontSize)

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
            img.save(out[0] + str(imgCount) + '.' + out[1])
            img.close()
            img = Image.open("A4sheet.jpg")
            d = ImageDraw.Draw(img)
            #d.rectangle((0, 0, img.width, img.height), fill = (255, 255, 255))
            imgCount += 1

        d.text((50, 40 + 40*lineCount), line, font = fnt, fill = (0, 0x2b, 0x59))
