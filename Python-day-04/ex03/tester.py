from new_student import Student


def main():
    try:
        student = Student(name="Edward", surname="agle")
        print(student)
        print("-----------------------------------")
        student1 = Student(name="Edward", surname="agle", id="toto")
        print(student1)
    except Exception as err:
        print(f"TypeError: {err}")


if __name__ == "__main__":
    main()
