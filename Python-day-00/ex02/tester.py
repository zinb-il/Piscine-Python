from find_ft_type import all_thing_is_obj
import math


ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj(10)
all_thing_is_obj(0.2)
all_thing_is_obj(True)
all_thing_is_obj(math.nan)
print(all_thing_is_obj(10))
