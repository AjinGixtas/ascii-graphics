import os
import math
import time
import shutil

def draw_line(out, x0, y0, x1, y1, char):
    """Bresenham's line algorithm to draw a line on a 2D array."""
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        if 0 <= x0 < len(out[0]) and 0 <= y0 < len(out):
            out[int(y0)][int(x0)] = char
        if x0 == x1 and y0 == y1:
            break
        e2 = err * 2
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    width, height = shutil.get_terminal_size()
    s = min(width, height) - 10
    center = [width // 2, height // 2]
    square = [[-s // 2, s // 2], [s // 2, s // 2], [-s // 2, -s // 2], [s // 2, -s // 2]]

    theta = math.pi / 30  # Rotate 6 degrees per frame
    
    out = [[" " for _ in range(width)] for _ in range(height)]

    for _ in range(100):  # Rotate 100 frames
        for i in range(4):
            next_i = (i + 1) % 4
            x0, y0 = square[i][0] + center[0], square[i][1] + center[1]
            x1, y1 = square[next_i][0] + center[0], square[next_i][1] + center[1]
            draw_line(out, x0, y0, x1, y1, "#")
        
        # Convert 2D array to string for terminal output
        termOut = "\n".join("".join(row) for row in out)
        
        clear_screen()
        print(termOut)
        time.sleep(0.1)
        
        # Clear the current square from the output buffer
        for i in range(4):
            next_i = (i + 1) % 4
            x0, y0 = square[i][0] + center[0], square[i][1] + center[1]
            x1, y1 = square[next_i][0] + center[0], square[next_i][1] + center[1]
            draw_line(out, x0, y0, x1, y1, " ")
        
        # Rotate square
        for i in range(4):
            x, y = square[i]
            square[i] = [x * math.cos(theta) - y * math.sin(theta),
                         x * math.sin(theta) + y * math.cos(theta)]

if __name__ == "__main__":
    main()
