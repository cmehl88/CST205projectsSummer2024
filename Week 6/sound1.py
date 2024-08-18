"""
Carson Mehl
Cst205
7/21/2024
Lab - Digital Audio Pt1
Summary: First sound python program. Creates sound with a few notes,
then saves it to sound.wav file.
"""

import numpy as np
from scipy.io.wavfile import write

# Task 1 and 2
# CD audio at 44,100 Hz
SAMPLES_S = 44_100

# Functioned used to create x and y vals from notes and duration passed in
# Function from slide examples
def create_pcm(frequency, duration):
    ang_freq = 2 * np.pi * frequency
    num_samples = int(SAMPLES_S * duration)
    x_vals = np.arange(num_samples)

    # sin() function between 1 and -1, so we scale value by 32767
    # but also leave some headroom (.3 reduction)
    y_vals = 32767 * .3 * np.sin(ang_freq * x_vals / SAMPLES_S)

    return np.int16(y_vals)

# List of frequencies and their durations in seconds
notes = [
    (200.0, 2.0),  # Note 1 for 2 seconds
    (392.0, 2.0),  # Note 2 for 2 seconds and so on
    (523.25, 2.0), 
    (100.0, 2.0) 
]

# Initialize an empty array to hold the entire waveform
the_waveform = np.array([], dtype=np.int16)

# Generate each note's waveform and concatenate them one after the other in order
for freq, dur in notes:
    note_waveform = create_pcm(freq, dur)
    the_waveform = np.concatenate((the_waveform, note_waveform))

# Write to the .wav file
write('sound.wav', SAMPLES_S, the_waveform)