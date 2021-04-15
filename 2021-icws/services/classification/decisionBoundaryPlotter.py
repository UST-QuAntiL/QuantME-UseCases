import numpy as np
from SPSAOptimizer import SPSAOptimizer
from matplotlib import cm, gridspec
from matplotlib import pyplot as plt
from math import sqrt


class DecisionBoundaryPlotter():

    @classmethod
    def generate_grid(cls, data, res):
        """ 2D shall suffice for now """
        xlim = np.array([np.min(data[:,0]), np.max(data[:,0])])*1.1
        ylim = np.array([np.min(data[:,1]), np.max(data[:,1])])*1.1

        # generate a grid of res^n_axes points on the canvas
        x_linspace = np.linspace(xlim[0], xlim[1], res)
        y_linspace = np.linspace(ylim[0], ylim[1], res)

        y_grid, x_grid = np.meshgrid(y_linspace, x_linspace)
        grid = np.vstack([x_grid.ravel(), y_grid.ravel()])

        grid2d = grid.T #transform(grid.T)

        return grid2d

    @classmethod
    def predict(cls, results, n_classes, is_statevector):
        n_data = len(results)

        indices = None
        if (n_data == 1):
            results = results[0]
            n_data = len(results.results)
            indices = range(n_data)

        probs, pred_lbls = \
            SPSAOptimizer.computeProbabilities(results, is_statevector, n_data, n_classes, indices)
        return pred_lbls

    @classmethod
    def save_plot(cls, data, labels, grid, predictions, filename):
        """ 2D shall suffice for now """
        fig = plt.figure()
        G = gridspec.GridSpec(1, 1)
        subplot = plt.subplot(G[0, 0])

        """ create a dictionary for coloring the plot """
        classes = list(set(labels))
        n_classes = len(classes)
        colors = cm.get_cmap("rainbow", n_classes)
        colors_dict = {}
        for i in range(n_classes):
            colors_dict[classes[i]] = colors(i)

        """ plot data """
        for i in range(len(labels)):
            subplot.scatter(data[i][0], data[i][1],
                        color=colors_dict[labels[i]],
                        s=100, lw=0, label=labels[i])

        grid_len = len(grid)
        resolution = int(sqrt(grid_len))

        """ plot decision boundary """
        subplot.contourf(grid[:,0].reshape(resolution, resolution), grid[:,1].reshape(resolution, resolution),
                predictions.reshape(resolution, resolution), #colors="k",
                levels=n_classes-1, linestyles=["-"],
                cmap='winter', alpha=0.3)

        """ add legend """
        handles, labels = subplot.get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        subplot.legend(by_label.values(), by_label.keys())

        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close(fig)
