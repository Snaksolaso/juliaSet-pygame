import math

class juliaSet:

    def __init__(self, xwidth, xheight, xrealStart, xrealEnd, xiStart, xiEnd, xc):
        self.width = xwidth
        self.height = xheight
        self.realStart = xrealStart
        self.realEnd = xrealEnd
        self.iStart = xiStart
        self.iEnd = xiEnd
        self.c = xc

    def scaleCoords(self, x, y):
        return(complex(self.realStart + (x / self.width) * (self.realEnd - self.realStart), self.iStart + (y / self.height) * (self.iEnd - self.iStart)))

    def calcPixel(self, x, y, maxiterations):
        z = self.scaleCoords(x, y)
        toAdd = math.exp(-abs(z))
        smoothcolor = toAdd;

        iteration = 0
        while(abs(z) < 30 and iteration < maxiterations):
            z = z**2 + self.c
            smoothcolor += toAdd
            iteration += 1

        return 255 - (iteration/maxiterations)*255,(smoothcolor/maxiterations)*255
    
    def zoom(self, mousePos, width, height):
        comRealWidth = self.realEnd - self.realStart
        comIheight = self.iEnd - self.iStart

        comOldRealCenter = self.realStart + comRealWidth/2 
        comOldICenter = self.iStart + comIheight/2
        comRectRealWidth = comRealWidth/8
        comRectIheight = comIheight/8
        comRealCoord = (comRealWidth * (mousePos[0]/width)) - comRealWidth/2 - comRectRealWidth/2 + comOldRealCenter

        comICoord = (comIheight * (mousePos[1]/height)) - comIheight/2 - comRectIheight/2 + comOldICenter

        self.realStart = comRealCoord
        self.realEnd = comRealCoord + comRectRealWidth
        self.iStart = comICoord
        self.iEnd = comICoord + comRectIheight