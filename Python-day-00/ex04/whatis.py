import sys

try:
    if (len(sys.argv) < 2):
        sys.exit(1)
    assert len(sys.argv) == 2, "more than one argument is provided"
    # assert sys.argv[1].isdigit(), "argument is not an integer"
    print("I'm Odd." if int(sys.argv[1]) % 2 else "I'm Even.")
except AssertionError as msg:
    print(f"AssertionError: {msg}")
except ValueError:
    print("AssertionError: argument is not an integer")
except Exception as err:
    print(f"AssertionError: {err}")
