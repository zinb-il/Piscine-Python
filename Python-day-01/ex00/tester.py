from give_bmi import give_bmi, apply_limit


def main():
    try:
        # Test1
        print("\033[32m #Test1 \033[0m")
        lst = [22.507863455018317, 29.0359168241966]
        height = [2.71, 1.15]
        weight = [165.3, 38.4]
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
        print([lst[i] - bmi[i] for i in range(len(lst))])
        print("\033[32m##############################################\033[0m")
        # Test2
        print("\033[32m #Test2 \033[0m")
        print("\033[32m test with dic and tuple \033[0m")
        give_bmi((4), (5))
        give_bmi([], [])
        give_bmi({'h':5}, {'h':5})
        give_bmi([1], [[1]])
        give_bmi([1, 4], ['l', 4])
        give_bmi([-9], [0])
        give_bmi([9], [-8])
        give_bmi(None, None)
        print("\033[32m##############################################\033[0m")
        # Test3
        print("\033[32m #Test3 \033[0m")
        apply_limit([], 26)
        apply_limit({'v': 4}, 26)
        apply_limit(['bmi'], 26)
        apply_limit(False, 26)
        apply_limit(bmi, 'p')
        apply_limit(bmi, 2.3)
    except Exception as err:
        print(f"ExceptionError: {err}")


if __name__ == "__main__":
    main()
