from tqdm import trange

for x in trange(10000):
	with open("data.txt", "a") as f:
		f.write(f"{x} line \n")

print("Hello Feature! Changes in Feature 2")

print("Change in Feature3")
