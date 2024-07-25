# 定义音频文件的帧数
audio_frames = {
    'TitleAudio': 47,
    'Speech1': 422,
    'Speech2': 300,
    'Speech3': 222,
    'Speech4': 249,
    'Speech5': 379,
    'Speech6': 316,
    'Speech7': 275,
    'Speech8': 221,
}

# 定义停顿时间
pause_frames = 0

# 初始化开始帧
start_frame = 0

# 计算每个音频文件的时间区间
audio_intervals = {}

for audio, frames in audio_frames.items():
    end_frame = start_frame + frames
    audio_intervals[audio] = (start_frame, end_frame)
    # 更新开始帧，包括音频的帧数和停顿时间
    start_frame = end_frame + pause_frames

# 输出每个音频文件的时间区间
for audio, (start, end) in audio_intervals.items():
    print(f'Audio file: {audio}, Start frame: {start}, End frame: {end}')