import os
import cv2

path = "Images"
Images = []
for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    if ext.lower() in ['.jpg', '.jpeg', '.png']:
        file_name = os.path.join(path, file)
        print(file_name)
        Images.append(file_name)
count = len(Images)
frame = cv2.imread(Images[0])
height, width, channels = frame.shape
size = (width, height)
print(size)
out = cv2.VideoWriter(
    "Project.avi", cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)
for i in range(count):
    image = cv2.imread(Images[i])
    out.write(image)
print("Done")