

default: reset

reset:
	reset

# download: # https://github.com/instaloader/instaloader
# 	instaloader --fast-update profile buzzfeedtasty

clean:
	python3 src/clean.py

crop:
	python3 src/crop.py