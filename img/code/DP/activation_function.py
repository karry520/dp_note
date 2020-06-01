import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

from matplotlib import rc, rcParams
rcParams["text.latex.preamble"] = [r"\usepackage{amsmath}"]
rcParams["text.usetex"] = True

fig, ax = plt.subplots(3, 2)

# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)

x = np.linspace(-10, 10, 500)
y1 = 1 / (1 + np.exp(-x))
y2 = np.tanh(x)
y3 = np.maximum(0, x)
y4 = np.maximum(0.2 * x, x)
y5 = []
for t in x:
    if t >= 0:
        y5.append(t)
    else:
        y5.append(0.1 * (np.exp(t) - 1))
y6 = []
Y = [y1, y2, y3, y4, y5, y6]
ano1 = [
    r"$\mathrm{Sigmoid}$",
    r"$\sigma(x)=\frac{1}{1+e^{-x}}$"
]
ano2 = [
    r"$\mathrm{tanh}$",
    r"$\mathrm{tanh}(x)$"
]
ano3 = [
    r"$\mathrm{ReLU}$",
    r"$\mathrm{max}(0,x)$"
]
ano4 = [
    r"$\mathrm{Leaky ReLU}$",
    r"$\mathrm{max}(0.1x,x)$"
]
ano5 = [
    r"$\mathrm{ELU}$",
    r"$\begin{cases} x& x\leq 0 \\ \alpha (e^x-1)& x < 0\end{cases}$"
]
ano6 = [
    r"$\mathrm{Maxout}$",
    r"$\max(w_1^Tx+b_1,w_2^Tx+b_2)$"
]
P = [[0.8, 0.5], [0.6, 0.2], [8, 6], [7.8, 5.4], [8, 4], [5, 1]]

Ano = [ano1, ano2, ano3, ano4, ano5, ano6]
for i in range(0, 3):
    for j in range(0, 2):
        idx = i * 2 + j
        if idx < 5:
            ax[i][j].spines['left'].set_position('center')
            ax[i][j].spines['right'].set_color('none')
            # ax[i][j].spines['bottom'].set_position('center')
            ax[i][j].spines['top'].set_color('none')

            ax[i][j].plot(x, Y[idx], color='k', lw=1, ls="-")
            ax[i][j].text(-10, P[idx][0], Ano[idx][0], fontsize=8, color='r')
            ax[i][j].text(-10, P[idx][1], Ano[idx][1], fontsize=8)
        else:
            ax[i][j].spines['left'].set_color('none')
            ax[i][j].spines['right'].set_color('none')
            ax[i][j].spines['bottom'].set_color('none')
            ax[i][j].spines['top'].set_color('none')
            ax[i][j].get_xaxis().set_visible(False)
            ax[i][j].get_yaxis().set_visible(False)

            ax[i][j].text(0.3, 0.2, Ano[idx][0], fontsize=12, color='r')
            ax[i][j].text(0.3, 0, Ano[idx][1], fontsize=8)


# plt.savefig("./activation.jpg")
# plt.show()
pdf = PdfPages("./activation.pdf")
pdf.savefig()

plt.close()
pdf.close()
