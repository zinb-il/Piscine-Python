from callLimit import callLimit


@callLimit(3)
def f():
    print("f()")


@callLimit(1)
def g():
    print("g()")


def main():
    try:
        for i in range(3):
            f()
            g()
    except Exception as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()
