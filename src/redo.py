
from main import *

if __name__ == "__main__":
    f = cropped[len(cropped) - 1].strip()
    split = f.split(".", 1)
    crop_video(f)
    print(get_caption(split[0]))
