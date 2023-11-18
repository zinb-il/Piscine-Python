import sys

if (len(sys.argv) < 2) :
        exit()
try :
    if (len(sys.argv) > 2) :
        print("AssertionError: more than one argument is provided")
    elif (int(sys.argv[1])):
        print("I'm Odd." if int(sys.argv[1]) % 2 else "I'm Even.")
except :
        print("AssertionError: argument is not an integer")
