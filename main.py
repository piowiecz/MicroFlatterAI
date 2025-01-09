import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from floodfill import *

# Wczytaj obraz rzutu architektonicznego
image_path = "Kawalerki.png"  # Zamień na ścieżkę do swojego obrazu
scale = 0.001  # Skala: 1 piksel = 1 cm (przykład, dostosuj do swojej skali)

# Wczytanie obrazu i konwersja do skali szarości
image = Image.open(image_path).convert('L')
image_array = np.array(image)

# Wyznaczenie wymiarów obrazu w metrach
pixel_size = 0.01  # Wymiary jednego piksela w metrach (przykładowo 1 cm)
height, width = image_array.shape
real_width = width * pixel_size
real_height = height * pixel_size

# Podział na siatkę 10x10 cm (1 element siatki = 10 pikseli)
grid_size = int(0.1 / pixel_size)  # Liczba pikseli odpowiadających 10 cm
rows = height // grid_size
cols = width // grid_size

# Macierz wynikowa
floor_matrix = np.zeros((rows, cols), dtype=int)


# Funkcja klasyfikująca piksele (prosty przykład)
def classify_region(region):
    avg_intensity = np.mean(region)
    if avg_intensity > 250:  # Jasny obszar -> przestrzeń otwarta
        return 0
    elif avg_intensity > 120:  # Szary obszar -> ściana działowa
        return 1
    else:  # Ciemny obszar -> ściana nośna
        return 2

print(image_array)

# Iteracja przez siatkę 10x10 cm
for i in range(rows):
    for j in range(cols):
        region = image_array[
            i * grid_size:(i + 1) * grid_size,
            j * grid_size:(j + 1) * grid_size
        ]
        floor_matrix[i, j] = classify_region(region)

# Wyświetlenie wynikowej macierzy
print(floor_matrix)

plt.imshow(floor_matrix, cmap='viridis')
plt.colorbar(label='Typ obszaru')
plt.title('Rzut piętra jako macierz')
plt.savefig("matrix.png")


# Run the algorithm
num_regions, all_regions, smallest_regions = flood_fill(floor_matrix)

# Output the results
print(f"Number of regions: {num_regions}")

# Print details of all regions
print("\nAll Regions:")
for idx, region in enumerate(all_regions):
    print(f"Region {idx + 1}:")
    print(f"  Area: {region['area']}")
    print(f"  Elements: {region['elements']}")

# Print details of the smallest regions
print("\nSmallest Regions:")
for idx, region in enumerate(smallest_regions):
    print(f"Region {idx + 1}:")
    print(f"  Area: {region['area']}")
    print(f"  Elements: {region['elements']}")
