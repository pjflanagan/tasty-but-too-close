# open the posted log and read it into an array
log_path = "src/log/" + "buzzfeedtasty"
log_file = open(join(log_path, "posted.txt"), "r")
posted = []
for line in log_file:
    posted.append(line)
log_file.close()

# log
log_file = open(join(log_path, "posted.txt"), "a")
log_file.write(f + "\n")
log_file.close()
