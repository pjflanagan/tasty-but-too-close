
from moviepy.editor import VideoFileClip, ImageClip
from moviepy.video import fx
from random import randint
import os
from os import listdir
from os.path import isfile, join
from .caption import get_hashtags
from .config import IN_PATH, OUT_PATH
from .log import cropped


# read all the in files
all_in_files = [f for f in listdir(IN_PATH) if isfile(join(IN_PATH, f))]


def isCroppable(split, f):
    # TODO: if the file is in skipped return false
    # TODO: if the file is over a minute long add it to skipped and return false
    return (
        len(split) > 1 and
        split[1] == "mp4" and
        (f + "\n") not in cropped and
        VideoFileClip(join(IN_PATH, f)).duration <= 60
    )


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
