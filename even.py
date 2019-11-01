import subprocess
import sys

def isEven(x):
    while True:
        if x == 0:
            return True
        elif x == 1:
            return False
        print(x)
        x = int(subprocess.check_output(['./square', str(x)]))


if __name__ == '__main__':
    print(isEven(int(sys.argv[1])))
