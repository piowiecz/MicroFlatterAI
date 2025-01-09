import numpy as np
import random
import matplotlib as plt
from main import floor_matrix

# Parametry środowiska
Input_GRID = floor_matrix
WALL_COST = 100  # Koszt budowy jednej ściany
PRICE_per_m2 = 12000  # Cena sprzedaży jednego mikromieszkania
PRICE_per_flat = 10000
PURCHASE_COST = 2000000  # Koszt zakupu całego mieszkania


# Funkcja nagrody
def calculate_reward(grid):
    # Liczba mikromieszkań (obszar zamknięty przez ściany)
    flats = count_flats(grid)
    profit = (PRICE_per_m2 * flat_area) - (np.sum(grid) * WALL_COST) - PURCHASE_COST
    return profit

def count_area(grid):
    pass

# Funkcja licząca zamknięte obszary (mikromieszkania)
def count_flats(grid):
    # Prosty przykład: każdy zamknięty obszar to jedno mikromieszkanie
    # Można tu zastosować bardziej zaawansowane algorytmy (np. DFS).
    return np.sum(grid == 0)


# Inicjalizacja Q-learning
Q = np.zeros((GRID_SIZE, GRID_SIZE, 4))  # Stany: każdy punkt siatki, 4 akcje (góra, dół, lewo, prawo)
actions = ["up", "down", "left", "right"]
learning_rate = 0.1
discount_factor = 0.9
epsilon = 0.1  # Eksploracja/eksploatacja


# Symulacja środowiska
def step(grid, x, y, action):
    new_x, new_y = x, y
    if action == "up" and x > 0:
        new_x -= 1
    elif action == "down" and x < GRID_SIZE - 1:
        new_x += 1
    elif action == "left" and y > 0:
        new_y -= 1
    elif action == "right" and y < GRID_SIZE - 1:
        new_y += 1
    # Dodanie ściany
    grid[new_x, new_y] = 1
    reward = calculate_reward(grid)
    return grid, new_x, new_y, reward


# Trenowanie agenta
episodes = 1000
for episode in range(episodes):
    grid = np.zeros((GRID_SIZE, GRID_SIZE))
    x, y = 0, 0  # Startowy punkt agenta
    total_reward = 0

    for _ in range(50):  # Maksymalna liczba kroków w jednym epizodzie
        if random.uniform(0, 1) < epsilon:
            action = random.choice(actions)  # Eksploracja
        else:
            action = actions[np.argmax(Q[x, y])]  # Eksploatacja

        # Wykonanie akcji
        new_grid, new_x, new_y, reward = step(grid, x, y, action)
        total_reward += reward

        # Aktualizacja Q-learning
        old_value = Q[x, y, actions.index(action)]
        next_max = np.max(Q[new_x, new_y])
        Q[x, y, actions.index(action)] = old_value + learning_rate * (reward + discount_factor * next_max - old_value)

        # Przejście do nowego stanu
        x, y = new_x, new_y

    if episode % 100 == 0:
        print(f"Episode {episode}: Total Reward: {total_reward}")

# Wyświetlenie wyników
print("Trening zakończony!")
print("Optymalny Q-Table:")
print(Q)


# Funkcja rysująca końcowy plan mieszkania
def plot_plan(grid):
    plt.figure(figsize=(6, 6))
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if grid[x, y] == 1:  # Ściana
                plt.fill_between([y, y + 1], x, x + 1, color="gray")
    plt.grid(True)
    plt.title("Końcowy plan mieszkania")
    plt.xticks(range(GRID_SIZE + 1))
    plt.yticks(range(GRID_SIZE + 1))
    plt.show()


# Rysowanie planu
plot_plan(final_grid)

