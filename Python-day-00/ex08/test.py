from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm


# # print(tqdm.__doc__)

# # Test1
for elem in ft_tqdm(range(10)):
    sleep(0.5)
print()
for elem in tqdm(range(10)):
    sleep(0.5)
print()


# # Test2
for elem in ft_tqdm(range(333)):
    sleep(0.05)
print()
for elem in tqdm(range(333)):
    sleep(0.05)
print()


# # Test3
colors = ["Blue", "Green", "Yellow", "White", "Gray", "Black"]

for x in tqdm(colors):
    sleep(1)

for x in ft_tqdm(colors):
    sleep(1)
    

# # Test4
for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()
for elem in tqdm(range(333)):
    sleep(0.005)
print()
