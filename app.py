import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render
import seaborn as sns

# Add page options
ui.page_opts(title="Pyshiny App",fillable=True)

# create a sidebar with slider input
with ui.sidebar():
    # Add a slider for specifying the number of bins in the histogram.
    # The ui.input_slider function is called with 5 arguments:
    # 1. A string id ("selected_number_of_bins") that uniquely identifies this input.
    # 2. A string label (e.g., "Number of Bins") to be displayed alongside the slider.
    # 3. An integer representing the minimum number of bins
    # 4. An integer representing the maximum number of bins
    # 5. An integer representing the initial value of the slider
    ui.input_slider("selected_number_of_bins", "Number_of_bins", 0, 100, 20)


@render.plot(alt="A histogram showing random data distribution")
def histogram():
    np.random.seed(19680801)
    x = 100 + 15 * np.random.randn(437)
    plt.hist(x, input.selected_number_of_bins(), density=True,color='orange')

@render.plot(alt="2D histogram plot")
def histogram_2d():
    count_of_point: int = 500
    np.random.seed(42)
    x = np.random.randn(count_of_point)
    y = np.random.randn(count_of_point)
    plt.hist2d(x=x, y=y, bins=input.selected_number_of_bins(), cmap = "RdYlGn_r")
