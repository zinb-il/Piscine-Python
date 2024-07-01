from load_image import ft_load


try:
    print(ft_load("landscape.jpg"))
    # print(ft_load("ttlandscape.jpg"))
    # print(ft_load("test.txt"))
    # print(ft_load(1))
    # print(ft_load([1]))
    # print(ft_load(['ff']))
except Exception as err:
    print(f"ExceptionError: {err}")
