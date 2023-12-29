import os
import sys
import argparse
import subprocess
from PIL import Image
import numpy as np
from datetime import datetime

def extract_frames(video, rate, start_time=None, duration=None):
    base_name = os.path.splitext(os.path.basename(video))[0]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    frame_dir = f'frames_{base_name}_{timestamp}'

    if not os.path.exists(frame_dir):
        os.makedirs(frame_dir)

    cmd = ['ffmpeg']
    if start_time:
        cmd.extend(['-ss', str(start_time)])
    if duration:
        cmd.extend(['-t', str(duration)])
    cmd.extend([
        '-i', video,
        '-vf', f'fps={rate}',
        os.path.join(frame_dir, 'frame_%04d.png')
    ])
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return frame_dir

def apply_flash_effect(frame_files, flash_mode):
    if flash_mode == 'front':
        flash_frame = Image.open(frame_files[0])
        flash_frame = flash_frame.point(lambda p: min(255, int(p * 1.5)))
        return flash_frame
    elif flash_mode == 'rear':
        flash_frame = Image.open(frame_files[-1])
        flash_frame = flash_frame.point(lambda p: min(255, int(p * 1.5)))
        return flash_frame
    return None

def create_long_exposure(frame_files, flash_mode=None):
    stack = np.zeros((Image.open(frame_files[0]).size[1], Image.open(frame_files[0]).size[0], 3), np.float32)
    for frame in frame_files:
        frame_data = np.array(Image.open(frame), dtype=np.float32)
        stack += frame_data / len(frame_files)
    stack = np.array(np.round(stack), dtype=np.uint8)
    final_image = Image.fromarray(stack, mode='RGB')

    if flash_mode in ['front', 'rear']:
        flash_frame = apply_flash_effect(frame_files, flash_mode)
        if flash_frame:
            final_image = Image.blend(final_image, flash_frame, alpha=0.3)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    final_output = f'long_exposure_{os.path.basename(frame_files[0])[:-8]}_{timestamp}.png'
    final_image.save(final_output)
    return final_output

parser = argparse.ArgumentParser(description="Create a long exposure effect from a video.")
parser.add_argument("video_file", help="Path to the video file.")
parser.add_argument("--flash-mode", type=str, choices=['front', 'rear'], default=None, help="Apply 'front' or 'rear' curtain flash effect.")
parser.add_argument("--keep-frames", action="store_true", help="Keep the extracted frames.")
parser.add_argument("--frame-rate", type=float, default=1, help="Frame rate for frame extraction (default: 1 frame per second).")
parser.add_argument("--start-time", type=float, default=None, help="Start time for frame extraction in seconds.")
parser.add_argument("--duration", type=float, default=None, help="Duration for frame extraction in seconds.")

args = parser.parse_args()

frame_dir = extract_frames(args.video_file, args.frame_rate, args.start_time, args.duration)
frame_files = sorted([os.path.join(frame_dir, f) for f in os.listdir(frame_dir) if f.endswith('.png')])

final_output_path = create_long_exposure(frame_files, args.flash_mode)
print(f"Long exposure image saved to {final_output_path}")

if not args.keep_frames:
    subprocess.run(['rm', '-rf', frame_dir])

