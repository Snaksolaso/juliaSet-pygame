import pygame
import juliaSet
import colorFuncs
import random
import os
os.system('clear')
print("".center(40,'-'))
print(" Nik's Julia Set Fractal Program ".center(40,'*'))
print("".center(40,'-'))
print()

pygame.font.init()

# Window dimensions
width = 711

height = 400

# complex constant, each different one creates a different fractal
c = complex(-.7269,  0.1889)
#c = complex(-0.12, -0.77)


screen = pygame.display.set_mode((width, height))
myfont = pygame.font.SysFont('Comic Sans MS', int(60* height/800))
myfont2 = pygame.font.SysFont('Comic Sans MS', int(30 * height/800))

running = True
ran = False
fractal = []
dotamount = 0
sharpness = 1

print(
'''
'c' is the constant that is added
to the fractal every iteration.
Each unique value generates a different fractal.
Here are some good c values to test:

1)
Real: -0.0519
Imaginary: 0.688
sharpness: 1

2)
Real: -0.7269
Imaginary: 0.1889
sharpness: 1

3)
Real: -0.12
Imaginary: -0.77

''')
valid = False
while(valid is False):
    real = float(input("Input the real part of c: "))
    imag = float(input("Input the imaginary part of c: "))
    sharpness = float(input("Enter brightness(use 1 unless the fractal is mostly blue): "))
    if(sharpness < 0):
        print("Sharpness must be >0")
    else:
        valid = True





c = complex(real,imag)
zoomcount = 0
set = juliaSet.juliaSet(width, height, -1.955555555, 1.955555555, -1.1, 1.1, c)
while running:
    if ran is False:
        for x in range(0, width):
            #displays the loading bar
            for h in range(height):
                screen.set_at((x + 1,h),(255,0,0))
                screen.set_at((x + 2,h),(255,0,0))
            
            # from here to the 'y' for loop is for displaying the text to the right of the loading bar

            percent = " " + str(int((x/width) * 100)) + "% "
            colorRef = (0,0,0)
            if(x < width - 4):
                colorRef = screen.get_at((x + 3,1))
            fontdisplay1 = myfont.render(percent, False, (255, 0, 0), colorRef)
            screen.blit(fontdisplay1, (x + 7, (height/25)))

            fontdisplay2 = myfont2.render(" " + str(c), False, (255, 0, 0), colorRef)
            screen.blit(fontdisplay2, (x + 7, (height/8)))

            randR = random.random() * 255 + 1
            randG = random.random() * 255 + 1
            randB = random.random() * 255 + 1
            fontdisplay3 = myfont2.render("by Nikolas Heintz, 2019", False, (randR, randG, randB), colorRef)

            screen.blit(fontdisplay3, (x + 7, height - (height/14)))
            pygame.display.flip()

            for y in range(0, height):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                old, iter = set.calcPixel(x, y, 1000)

                # R, G, B each represent their corresponding color value.
                # I made a separate module with functions to apply to iter, giving different color behavior. (I am not using them as of right now)

                R = sharpness * iter
                G = sharpness * iter
                B = sharpness*iter + 100
                if(R > 255):
                    R = 255
                if(G > 255):
                    G = 255
                if(B > 255):
                    B = 255
                color = (R, G, B)
                screen.set_at((x, y), color)
                ran = True
        pygame.image.save(screen, "fractal" + str(zoomcount) + ".png")

        # saves a surface with the fractal for later use
        fractal = screen.copy()

    screen.blit(fractal, (0, 0))
    pygame.event.get()

    # displays a rectangle around the mouse cursor
    mousePos = pygame.mouse.get_pos()
    scaledWidth = width/8
    scaledHeight = height/8
    mouseRect = pygame.Rect(mousePos[0] - scaledWidth/2, mousePos[1] - scaledHeight/2, scaledWidth, scaledHeight)
    pygame.draw.rect(screen, (255, 0, 0), mouseRect, 2)

    pygame.display.flip()

    # mouse input:
    if(pygame.mouse.get_pressed()[0]):
        pygame.image.save(screen, "fractal" + str(zoomcount) + "to" + str(zoomcount + 1) + ".png")
        zoomcount += 1
        set.zoom(mousePos, width, height)
        ran = False

