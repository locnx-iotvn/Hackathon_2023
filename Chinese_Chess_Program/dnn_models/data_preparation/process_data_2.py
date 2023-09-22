import cv2
import os

input_folder = "data/raw_01"
output_folder = "data/data_01"

file_list_file = "sss.txt"
files = []
with open(file_list_file, "r") as f:
    for line in f:
        files.append(line.strip())

files = sorted(files)
for i, file in enumerate(files):
    img = cv2.imread(file)
    if img is None:
        print("Error reading image {}".format(file))
        continue
    new_name = "{:04d}.jpg".format(i + 560)
    cv2.imwrite(os.path.join(output_folder, new_name), img)
