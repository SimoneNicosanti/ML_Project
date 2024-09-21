import numpy as np

rng = np.random.default_rng(0)
rng_2 = np.random.default_rng(0)

list_1 = []
list_2 = []
for i in range(0, 1_000_000) :
    if (i % 1_000 == 0) :
        rng.random()
        state_1 = rng.bit_generator.state
        rng_2.bit_generator.state = state_1

        list_1.append(rng.random())
        list_2.append(rng_2.random())
    else :
        rng.random()

for i in range(0, len(list_1)) :
    if (list_1[i] != list_2[i]) :
        print("DIFFERENT")