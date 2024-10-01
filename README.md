# Audio-Desnoising-AutoEncoder
## Denoising Audio Signals Using Convolutional Autoencoder

This project focuses on building a **Convolutional Autoencoder (CAE)** to denoise audio signals. The goal is to remove noise from audio signals, improving their quality for further processing and analysis.

## Project Overview

In many real-world scenarios, audio signals are affected by various types of noise that can degrade their quality. This project leverages deep learning techniques, specifically Convolutional Autoencoders, to learn and recover clean signals from noisy inputs.

The model is trained on audio samples converted into spectrograms using Short-Time Fourier Transform (STFT). After denoising, the output spectrogram is converted back into an audio signal.

## Model Architecture

The Convolutional Autoencoder is used to learn a compressed representation of the noisy audio signal and reconstruct the denoised signal. The architecture consists of:

1. **Encoder**: A series of convolutional layers that capture the essential features of the noisy signal.
2. **Decoder**: A series of transposed convolutional layers that reconstruct the clean signal from the compressed representation.

## Getting Started

### Prerequisites

- Python 3.x
- Libraries:
  - `librosa`
  - `numpy`
  - `matplotlib`
  - `tensorflow` 
  - `scikit-learn`

You can install the required packages by running:

```bash
pip install -r requirements.txt
