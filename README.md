# Video Converter

A python video converter based on FFmpeg

## 1. Description

This python script allows the user to convert all the videos in a given path into other extension. The user can also set the output resolution, bitrate and framerate. It is also possible to trim the video.

All these parameters have to be defined in `VideoConverter.py` file in the `PARAMETERS` section.

The converted videos will be stored in a folder named `Converted` in the `PATH` where your input videos are stored. The program will convert recursively all the videos in this `PATH`.

## 2. Requirements

FFmpeg must be installed in your computer before running this script.
FFmpeg can be downloaded from https://www.ffmpeg.org/download.html

For more information check out FFmpeg documentation at
https://www.ffmpeg.org/ffmpeg-all.html
 
## 3. Parameters

* **PATH**: The path where your folders are stored
* **INPUT_EXT**: Input video extension
* **OUTPUT_EXT**: Output video extension
* **BITRATE**: Output video bitrate in kb/s
* **FRAMERATE**: Output video framerate (fps)
* **OUTPUT_RES**: Output video resolution ('hd480', 'hd720', 'hd1080', '2k'...). More info at https://www.ffmpeg.org/ffmpeg-all.html#toc-Video-size
* **START**: Starting time if you want to trim the video ('hh:mm:ss')
* **END**: Ending time if you want to trim the video ('hh:mm:ss'). Set it to None if you do not want to trim the video
