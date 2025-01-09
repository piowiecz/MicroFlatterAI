The main.py script loads an apartment plan from a .png file and allows you to set the scale of the projection. The example uses the conversion factor 1px = 1cm.
It then converts the apartment plan to an array and assigns the appropriate regions. 0 - empty space, 1 - partition wall, 2 - load-bearing wall.
As a result, we additionally get a graph depicting the loaded array.

The floodfill.py script implements the flood-fill algorithm for analyzing a two-dimensional grid (such as an array).
Its goal is to find all regions (connected areas of 0 space), their size (number of cells), and identify the smallest regions.


The q-learning.py script implements a simulation using Q-learning to optimize the placement of walls in a grid that represents living space. The main goal is to maximize profits from the construction and sale of micro-apartments, taking into account the cost of construction and purchase of the apartment.
