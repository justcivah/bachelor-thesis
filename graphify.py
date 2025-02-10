import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.colors

def plot_graph(data, y_column, y_label, filename, color):
    """Generates and saves a plot with consistent styling parameters."""
    plt.figure(figsize=(10, 6))
    plt.plot(data['epoch'], data[y_column], color=color, lw=6)
    
    # Crea una versione più chiara del colore con trasparenza
    light_color = tuple(c * 0.5 + 0.5 for c in matplotlib.colors.to_rgb(color))
    
    # Calcola il valore minimo e massimo della curva
    y_min = data[y_column].min()
    y_max = data[y_column].max()
    
    # Aggiungi un margine del 10% sopra e sotto
    margin = 0.10 * (y_max - y_min)
    plt.ylim(y_min - margin, y_max + margin)
    
    # Calcola l'offset di 0.5 cm in unità di dati dell'asse y
    ax = plt.gca()
    fig = plt.gcf()
    bbox = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    height_inches = bbox.height 
    height_cm = height_inches * 2.54 
    data_range = y_max + margin - (y_min - margin)
    offset_cm = 0.5
    offset_data = (offset_cm / height_cm) * data_range
    
    # Riempie l'area sotto la curva, lasciando 0.5 cm di spazio dall'asse x
    plt.fill_between(data['epoch'], data[y_column], y_min - margin + offset_data, color=light_color, alpha=0.3)
    
    plt.xlabel('Epoca', fontsize=37, labelpad=30)
    plt.ylabel(y_label, fontsize=37, labelpad=30)
    plt.tick_params(axis='both', which='major', labelsize=34)
    plt.grid(True, which='both', axis='both', color='#f0f0f0', linestyle='-', linewidth=1)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

# Load CSV data
data = pd.read_csv("results.csv")

# Configure global plot settings
sns.set(style="whitegrid")
plt.rcParams.update({
    "text.usetex": True,
    "font.weight": "bold",
    "axes.labelweight": "bold",
    "font.family": "serif",
    "text.latex.preamble": r"""
        \usepackage[utf8]{inputenc}
        \usepackage[T1]{fontenc}
        \usepackage{amsmath}
        \usepackage{bm}
        \AtBeginDocument{\boldmath\bfseries}
    """
})

# Generate all plots using the function
plot_graph(data, 'train/seg_loss', 'Loss addestramento', 'train-loss.pdf', '#5b8db8')
plot_graph(data, 'val/seg_loss', 'Loss validazione', 'validation-loss.pdf', '#e2975d')
#plot_graph(data, 'val/seg_loss', 'Loss testing', 'testing-loss.pdf', '#e2975d')
plot_graph(data, 'metrics/mAP50(M)', 'mAP50', 'map50.pdf', '#82a67d')
plot_graph(data, 'metrics/mAP50-95(M)', 'mAP50-95', 'map50-95.pdf', '#ba3f98')