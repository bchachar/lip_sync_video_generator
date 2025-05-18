from TTS.api import TTS
import subprocess
import os

# ---- 1. Generate Audio with Coqui TTS ----

# Load a pre-trained TTS model (multi-speaker, English)
model_name = "tts_models/en/ljspeech/tacotron2-DDC"
tts = TTS(model_name)

# Input text
text = "Welcome to the future of generative Artificial Intelligence. Today, you will see how machines can talk, learn, and think creatively."
audio_path = "./audio/output.wav"
image_path = "./images/Liz.png"
checkpoint_path = "./Wav2Lip/checkpoints/wav2lip.pth"
output_video_path = "./results/result_voice.mp4"

# Convert to audio and save
tts.tts_to_file(text=text, file_path=audio_path)
print(f"✅ Audio saved to {audio_path}")

# ---- 2. Run Wav2Lip ----


# Construct command
command = [
    "python", "Wav2Lip/inference.py",
    "--checkpoint_path", checkpoint_path,
    "--face", image_path,
    "--audio", audio_path,
    # "--resize_factor", "2",
]

try:
    subprocess.run(command, check=True)
    print(f"✅ Wav2Lip video saved to {output_video_path}")
except subprocess.CalledProcessError as e:
    print(f"❌ Error running Wav2Lip: {e}")

