import random
import time

def monte_carlo_sim(total_points):
    inside_circle = 0
    for i in range(total_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if (x**2 + y**2) <= 1:
                inside_circle += 1
    ratio = (inside_circle/total_points)
    pi_approx = ratio * 4
    print("Ratio: ", ratio, "PI Approx: ", pi_approx)
    return pi_approx

start_time = time.time()  # Record the start time

pi_estimate_1 = monte_carlo_sim(100)
pi_estimate_2 = monte_carlo_sim(1000)
pi_estimate_3 = monte_carlo_sim(100000)

end_time = time.time()  # Record the end time
elapsed_time = end_time - start_time  # Calculate elapsed time
print("Simulation Time: ", elapsed_time, " seconds")    