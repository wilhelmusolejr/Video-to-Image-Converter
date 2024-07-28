import cv2
import numpy as np
import os
import random

os.system('cls' if os.name == 'nt' else 'clear')
save_path = "image"
list_videos = os.listdir("video")

numbers = []
total = 0

if list_videos:
    for video in list_videos:
        running_count = 0

        print("\n----------------------------")
        print(f"Processing video: {video}")
        
        random_number = random.randint(1, 100)
        
        file_path = os.path.join("video", video)
        file_base_name = os.path.splitext(os.path.basename(file_path))[0]
        directory_path = os.path.join(save_path, file_base_name)
        
        try:
            os.makedirs(directory_path, exist_ok=True)
        except Exception as e:
            print(f"Error creating directory '{directory_path}': {e}")
        
        cap = cv2.VideoCapture(file_path)
        count = 1
            
        while cap.isOpened():
            ret, frame = cap.read()
            count += 1
            
            if ret:
                if count % 30 == 0:
                    new_image = os.path.join(directory_path, f"{running_count}_{random_number}.jpg")
                    cv2.imwrite(new_image, frame)
                    running_count += 1
            else:
                cap.release()
        
        numbers.append(running_count)
        print(f"{running_count} images generated for this video.")
else:
    print("No videos were detected. Please place videos in the 'video' folder.")

total = sum(numbers)
print("\n============================")
print(f"Total images generated from all videos: {total}")
print("============================")
