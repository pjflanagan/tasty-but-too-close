from random import sample
import subprocess
from .config import IN_PATH
from os.path import join


HASHTAGS = [
    'tasty',
    'tooclose',
    'delicious',
    'recipe',
    'food',
    'yum',
    'yummy',
    'ohyes',
    'buzzfeedtasty',
    'meal',
    'cooking',
    'cook',
    'learntocook',
    'howto',
    'diy',
    'eat',
    'eating'
    'goodeats',
    'zoomed',
    'zoom',
    'zoomin',
    'tastybuttooclose',
    'makefood',
    'kitchen',
    'wholesome',
    'scrumptious',
    'appetizing',
    'delectable',
    'savory',
    'tantalizing'
]


def get_hashtags():
    # get 20 from the list of hashtags with # added to the front and join them into a string
    return '.\n.\n.\n' + ' '.join(sample(['#' + tag for tag in HASHTAGS], 20))


def get_caption(name):
    # read the first line of the original caption and add the hashtags
    caption_file = open(join(IN_PATH, name + '.txt'), 'r')
    caption = ''
    for line in caption_file:
        caption += line
        break
    return caption + get_hashtags()


def copy(s):
    subprocess.run('pbcopy', universal_newlines=True, input=s)
