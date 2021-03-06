

default:
	reset
	make crop

# https://github.com/instaloader/instaloader
download: 
	instaloader --no-profile-pic --no-pictures --dirname-pattern ./src/data/in/{profile} buzzfeedtasty

clean:
	python3 src/commands/clean.py

crop:
	open ./src/data/out/buzzfeedtasty
	python3 src/commands/crop.py

skip:
	python3 src/commands/skip.py

redo:
	python3 src/commands/redo.py
