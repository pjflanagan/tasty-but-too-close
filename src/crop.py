
from main import *


def isCroppable(split, f):
    # TODO: if the file is in skipped return false
    # TODO: if the file is over a minute long add it to skipped and return false
    return (
        len(split) > 1 and
        split[1] == "mp4" and
        (f + "\n") not in cropped and
        VideoFileClip(join(IN_PATH, f)).duration <= 60
    )


if __name__ == "__main__":
    for f in all_in_files:
        split = f.split(".", 1)
        # if the end is mp4 and has not been processed yet
        if isCroppable(split, f):
            crop_video(f)
            print(get_caption(split[0]))
            log(f)
            break
