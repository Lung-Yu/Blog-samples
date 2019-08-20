import numpy as np
import random

def shuffle(*args):
    seed = random.randint(0,2**32)
    rand_state = np.random.RandomState(seed)
    for lst in args:
        rand_state.shuffle(lst)
        rand_state.seed(seed)
