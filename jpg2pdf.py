import os
from os import listdir
from os.path import isfile, join
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader


path='E:\\temp\\'
# subList = [d for d in os.listdir(path) if os.path.isdir(d)]
subList = [d for d in os.listdir(path)]

for subD in subList:
    pathNew = path + subD + '\\'
    onlyfiles = [f for f in listdir(pathNew) if isfile(join(pathNew, f))]
    pdfName = path + subD + '.pdf'
    c = canvas.Canvas(pdfName)

    for imName in onlyfiles:
        imPath = pathNew + imName
        im = ImageReader(imPath)
        imagesize = im.getSize()
        c.setPageSize(imagesize)
        c.drawImage(imPath,0,0)
        c.showPage()
    c.save()
