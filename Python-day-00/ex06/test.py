from ft_filter import ft_filter

# Test1
# def check(letter) :
#   list_of_vowels = ['a', 'e', 'i', 'o', 'u']
#   if letter in list_of_vowels:
#       return True
#   else:
#       return False
# letters = ['u', 'a', 'q', 'c', 'i', 'd', 'z', 'p', 'e']
# f1 = filter(check, letters)
# f2 = ft_filter(check, letters)


# Test 2
# nums = [5, 10, 23, 64, 42, 53, 93, 2, 0, -14, 6, -22, -13]
# f1 = filter(lambda p : p%2 != 0, nums)
# f2 = ft_filter(lambda p : p%2 != 0, nums)

# Test 3
# nums = [5, -23, "", True, False, 0, 0.0, {}, []]
# f1 = filter(None, nums)
# f2 = ft_filter(None, nums)

# Test 4
# books = [{"Title":"Angels and Demons", "Author":"Dan Brown", "Price":500},
#    {"Title":"Gone Girl", "Author":"Gillian Flynn", "Price":730},
#    {"Title":"The Silent Patient", "Author":"Alex Michaelidis", "Price":945},
#    {"Title":"Before I Go To Sleep", "Author":"S.J Watson", "Price":400}]

# def func(book):
#    if book["Price"] > 500:
#        return True
#    else:
#        return False

# f1 = filter(func, books)
# f2 = ft_filter(func, books)


# print(filter.__doc__)
# print(ft_filter.__doc__)

# print(type(f1))
# print(type(f2))

# print(f1)
# print(f2)

# print(list(f1))
# print(list(f2))


# Online Test

# def is_even(num):
#     return num % 2 == 0


# def test_filter():
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     strings = ["apple", "banana", "cherry", "date", "elderberry"]
#     mixed_types = [1, "apple", 2.5, "banana", 3, "cherry", 4.7]

#     even_numbers = ft_filter(is_even, numbers)
#     assert list(even_numbers) == [2, 4, 6, 8, 10], \
#         "\033[31mTest 1 failed\033[0m"
#     print("\033[32m       ok\033[0m")

#     odd_numbers = ft_filter(lambda x: x % 2 != 0, numbers)
#     assert list(odd_numbers) == [1, 3, 5, 7, 9], "\033[31mTest 2 \
#     failed\033[0m"
#     print("\033[32m       ok\033[0m")

#     greater_than_5 = ft_filter(lambda x: x > 5, numbers)
#     assert list(greater_than_5) == [6, 7, 8, 9, 10], \
#         "\033[31mTest 3 failed\033[0m"
#     print("\033[32m       ok\033[0m")

#     long_strings = ft_filter(lambda s: len(s) > 5, strings)
#     assert list(long_strings) == ["banana", "cherry", "elderberry"], \
#         "\033[31mTest 4 failed\033[0m"
#     print("\033[32m       ok\033[0m")

#     integers = ft_filter(lambda x: isinstance(x, int), mixed_types)
#     assert list(integers) == [1, 3], "\033[31mTest 5 failed\033[0m"
#     print("\033[32m       ok\033[0m")

#     floats = ft_filter(lambda x: isinstance(x, float), mixed_types)
#     assert list(floats) == [2.5, 4.7], "\033[31mTest 6 failed\033[0m"
#     print("\033[32m       ok\033[0m")

#     print("\033[32mAll tests passed\033[0m")


# test_filterstring()

def test_filterstring():
    test_cases = [
        ("Hello World", 4, ["Hello", "World"]),
        ("Python is fun", 2, ["Python", "fun"]),
        ("", 0, []),
        ("abc def ghi", 1, ["abc", "def", "ghi"]),
        ("One Two Three", 4, ["Three"]),
        ("Zero Nani Three", 5, []),
    ]
    passed_tests = 0
    for text, n, expected_result in test_cases:
        filtered_words = \
            list(ft_filter(lambda word: len(word) > n, text.split()))
        if filtered_words == expected_result:
            passed_tests += 1
            print("\033[32m       ok\033[0m")
        else:
            print("\033[31mTest failed for input '{}', {}: Expected {}, \
            got {}\033[0m".format(text, n, expected_result, filtered_words))
    print("\033[32m{} out of {} \
    tests passed\033[0m".format(passed_tests, len(test_cases)))


test_filterstring()
