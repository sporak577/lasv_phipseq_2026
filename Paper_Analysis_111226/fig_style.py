# fig_style.py
import matplotlib.pyplot as plt

def apply_style():
    plt.rcParams.update({
        'font.size': 9, 'axes.labelsize': 10, 'axes.titlesize': 11,
        'xtick.labelsize': 9, 'ytick.labelsize': 9, 'legend.fontsize': 9,
        'axes.spines.top': False, 'axes.spines.right': False,
        'svg.fonttype': 'none', 'pdf.fonttype': 42,
    })