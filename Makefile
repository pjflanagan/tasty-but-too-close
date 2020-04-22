

default: reset

reset:
	reset

# download: # https://github.com/instaloader/instaloader
# 	instaloader --fast-update profile buzzfeedtasty

clean:
	python3 src/clean.py

crop:
	open ./src/data/out/buzzfeedtasty
	python3 src/crop.py

skip:
	python3 src/skip.py

redo:
	python3 src/redo.py
