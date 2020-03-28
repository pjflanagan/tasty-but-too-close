
from instapy_cli import client
from config import USERNAME, PASSWORD
import ssl

import os
from os import listdir
from os.path import isfile, join

# import imageio

# posts one random one
# goes through the list of out files
# if the out file has not been posted yet, select it
# find the original caption in the in folder
# log that this was posted in the log.txt

ssl._create_default_https_context = ssl._create_unverified_context
# imageio.plugins.ffmpeg.download()

in_path = "src/data/in/" + "buzzfeedtasty"
all_in_files = [f for f in listdir(in_path) if isfile(join(in_path, f))]

out_path = "src/data/out/" + "buzzfeedtasty"
all_out_files = [f for f in listdir(out_path) if isfile(join(out_path, f))]

# open the posted log and read it into an array
log_path = "src/log/" + "buzzfeedtasty"
log_file = open(join(log_path, "posted.txt"), "r")
posted = []
for line in log_file:
    posted.append(line)
log_file.close()

for f in all_out_files:

    split = f.split(".", 1)

    # if this file is not in the array
    if (f + "\n") not in posted:

        print(split)

        # read the original caption
        caption_file = open(join(in_path, split[0] + ".txt"), "r")
        caption = ""
        for line in caption_file:
            caption += line + "\n"

        # post
        with client(USERNAME, PASSWORD) as cli:
            cli.upload(join(out_path, f), caption)
        # print("instapy -u " + USERNAME + " -p " + PASSWORD +
        #       " -f " + join(out_path, f) + " -t '" + caption + "'")

        # log
        log_file = open(join(log_path, "posted.txt"), "a")
        log_file.write(f + "\n")
        log_file.close()
        break
