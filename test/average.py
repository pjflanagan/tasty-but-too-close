from moviepy.editor import VideoFileClip, ImageClip
clip = VideoFileClip("buzzfeedtasty/2020-03-03_23-11-13_UTC.mp4")
fps= 1.0 # take one frame per second
nframes = clip.duration*fps # total number of frames used
total_image = sum(clip.iter_frames(fps,dtype=float,logger='bar'))
average_image = ImageClip(total_image/ nframes)
average_image.save_frame("average.png")
