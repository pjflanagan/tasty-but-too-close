

default: reset

reset:
	reset

# download: # https://github.com/instaloader/instaloader
# 	instaloader --fast-update profile buzzfeedtasty

clean:
	python3 src/clean.py

# TODO:
# skip:
	# add the last file to skipped.txt

# TODO:
# redo:
	# delete the last one 
	# crop

crop:
	open ./src/data/out/buzzfeedtasty
	python3 src/crop.py

# post:
# 	python3 src/post.py