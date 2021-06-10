import numpy as np

sample_length = 128

# original message
message = 'beer'

# encoded as ascii bytes
message_bytes = bytearray(message.encode('ascii'))
# 1's and 0's
message_bits = np.unpackbits(message_bytes)

alien_signal = np.repeat(message_bits, sample_length)
alien_signal = np.random.normal(alien_signal, 2)


np.savetxt('alien_signal.txt', alien_signal, fmt='%.4f')
