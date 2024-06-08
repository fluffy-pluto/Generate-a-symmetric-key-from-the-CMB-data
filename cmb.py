import numpy as np
from hashlib import sha512

# Simulate CMB power spectral data
def simulate_cmb_power_spectrum(size):
# The CMB power spectrum typically has a bell-curve like shape.
# Here we simulate it with random numbers from a CMB power distribution spectrum.
    return np.random.normal(size=size)

# Generate symmetric key from CMB power spectrum data.
def generate_symmetric_key(cmb_data):
# Convert the CMB data to bytes
    cmb_bytes = cmb_data.tobytes()

# Hash the bytes from above using SHA-512 or something else to generate a symmetric key.
    key = sha512(cmb_bytes).digest()

    return key

# CMB power spectrum simulation. Insert a numerical value in the bracket.
cmb_data = simulate_cmb_power_spectrum(456456)

# Generate a symmetric key from the CMB data.
key = generate_symmetric_key(cmb_data)

print("Symmetric key:", key)
