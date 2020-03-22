
import os
from os import listdir
from os.path import isfile, join

# this cleans up the download folder from any files that aren't mp4's or
# thier caption.txt's, and then records them all in the log

path = "src/data/in/" + "buzzfeedtasty"

all_files = [f for f in listdir(path) if isfile(join(path, f))]

all_mp4_names = []
for f in all_files:
    sep = "."
    split = f.split(sep, 1)
    if len(split) > 1 and split[1] == "mp4":  # if the end is mp4
        all_mp4_names.append(split[0])  # store the front in the name

print("count of mp4s: " + str(len(all_mp4_names)))

for f in all_files:
    sep = "."
    split = f.split(sep, 1)
    if len(split) > 1:
        if split[1] not in ["txt", "mp4"]:
            # if it isn't a txt or mp4 file, delete it
            print("deleted: " + f)
            os.remove(join(path, f))
        elif split[0] not in all_mp4_names:
            # if it isn't associated with a video that is an mp4, delete it
            print("deleted: " + f)
            os.remove(join(path, f))
