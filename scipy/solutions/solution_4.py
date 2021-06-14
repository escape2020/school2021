# flake8: noqa
from matplotlib.colors import LogNorm, PowerNorm
rate, data = wavfile.read('./data/synth_sound.wav')
f, t, Sxx = signal.spectrogram(data, rate)
plt.pcolormesh(t, f, Sxx, norm=PowerNorm(0.1), shading='auto')
plt.ylabel('Frequency / Hz')
plt.xlabel('Time / s')
plt.xlim([0, 4])

