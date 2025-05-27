import random
import matplotlib.pyplot as plt

# Setup
N = 100       # total population
days = 50     # number of days to simulate
beta = 0.1   # infection probability
infectious_period = 5

# State: 'S', 'I', or 'R'
people = ['S'] * N
people[0] = 'I'  # initial infected person
days_infected = [0] * N

history = {'S': [], 'I': [], 'R': []}

# Simulation
for day in range(days):
    new_people = people.copy()
    for i, state in enumerate(people):
        if state == 'I':
            for j in range(N):
                if people[j] == 'S' and random.random() < beta:
                    new_people[j] = 'I'
            days_infected[i] += 1
            if days_infected[i] >= infectious_period:
                new_people[i] = 'R'
    people = new_people

    # Count
    history['S'].append(people.count('S'))
    history['I'].append(people.count('I'))
    history['R'].append(people.count('R'))

# Plot
plt.plot(history['S'], label='Susceptible')
plt.plot(history['I'], label='Infected')
plt.plot(history['R'], label='Recovered')
plt.xlabel('Day')
plt.ylabel('People')
plt.legend()
plt.title('Toy Epidemic Simulation')
plt.show()