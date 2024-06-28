from give_bmi import give_bmi, apply_limit


def main():
    try:
        lst = [22.507863455018317, 29.0359168241966]
        height = [2.71, 1.15]
        weight = [165.3, 38.4]
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        # print([lst[i] - bmi[i] for i in range(len(lst))])
        print(apply_limit(bmi, 26))
    except Exception as err:
        print(f"ExceptionError: {err}")


if __name__ == "__main__":
    main()
