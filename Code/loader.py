import librosa
import numpy as np

class Loader:
    """Loader is responsible for loading an audio file."""
    
    def __init__(self, sample_rate, duration, mono):
        self.sample_rate = sample_rate
        self.duration = duration
        self.mono = mono

    def load(self, file_path):
        signal, _ = librosa.load(file_path, sr=self.sample_rate, duration=self.duration, mono=self.mono)
        return signal

def calculate_duration(hop_length, num_frames, sample_rate):
    # Calculate duration from number of frames, hop length, and sample rate
    duration_seconds = (num_frames * hop_length) / sample_rate
    return duration_seconds

if __name__ == "__main__":
    SAMPLE_RATE = 22050
    HOP_LENGTH = 256  # From your LogSpectrogramExtractor
    FRAME_COUNT = 256  # Dimension for the time frame from (None, 256, 259, 1)

    # Calculate duration for a single file
    duration_seconds = calculate_duration(HOP_LENGTH, FRAME_COUNT, SAMPLE_RATE)
    print(f"Duration of the signal for frame count 259: {duration_seconds} seconds")
