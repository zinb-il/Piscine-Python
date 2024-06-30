from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm


# print(tqdm.__doc__)
# for elem in ft_tqdm(range(0,10)):
#     sleep(0.5)
# print()
for elem in tqdm(range(10,100)):
    sleep(5)
print()

# colors = ["Blue","Green","Yellow","White","Gray","Black"]
# for x in tqdm(colors):
#     sleep(1)
#     print(x)
