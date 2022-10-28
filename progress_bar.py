import time

def main():
    i = 0
    while (i < 11):
        prstring = (i * "-") + ">" + ((10-i) * " ")
        if (i < 10):
            print(f"PROGRESS: [{prstring}] {i*10}%", end="\r")
            time.sleep(0.5)
        else:
            print(f"PROGRESS: [{prstring}] {i*10}%")
        i += 1

if __name__ == "__main__":
    main()