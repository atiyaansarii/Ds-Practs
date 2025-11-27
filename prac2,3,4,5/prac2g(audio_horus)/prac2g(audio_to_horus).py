# audio to horus :-
import pandas as pd
from scipy.io import wavfile

# Input and Output Files
audio_file = "C:/Atiya/FY-MSC-IT/Data Science/DS Practs/sample_audio.wav"  # Path to the audio file
output_csv = "C:/Atiya/FY-MSC-IT/Data Science/DS Practs/HORUS-Audio.csv"   # Path to save the CSV file

# Read the audio file
sample_rate, audio_data = wavfile.read(audio_file)

# Create time values for each sample
time_stamps = [i / sample_rate for i in range(len(audio_data))]

# If the audio is stereo, handle each channel separately
if audio_data.ndim == 1:  # Mono audio
    horus_data = {"Time (s)": time_stamps, "Channel": 1, "Amplitude": audio_data}
else:  # Stereo audio
    horus_data = {
        "Time (s)": time_stamps * 2,
        "Channel": [1] * len(time_stamps) + [2] * len(time_stamps),
        "Amplitude": list(audio_data[:, 0]) + list(audio_data[:, 1]),
    }

# Convert to a DataFrame and save as CSV
df = pd.DataFrame(horus_data)
df.to_csv(output_csv, index=False)

print(f"Audio converted to HORUS format and saved as: {output_csv}")
