import numpy as np

def draw_suspect():
    s = np.random.choice(["E", "S"], p=(0.65, 0.35))
    return s

def observation_model(s: str):
    if s == "E":
        return np.random.choice(["U", "A", "C"], p=(0.25, 0.10, 0.65))
    return np.random.choice(["U", "A", "C"], p=(0.35, 0.15, 0.50))

def simulate_many(num_sims):
    sims = []
    for _ in range(num_sims):
        s = draw_suspect()
        w = observation_model(s)
        sims.append(f"{s}-{w}")
    return sims

num_sims = 100
simulations = simulate_many(num_sims)
scenarios, freqs = np.unique(simulations, return_counts = True)
print(list(scenarios))
print(np.round(freqs / num_sims, 2))

num_sims = 1000
simulations = simulate_many(num_sims)
scenarios, freqs = np.unique(simulations, return_counts = True)
print(list(scenarios))
print(np.round(freqs / num_sims, 5))

num_sims = 10000
simulations = simulate_many(num_sims)
scenarios, freqs = np.unique(simulations, return_counts = True)
print(list(scenarios))
print(np.round(freqs / num_sims, 5))

num_sims = 100000
simulations = simulate_many(num_sims)
scenarios, freqs = np.unique(simulations, return_counts = True)
print(list(scenarios))
print(np.round(freqs / num_sims, 5))

num_sims = 1000000
simulations = simulate_many(num_sims)
scenarios, freqs = np.unique(simulations, return_counts = True)
print(list(scenarios))
print(np.round(freqs / num_sims, 5))