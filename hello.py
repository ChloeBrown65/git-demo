import sys 

def hello():
	if sys.argv[1] == "Jupiter":
		hellojupiter()
	else:
		helloworld()

def hellojupiter():
	print("hello jupiter")

def helloworld():
	print ("hello world")

if __name__ == '__main__':
	hello()
