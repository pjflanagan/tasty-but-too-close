
import os
from os import listdir
from os.path import isfile, join
from .config import LOG_PATH

# open the cropped log and read it into an array
log_file = open(join(LOG_PATH, "cropped.txt"), "r")
cropped = []
for line in log_file:
    cropped.append(line)
log_file.close()


def log(f):
    # log
    log_file = open(join(LOG_PATH, "cropped.txt"), "a")
    log_file.write(f + "\n")
    log_file.close()
