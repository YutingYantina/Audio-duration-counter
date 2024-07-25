import os
from pydub import AudioSegment

# 音频文件目录，如果是手动上传，使用当前目录
audio_dir = '/content'  # 或 '/content/drive/My Drive/your_audio_folder'

# 获取目录中的所有 mp3 文件
audio_files = [f for f in os.listdir(audio_dir) if f.endswith('.mp3')]

# 设置视频的帧率
fps = 30

# 保存音频文件时长和帧数的列表
audio_durations = []

for audio_file in audio_files:
    audio_path = os.path.join(audio_dir, audio_file)
    audio = AudioSegment.from_file(audio_path)
    duration_ms = len(audio)  
    duration_frames = int((duration_ms / 1000) * fps)  
    audio_durations.append((audio_file, duration_frames))

# 输出音频文件的帧数
for audio_file, duration_frames in audio_durations:
    print(f'Audio file: {audio_file}, Frames: {duration_frames}')
    