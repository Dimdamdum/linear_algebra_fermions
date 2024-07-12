import matplotlib.pyplot as plt
import numpy as np

def lists_to_plots(list_of_lists):
    numb_of_lists = len(list_of_lists)
    size = int(np.sqrt(numb_of_lists)) + 1
    num_rows = size
    num_cols = size

    # Create a figure and a set of subplots
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(10, 8))

    # Flatten the list of axes for easier indexing
    axs = axs.flatten()

    # Plot each list in the corresponding subplot
    for i, sublist in enumerate(list_of_lists):
        x_values = list(range(len(sublist)))
        y_values = sublist
        axs[i].plot(x_values, y_values, marker='o')
        axs[i].set_title(f'Plot {i + 1}')
        axs[i].set_xlabel('Index (i)')
        axs[i].set_ylabel('Value (list[i])')

    # Adjust layout
    plt.tight_layout()

    # Show the plot
    plt.show()

#test:
list_of_lists = [
    [1, 2, 3, 4],
    [2, 4, 6, 8],
    [1, 4, 9, 16],
    [1, 3, 6, 10],
    [1, 2, 3.5]
]

#lists_to_plots(list_of_lists)
