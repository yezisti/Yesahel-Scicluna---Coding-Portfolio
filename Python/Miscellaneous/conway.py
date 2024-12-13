# Simulates Conway's Game of Life using Pygame
# Reproduced from https://www.youtube.com/watch?v=cRWg2SWuXtM

import time, pygame
import numpy as np

# Settings:
# Scale factors for window size based on desktop dimensions
width_scale = 0.5
height_scale = 0.5
# Size of each cell in the grid
cell_size = 20
# Delay between updates when the simulation is running
latency = 0.0
# Colours for the background, living cells, dying cells, and grid lines
background_colour = (10, 10, 10)
living_cell_colour = (255, 255, 255)
dying_cell_colour = (170, 170, 170)
grid_colour = (40, 40, 40)

def update(screen, cells, with_progress=False):
    """
    Updates the grid of cells based on Conway's Game of Life rules and displays 
    it.
    
    Parameters:
        screen (pygame.Surface): The surface to draw the grid on.
        cells (numpy.ndarray): The current state of the grid (0 for dead, 1 for 
        alive).
        with_progress (bool): Whether to visually highlight changes (e.g., dying
        cells).
    
    Returns:
        numpy.ndarray: The updated grid after applying the game's rules.
    """
    # Create an empty grid to store the updated state
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    # Iterate through each cell in the grid
    for row, col in np.ndindex(cells.shape):
        # Count the number of alive neighbours
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        # Default colour is background unless cell is alive
        colour = background_colour if cells[row, col] == 0 else living_cell_colour

        # Apply rules for live cells
        if cells[row, col] == 1:
            # Cell dies if under- or over-populated
            if alive < 2 or alive > 3:  
                if with_progress:
                    colour = dying_cell_colour
            # Cell survives
            elif 2 <= alive <= 3:  
                updated_cells[row, col] = 1
                if with_progress:
                    colour = living_cell_colour
        else:
            # Apply rules for dead cells: become alive if exactly 3 neighbours 
            # are alive
            if alive == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    colour = living_cell_colour

        # Draw the cell on the screen
        pygame.draw.rect(screen, colour,
                        (col * cell_size, row * cell_size,
                         cell_size - 1, cell_size - 1))

    # Update the display with the new grid
    pygame.display.update()

    return updated_cells

def main():
    """
    Main function to initialise and run the Game of Life simulation.
    """
    # Initialise Pygame and set the window title
    pygame.init()
    pygame.display.set_caption("Conway's Game of Life")

    # Get screen dimensions and set up the Pygame window
    desktop_width, desktop_height = pygame.display.get_desktop_sizes()[0]
    screen = pygame.display.set_mode((desktop_width * width_scale,
                                      desktop_height * height_scale * 0.9))
    screen.fill(grid_colour)

    # Create a grid of cells, all initially dead (0)
    cells = np.zeros((int(desktop_height * height_scale * 0.9 // cell_size), 
                      int(desktop_width * width_scale // cell_size)))
    update(screen, cells)

    # The simulation is paused initially
    running = False  

    # Main event loop
    while True:
        # Handle events (quit, toggle simulation, draw cells)
        for event in pygame.event.get():
            # Quit the application
            if event.type == pygame.QUIT:  
                pygame.quit()
                return
            # Toggle running state with Space key
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  
                    running = not running
            # Draw living cells with left mouse button
            if pygame.mouse.get_pressed()[0]:  
                pos = pygame.mouse.get_pos()
                cells[pos[1] // cell_size, pos[0] // cell_size] = 1
                update(screen, cells)

        # Update the grid if the simulation is running
        if running:  
            cells = update(screen, cells, with_progress=True)
            # Add delay between updates
            time.sleep(latency)  

# Entry point of the script
if __name__ == "__main__":
    # Start the simulation
    main()  
