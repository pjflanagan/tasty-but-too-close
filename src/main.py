
from moviepy.editor import VideoFileClip, ImageClip
from moviepy.video import fx
from random import randint
import os
from os import listdir
from os.path import isfile, join

IN_PATH = "src/data/in/" + "buzzfeedtasty"
OUT_PATH = "src/data/out/" + "buzzfeedtasty"
LOG_PATH = "src/log/" + "buzzfeedtasty"

# read all the in files
all_in_files = [f for f in listdir(IN_PATH) if isfile(join(IN_PATH, f))]

# open the cropped log and read it into an array
log_file = open(join(LOG_PATH, "cropped.txt"), "r")
cropped = []
for line in log_file:
    cropped.append(line)
log_file.close()


def crop_video(f):
    # select a random x and y to view from
    side = randint(160, 260)
    random_x = randint(0, 640 - side)
    random_y = randint(0, 640 - side)

    # create a new clip from it
    clip = VideoFileClip(join(IN_PATH, f))

    # crop the clip to that size
    cropped_clip = fx.all.crop(
        clip,
        x1=random_x,
        y1=random_y,
        x2=random_x+side,
        y2=random_y+side
    )
    cropped_clip = cropped_clip.resize(width=640, height=640)

    # save as the same name
    out_file_path = join(OUT_PATH, f)
    cropped_clip.write_videofile(
        out_file_path,
        audio_codec='aac',
        codec='libx264'  # 'mpeg4'
    )


def get_caption(name):
    # read the original caption
    caption_file = open(join(IN_PATH, name + ".txt"), "r")
    caption = ""
    for line in caption_file:
        caption += line + "\n"
    return caption


def log(f):
    # log
    log_file = open(join(LOG_PATH, "cropped.txt"), "a")
    log_file.write(f + "\n")
    log_file.close()
