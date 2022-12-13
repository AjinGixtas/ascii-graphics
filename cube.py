import sys
import time
import os
import math
import numpy

'''
Possible options:

1: store a position for every char space in the cube
    - Expensive, need to calculate every pixel

2: Store the positions for the corners only and then do the math to draw the rest inbetween
    - Cheap, only need to calculate 4 pixels then do the if else statements for the rest (memory efficient and time efficient, linear)
    - Need to get the vector between corners and do the fill
    - Does this apply to 3D? Possibly, would have 3D line functions between the points, replace image with front most chars
'''

def main():
    width, height = os.get_terminal_size()
    print(height, width)
    time.sleep(2)

    if (width >= height):
        s = height - 10
    elif (height > width):
        s = width - 10

    center = [width//2, height//2]
    square = [[-s//2, s//2], [s//2, s//2], [-s//2, -s//2], [s//2, -s//2]]

    theta = math.pi/6
    
    out = [[" " for a in range(width)] for b in range(height)]

    j = 0
    while j < 15:

        if (square[1][0] - square[1][0]) == 0:
            p12s
        else:
            p12s = (square[1][1]-square[0][1]) / (square[1][0] - square[1][0])

        for w in range(width):
            for h in range(height):
                if p12s > 0:
                    if w >= square[0][0]:
                        if h >= 12:
                            pass

        for i in range(4):
            print(square[i][1]+center[1], square[i][0]+center[0])
            out[square[i][1]+center[1]][square[i][0]+center[0]] = "#"

        termOut = [("".join(out[i]))+"\n" for i in range(len(out))]
        termOut = "".join(termOut)

        os.system('cls')

        print(termOut)
        time.sleep(0.1)

        os.system('cls')

        for i in range(4):
            out[square[i][1]+center[1]][square[i][0]+center[0]] = " "
            square[i] = [square[i][0]*math.cos(theta) - square[i][1]*math.sin(theta), square[i][0]*math.sin(theta) + square[i][1]*math.cos(theta)]

        j += 1


if __name__ == '__main__':
    main()