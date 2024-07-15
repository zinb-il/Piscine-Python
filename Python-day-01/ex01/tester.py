from array2D import slice_me


try:
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    # Test1
    print("\033[32m##Test1 \033[0m")
    slice_me([], 1, 1)
    slice_me([[2], 1], 1, 1)
    slice_me([[1], [1, 2]], 1, 1)
    slice_me(family, 'g', 1)
    slice_me(family, 1.2, 1)
    slice_me(family, 1, '1')
    slice_me(family, 1, 1.3)
    print("\033[32m##################################\033[0m")
    # #######################################################
    # Test2
    print("\033[32m##Test2 \033[0m")
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))
    print("\033[32m################################# \033[0m")
    # ########################################################
    # Test3
    print("\033[32m##Test3 \033[0m")
    print(slice_me(family, -100, 2))
    print(slice_me(family, 100, 120))
    print("\033[32m################################# \033[0m")
    # #######################################################
except Exception as err:
    print(f"ExceptionError: {err}")