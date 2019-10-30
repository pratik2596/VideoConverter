"""Video Converter

This python scripts allows the user to convert all the videos in a given path
into other extension. The user can also set the output resolution, bitrate and
framerate. It is also possible to trim the video.

All these parameters have to be defined below in this script.

FFmpeg must be installed in your computer before running this script.
FFmpeg can be downloaded from https://www.ffmpeg.org/download.html

For more information check out FFmpeg documentation at
https://www.ffmpeg.org/ffmpeg-all.html
"""

import os
import psutil
import time

# -- PARAMETERS --
# PATH: The path where your folders are stored
PATH = "path/to/your/videos"
# INPUT_EXT: Input video extension
INPUT_EXT = 'mp4'
# OUTPUT_EXT: Output video extension
OUTPUT_EXT = 'mp4'
# BITRATE: Output video bitrate in kb/s
BITRATE = '4000'
# FRAMERATE: Output video framerate (fps)
FRAMERATE = '60'
# OUTPUT_RES: Output video resolution. More info at
# https://www.ffmpeg.org/ffmpeg-all.html#toc-Video-size
OUTPUT_RES = 'hd720'
# START: Starting time if you want to trim the video ('hh:mm:ss')
START = '00:00:00'
# END: Ending time if you want to trim the video ('hh:mm:ss').
# Set it to None if you do not want to trim the video
END = None

try:
    os.mkdir(os.path.join(PATH, 'Converted'))
except OSError:
    pass


def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains
    the given name processName.
    '''
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except(psutil.NoSuchProcess, psutil.AccessDenied,
                psutil.ZombieProcess):
            pass
    return False


def main():
    exclude = set(['Converted'])
    for root, dirs, files in os.walk(PATH, topdown=True):
        dirs[:] = [d for d in dirs if d not in exclude]
        for fname in files:
            if fname.lower().endswith(INPUT_EXT):
                print("Converting ", fname)
                while checkIfProcessRunning('ffmpeg') is True:
                    time.sleep(5)
                else:
                    os.chdir(PATH)
                    if END is None:
                        os.system('ffmpeg -i "{}" -r {} -s {} -b:v {}k \
                                  "{}.{}"'.format(fname, FRAMERATE, OUTPUT_RES,
                                  BITRATE, '.\Converted\{}'.format(
                                      fname.split('.')[0]), OUTPUT_EXT))
                    else:
                        os.system('ffmpeg -i "{}" -r {} -s {} -ss {} -to {} \
                                  -b:v {}k "{}.{}"'.format(fname, FRAMERATE,
                                  OUTPUT_RES, START, END, BITRATE,
                                  '.\Converted\{}'.format(fname.split('.')[0]),
                                  OUTPUT_EXT))


if __name__ == '__main__':
    main()
