
# Long Exposure Video Effect

## Overview
This script creates a long exposure effect from a video file. It can simulate 'Front Curtain Flash' or 'Rear Curtain Flash' effects and allows the user to specify the start time and duration for frame extraction. The script is written in Python and uses `ffmpeg` for frame extraction and `PIL` for image processing.

## Installation
To use this script, you need to have Python installed on your system along with the `ffmpeg` and `PIL` (Python Imaging Library) packages.

1. Install Python (if not already installed): Visit [Python's official website](https://www.python.org/downloads/) for installation instructions.
2. Install `ffmpeg`: Follow the instructions on [FFmpeg's official website](https://ffmpeg.org/download.html).
3. Install PIL:
   ```bash
   pip install pillow
   ```

## Usage
To use the script, run it with the required arguments:

```bash
python long_exposure.py <path_to_video> [--flash-mode {front,rear}] [--keep-frames] [--frame-rate FRAME_RATE] [--start-time START_TIME] [--duration DURATION]
```

### Arguments
- `<path_to_video>`: Path to the video file.
- `--flash-mode {front,rear}`: Apply 'front' or 'rear' curtain flash effect (optional).
- `--keep-frames`: Keep the extracted frames (optional).
- `--frame-rate FRAME_RATE`: Frame rate for frame extraction, default is 1 frame per second (optional).
- `--start-time START_TIME`: Start time for frame extraction in seconds (optional).
- `--duration DURATION`: Duration for frame extraction in seconds (optional).

### Example
```bash
python long_exposure.py /path/to/video.mp4 --flash-mode front --start-time 10 --duration 5
```

This command will create a long exposure effect from the video, starting at 10 seconds into the video and lasting for 5 seconds, with a front curtain flash effect.

### Output Examples
After running the script, you will find the output images named in the format similar to the following examples:

![alt text](https://github.com/iveskins/photo_utils_longexposure_from_video/blob/main/long_exposure_frame__20231229_121036.png?raw=true)
![alt text](https://github.com/iveskins/photo_utils_longexposure_from_video/blob/main/long_exposure_frame__20231229_121237.png?raw=true)
![alt text](https://github.com/iveskins/photo_utils_longexposure_from_video/blob/main/long_exposure_frame__20231229_121222.png?raw=true)
![alt text](https://github.com/iveskins/photo_utils_longexposure_from_video/blob/main/long_exposure_frame__20231229_121202.png?raw=true)

These files are timestamped to ensure unique naming and easy identification.

## License
[MIT](https://opensource.org/licenses/MIT)

