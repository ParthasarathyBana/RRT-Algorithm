# importing the necessary modules
import matplotlib.lines as lines
import numpy as np
import copy


# This function helps to plot lines via the plot axis handle and the path provided list of - (y,x)
def plot_lines(axis, path, colour='red'):

        # Check if the path is empty
        if len(path) < 2:
            # Returns from the function
            return
        else:
            # Gets the first element of the path
            previous_coordinate = path[0]
            # Iterating from the second coordinate in the path till the last coordinate
            for coordinate in path[1:]:
                # Obtaining the line to be plotted
                line = lines.Line2D([previous_coordinate[1], coordinate[1]],
                                    [previous_coordinate[0], coordinate[0]], color=colour)
                # Adding the specified lines to the axis
                axis.add_line(line)
                # The previous coordinate is updated
                previous_coordinate = coordinate


# This function plots lines between sets of two points via the plot axis handle - list of [(y1,x1), (y2,x2)]
def plot_branches(axis, branches, colour='orange'):

        # Check if the path is empty
        if len(branches) == 0:
            # Returns from the function
            return
        else:
            # Iterating from the second coordinate in the path till the last coordinate
            for coordinate in branches:
                # Obtaining the line to be plotted
                line = lines.Line2D([coordinate[0][1], coordinate[1][1]],
                                    [coordinate[0][0], coordinate[1][0]], color=colour)
                # Adding the specified lines to the axis
                axis.add_line(line)


# Concatenate three (height, width) images into one (height, width, 3)
def concat_channels(r, g, b, multiplier=1):
    # In case the R, G and B components don't have matching dimensions
    if r.shape != g.shape or r.shape != b.shape:
        # Raise an exception
        raise Exception('The R, G and B components don\'t have matching dimensions')
    # We initialize the new RGB array
    rgb_array = np.zeros((r.shape[0], r.shape[1], 3), dtype=np.uint8)
    # The first element of third dimension is red channel
    rgb_array[..., 0] = np.minimum(np.multiply(r, multiplier), 255)
    # The second element of third dimension is red channel
    rgb_array[..., 1] = np.minimum(np.multiply(g, multiplier), 255)
    # The third element of third dimension is red channel
    rgb_array[..., 2] = np.minimum(np.multiply(b, multiplier), 255)
    # Returns the RGB array
    return rgb_array


# Marks in a specified color in the image at the coordinates specified within the list
def color_marker(image_rgb, coordinate_list, color):
    # Raises an exception if anything other than an RGB array is passed
    if len(image_rgb.shape) != 3 or image_rgb.shape[2] != 3:
        # Raise an exception
        raise Exception('Can\'t handle non RGB images')
    # We make a shallow copy of the rgb image in order to prevent permanent modification
    image = image_rgb.copy()
    # Iterating through the coordinate list
    for coordinate in coordinate_list:
        # We mark in the color specified at the coordinate
        image[coordinate[0], coordinate[1], :] = color
    # Returns the RGB image
    return image
