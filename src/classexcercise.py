import numpy as np 

rng = np.random.default_rng(seed=11)

x = rng.binomial(n=1, p=0.6, size=100000)



import numpy as np
rng = np.random.default_rng(42)
draws = rng.binomial(n=12, p=0.36, size=200_000)
estimate = (draws == 4).mean()


rng = np.random.default_rng(seed=0)
draws = rng.binomial(15, 0.58, size=100_000)
print((draws >= 12).mean())