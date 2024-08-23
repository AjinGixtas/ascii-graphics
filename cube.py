import sys
import time
import os

def main():
    width, height = os.get_terminal_size()
    print(height, width)
    time.sleep(2)
    os.system('cls')

    if (width >= height):
        cubeSize = height - 10
    elif (height > width):
        cubeSize = width - 10

    start_x = (width - cubeSize) // 2
    finish_x = start_x + cubeSize
    start_y = (height - cubeSize//2) // 2
    finish_y = start_y + cubeSize//2

    j = 0
    while j < 15:
        termOut = ""
        for i in range(0, height+1):
            if i < start_y or i > finish_y:
                termOut += width * " " + "\n"
            else:
                termOut += (start_x * " ") + (cubeSize * "#") + ((width-finish_x) * " ") + '\n'
        print(termOut)
        j += 1
        time.sleep(0.25)
        os.system('cls')




if __name__ == '__main__':
    main()