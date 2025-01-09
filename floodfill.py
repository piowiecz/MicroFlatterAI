def flood_fill(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    regions = []  # To store information about each region

    # Directions for moving in the grid: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def is_valid(x, y):
        """Check if the position is within the grid and not visited."""
        return 0 <= x < rows and 0 <= y < cols and not visited[x][y] and grid[x][y] == 0

    def flood_fill_region(x, y):
        """Flood-fill to find the area and elements of the region."""
        stack = [(x, y)]
        visited[x][y] = True
        area = 0
        elements = []

        while stack:
            cx, cy = stack.pop()
            area += 1
            elements.append((cx, cy))

            # Explore neighbors
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if is_valid(nx, ny):
                    visited[nx][ny] = True
                    stack.append((nx, ny))

        return area, elements

    # Main loop to process the entire grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0 and not visited[i][j]:  # Start a new region
                area, elements = flood_fill_region(i, j)
                regions.append({"area": area, "elements": elements})

    # Identify the smallest regions
    if regions:
        smallest_area = min(regions, key=lambda x: x["area"])["area"]
        smallest_regions = [r for r in regions if r["area"] == smallest_area]
    else:
        smallest_regions = []

    return len(regions), regions, smallest_regions
