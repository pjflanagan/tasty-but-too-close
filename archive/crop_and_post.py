
from moviepy.editor import VideoFileClip, ImageClip
from moviepy.video import fx
from random import randint
from PIL import Image

from config import USERNAME, PASSWORD

import os
from os import listdir
from os.path import isfile, join

from instagram_private_api import Client, ClientCompatPatch
import ssl
# import base64

ssl._create_default_https_context = ssl._create_unverified_context

IN_PATH = "src/data/in/" + "buzzfeedtasty"
all_in_files = [f for f in listdir(IN_PATH) if isfile(join(IN_PATH, f))]

OUT_PATH = "src/data/out/" + "buzzfeedtasty"
all_out_files = [f for f in listdir(OUT_PATH) if isfile(join(OUT_PATH, f))]

MIN_WIDTH = 612


def crop_video(f):
    # select a random x and y to view from
    side = randint(160, 320)
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
    cropped_clip = fx.all.resize(cropped_clip, width=MIN_WIDTH)

    # save as the same name
    out_file_path = join(OUT_PATH, f)
    cropped_clip.write_videofile(
        out_file_path,

        audio_codec='aac',
        codec='mpeg4'
    )


def crop_image(f):
    # select a random x and y to view from
    side = randint(160, 320)
    random_x = randint(0, 640 - side)
    random_y = randint(0, 640 - side)

    # open the thumbnail
    thumb = Image.open(join(IN_PATH, f))
    cropped_thumb = thumb.crop(
        (random_x, random_y, random_x + side, random_y + side))
    new_size = (MIN_WIDTH, MIN_WIDTH)
    cropped_thumb = cropped_thumb.resize(new_size)

    # save the thumbnail
    out_file_path = join(OUT_PATH, f)
    cropped_thumb.save(out_file_path)


def get_caption(name):
    # read the original caption
    caption_file = open(join(IN_PATH, name + ".txt"), "r")
    caption = ""
    for line in caption_file:
        caption += line + "\n"
    return caption


def get_video_data(name):
    video_string = ""
    with open(join(OUT_PATH, name + ".mp4"), "rb") as video_file:
        video_string = video_file.read()
        return video_string


def get_thumb_data(name):
    thumb_string = ""
    with open(join(OUT_PATH, name + ".jpg"), "rb") as thumb_file:
        thumb_string = thumb_file.read()
        return thumb_string


def get_video_duration(name):
    clip = VideoFileClip(join(OUT_PATH, name + ".mp4"))
    return clip.duration


def post(name):
    caption = get_caption(name)
    video_data = get_video_data(name)
    thumb_data = get_thumb_data(name)
    duration = get_video_duration(name)

    # post
    dims = (MIN_WIDTH, MIN_WIDTH)
    api = Client(USERNAME, PASSWORD)
    api.post_video(
        video_data=video_data,
        size=dims,
        duration=duration,
        thumbnail_data=thumb_data,
        caption=caption
    )


if __name__ == "__main__":
    for f in all_in_files:
        split = f.split(".", 1)

        # if the end is mp4 and has not been processed yet
        if len(split) > 1 and split[1] == "mp4" and f not in all_out_files:
            crop_video(f)
            crop_image(split[0] + ".jpg")
            post(split[0])
            break
