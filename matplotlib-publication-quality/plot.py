import matplotlib.pyplot as plt
import numpy as np


formula = (
    r'$\displaystyle '
    r'N = \int_{E_\text{min}}^{E_\text{max}} '
    r'\int_0^A'
    r'\int_{t_\text{min}}^{t_\text{max}} '
    r'Φ_0 \left(\frac{E}{\SI{1}{\GeV}}\right)^{\!\!-γ}'
    r' \, \symup{d}A \, \symup{d}t \, \symup{d}E'
    r'$'
)


def power_law_spectrum(energy, normalisation, spectral_index):
    return normalisation * energy**(-spectral_index)


bin_edges = np.logspace(2, 5, 15)
bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])

y = power_law_spectrum(bin_centers, 1e-5, 2.5)
relative_error = np.random.normal(1, 0.2, size=len(y))
y_with_err = relative_error * y

fig, ax = plt.subplots()
ax.errorbar(
    np.log10(bin_centers),
    y_with_err,
    xerr=[
        np.log10(bin_centers) - np.log10(bin_edges[:-1]),
        np.log10(bin_edges[1:]) - np.log10(bin_centers)
    ],
    yerr=0.5 * y_with_err,
    linestyle='',
)

ax.set_xlabel(r'$\log_{10}\bigl(E \mathbin{/} \si{\giga\electronvolt}\bigr)$')
ax.set_ylabel(
    r'$\Phi_0'
    r'\mathbin{/}'
    r'\bigl(\si{\per\GeV\per\second\per\steradian\per\meter\squared}\bigr)$'
)

ax.text(0.1, 0.1, formula, transform=plt.gca().transAxes)
ax.set_yscale('log')

fig.tight_layout(pad=0)
fig.savefig('build/plot.pdf')
