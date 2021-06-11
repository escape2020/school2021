# flake8: noqa
corr = signal.correlate(
    alien_signal,
    signal.boxcar(sample_length),
    mode='same'
) / sample_length # divide by sample length to normalize output


# plot stuff
plt.figure()
plt.plot(corr)
plt.plot(clock, corr[clock], 'ro')
plt.axhline(0.5, ls='--', color='gray')


# decode the aline message
a = np.where(corr[clock] > 0.5, 1, 0)
s = bytearray(np.packbits(a)).decode('ascii')

print(f'Decoded Alien Message is: "{s}" ')
