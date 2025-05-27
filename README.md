# Wav2Lip Video Generation Pipeline

This project enables you to create lip-synced videos from an input image and generated audio from a given text prompt. The pipeline converts text into speech (TTS), and then uses the Wav2Lip model to animate the image with synchronized lip movements to match the audio.

---

## 🔥 Features

* Convert any text into audio using TTS (Text-to-Speech)
* Use Wav2Lip to generate a lip-synced video from a static face image and audio
* Automatic audio extraction and video frame preparation
* Resize factor customization to fit different GPU memory requirements
* CUDA support for fast inference

---

## 🛠️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-bchachar/lip_sync_video_generator.git
cd lip_sync_video_generator
```

### 2. Set Up Python Virtual Environment (Recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> Make sure you have `ffmpeg` installed and accessible via command line.

### 4. Download Required Models

#### a. Clone Wav2Lip Repository

Clone the official Wav2Lip repository into the project root directory:

```bash
git clone https://github.com/Rudrabha/Wav2Lip.git
```

#### b. Wav2Lip Checkpoint (.pth file)

Download the `wav2lip.pth` file from [this Hugging Face link](https://huggingface.co/numz/wav2lip_studio/blob/main/Wav2lip/wav2lip.pth) and place it in `./Wav2Lip/checkpoints/`

---

## ⚙️ How It Works

1. Input text is converted into audio using a TTS system.
2. The audio is saved to `./audio/output.wav`
3. The image and audio are passed to the Wav2Lip model.
4. A video is generated where the lips of the image move in sync with the spoken audio.

---

## 🚀 Usage

### Run the full pipeline:

```bash
python main.py
```

---

## 🐞 Common Issues & Fixes

### 1. `CUDA error: no kernel image is available for execution on the device`

* Your GPU (e.g., RTX 4090) may not be supported by the current PyTorch installation.
* Fix: Reinstall PyTorch with support for compute capability 8.9:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

### 2. `invalid load key, '<'` or TorchScript Errors

* Occurs when the wrong model file is used (e.g., a TorchScript `.pt` file instead of a PyTorch `.pth` checkpoint)
* Fix: Use the `.pth` file from the correct source (e.g., Hugging Face link above)

### 3. `Image too big to run face detection on GPU`

* Fix: Use the `--resize_factor` argument (e.g., 2 or 4)

### 4. Output video not found

* Fix: Ensure `ffmpeg` is installed and accessible from the command line.

---

## 📁 Project Structure

```
.
├── Wav2Lip
│   ├── checkpoints
│   │   └── wav2lip.pth
├── audio
│   └── output.wav
├── images
│   └── sample.jpg
├── video
│   └── result_voice.mp4
├── generate_lipsync_video.py
└── requirements.txt
```

---

## 📜 License

MIT License. See `LICENSE` file for more information.

---

## 🙏 Acknowledgements

* [Wav2Lip (Original Repo)](https://github.com/Rudrabha/Wav2Lip)
* [Hugging Face: wav2lip\_studio](https://huggingface.co/numz/wav2lip_studio)
