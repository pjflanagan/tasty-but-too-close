
from tools import *


if __name__ == "__main__":
    for f in all_in_files:
        split = f.split(".", 1)
        # if the end is mp4 and has not been processed yet

        if isCroppable(split, f):
            # video
            crop_video(f)

            # caption
            caption = get_caption(split[0])
            copy(caption)
            print('COPIED:\n' + caption + '\n')

            # log
            log(f)

            break
