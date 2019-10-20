import subprocess
import sys

def isEven(x):
	while True:
		if x == '0':
			return True
		elif x == '1':
			return False
		print(x)
                try:
		    x = subprocess.check_output(['java', 'SquareInt', x])
                except:
                    return "u dont have java"

if __name__ == '__main__':
	print(isEven(sys.argv[1]))
