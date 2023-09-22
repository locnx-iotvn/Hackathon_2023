import cv2
import os

input_folder = "data/raw_01"
output_folder = "data/data_01"

files = sorted(os.listdir(input_folder))
for i, file in enumerate(files):
    img = cv2.imread(os.path.join(input_folder, file))
    if img is None:
        print("Error reading image {}".format(file))
        continue
    new_name = "{:04d}.jpg".format(i)
    cv2.imwrite(os.path.join(output_folder, new_name), img)
