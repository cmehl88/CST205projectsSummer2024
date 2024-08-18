"""
Carson Mehl
Cst205
7/21/2024
Lab - Digital Audio Pt2
Summary: Creates a .wav file with multiple notes at the same time
called chords. This .wav file is then passed to the file sound2_gui.py to 
be used in, sound2_gui is not complete.
"""

import numpy as np
from scipy.io.wavfile import write

# CD audio at 44,100 Hz
SAMPLES_S = 44_100
frequencies = [220, 330, 395]  
# Time in seconds of note
duration = 2.0

# Example from slides
def create_pcm(frequency, duration, sample_rate=SAMPLES_S):
    ang_freq = 2 * np.pi * frequency
    num_samples = int(sample_rate * duration)
    x_vals = np.arange(num_samples)

    # sin() function between 1 and -1, so we scale value by 32767
    # but also leave some headroom (.3 reduction)
    y_vals = 32767 * 0.3 * np.sin(ang_freq * x_vals / sample_rate)
    return np.int16(y_vals)

# Function to create the chord, takes parameters to get samples then save as .wav
def chord(frequencies, duration, sample_rate=SAMPLES_S):
    num_samples = int(sample_rate * duration)
    combined_waveform = np.zeros(num_samples, dtype=np.float32)

    # Get each frequency
    for freq in frequencies:
        waveform = create_pcm(freq, duration, sample_rate)
        combined_waveform += waveform

    # Normalize to avoid clipping (without this it's very static!)
    max_val = np.max(np.abs(combined_waveform))
    if max_val > 0:
        combined_waveform = combined_waveform / max_val
    combined_waveform = np.int16(combined_waveform * 32767)

    # Write to the .wav file
    write('chord.wav', sample_rate, combined_waveform)
chord(frequencies, duration)