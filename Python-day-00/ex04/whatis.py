import sys

try:
    if (len(sys.argv) < 2):
        sys.exit(1)
    assert len(sys.argv) == 2, "more than one argument is provided"
    print("I'm Odd." if int(sys.argv[1]) % 2 else "I'm Even.")
except AssertionError as msg:
    print(f"AssertionError: {msg}")
except Exception:
    print("AssertionError: argument is not an integer")
