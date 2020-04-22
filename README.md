
Setps:

- 1. Download the vidoes (will automatically skip ones that are present) `instaloader --fast-update buzzfeedtasty`
- 2. Optional: Clean up the download folder `make clean`
- 3. Crop the video, if you don't like it, delete the last line in `cropped.txt` and redo the video `make crop`
- 4. Copy the caption text, airdrop to yourself, post on insta using phone
- 5. Or if this video is weird and not good then paste the name in `skipped.txt` for refrence


# TODO: 
- [ ] only process videos that are a minute long or less, if they are too long, add them to skipped
- [x] renmae posted to cropped, not all that are cropped are posted
- [ ] make a skip command (skip the video that was made last)
- [x] make a redo command (redo the video that was made last)
