import a_star
import rrt
import line_plotter

# importing all the necessary modules
from PIL import Image
import numpy as np
import matplotlib.pyplot as plot
import time
import math
import os
from path_planner_visualizer import RoverDomainVisualizer


if __name__ == '__main__':
    # Obtains the path to the current working directory
    directory_main = os.getcwd()
    # The directory from which we may load maps
    directory_maps = directory_main + '\Maps\\'
    # The list of maps to load
    maps_to_load = 'map_3'
    # The coordinate to start from
    start_coordinate = (20, 0) # 1. (20,0), 2. (0,0), 3. (0,0)
    # The coordinate to end at
    end_coordinate = (145,140) # 1. (145,140), 2. (290,290), 3. (490,490)
    print("Planner started")
    # Reads in the bitmap world images (obstacles are zeros and free space are ones)
    world_map = Image.open(directory_maps + maps_to_load + '.bmp')
    # Converts the image into a numpy array
    world_map = np.abs(np.array(world_map)-1)
    # Creates an RGB Version of the world map
    world_map_rgb = line_plotter.concat_channels(world_map, world_map, world_map)


    # ---------- Plot Layout ----------
    # Specify that we require subplots along two rows and two columns
    figure, axis = plot.subplots(1, 2)
    # Specifying the primary plot title
    figure.suptitle('Results for map: ' + maps_to_load)
    #print("before A-star")


    # ---------- A* Algorithm ----------
    # Uses the A_star algorithm to find the shortest route to the goal
    path, path_length, computation_time, coordinates_expanded = a_star.find_path(world_map, start_coordinate,
                                                                                 end_coordinate)
    # We initialize the visualization object with the number of rovers and the grid size (width x height)
    visualizer = RoverDomainVisualizer(1, (150, 150))

    path = path[::-1]

    for pos in range(len(path)+10):
        if pos >= len(path)-1:
            pos = len(path)-1
            # We update the visualizer
            visualizer.update_visualizer([(path[pos][1], path[pos][0])], [end_coordinate], [True], False, 0.05)
        else:
            # We update the visualizer
            visualizer.update_visualizer([(path[pos][1], path[pos][0])], [end_coordinate], [False], False, 0.05)


    # Adds lines to the plot
    line_plotter.plot_lines(axis[0], path, 'red')
    # We mark orange for all the coordinates expanded by the A* algorithm
    map_rgb_temp = line_plotter.color_marker(world_map_rgb, coordinates_expanded, [255, 165, 0])
    # Plotting the image with a grayscale colormap
    axis[0].imshow(map_rgb_temp, cmap='gray')
    # Specifying the plot title
    axis[0].set_title('A* run time: ' + format(computation_time, '.2f') + ' seconds')
    # Specifying the label for the x-axis
    axis[0].set_xlabel('Map Columns')
    # Specifying the label for the y-axis
    axis[0].set_ylabel('Map Rows')
    print("A-star completed")


    # ---------- RRT Algorithm ----------
    # Uses the RRT algorithm to find a path to the destination
    path, path_length, computation_time, branch_set = rrt.find_path(world_map, start_coordinate,
                                                                    end_coordinate, 10, 10)

    # We initialize the visualization object with the number of rovers and the grid size (width x height)
    visualizer = RoverDomainVisualizer(1, (150, 150))

    path = path[::-1]

    for pos in range(len(path) + 10):
        if pos >= len(path) - 1:
            pos = len(path) - 1
            # We update the visualizer
            visualizer.update_visualizer([(path[pos][1], path[pos][0])], [end_coordinate], [True], False, 0.3)
        else:
            # We update the visualizer
            visualizer.update_visualizer([(path[pos][1], path[pos][0])], [end_coordinate], [False], False, 0.3)

    # Adds rrt branch lines to the plot
    line_plotter.plot_branches(axis[1], branch_set, 'orange')
    # Adds rrt path lines to the plot
    line_plotter.plot_lines(axis[1], path, 'red')
    # Plotting the image with a grayscale colormap
    axis[1].imshow(world_map_rgb, cmap='gray')
    # Specifying the plot title
    axis[1].set_title('RRT run time: ' + format(computation_time, '.2f') + ' seconds')
    # Specifying the label for the x-axis
    axis[1].set_xlabel('Map Columns')
    # Specifying the label for the y-axis
    axis[1].set_ylabel('Map Rows')
    print("RRT completed")


    # Display the image
    plot.show()