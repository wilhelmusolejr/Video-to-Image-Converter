import cv2
import numpy as np
import os
import random

os.system('cls')

save_path = "images"

list_denom = os.listdir("video")
running_count = 1

for denom in list_denom:
  list_videos = os.listdir("video/" + str(denom))
  
  print("--------")
  print("Current denom: P" + str(denom))
  print("with " + str(len(list_videos)) + " videos")
  
  for video in list_videos:
    
    print("generating " + str(video))
    
    random_number = random.randint(1,100)
  
    path = "video/" + str(denom) + "/" + video
    cap = cv2.VideoCapture(path)
    count = 1
    
    while(cap.isOpened()):
      ret, frame = cap.read()
      count = count + 1
      
      if ret == True:
        if(count%30 ==0):
          cv2.imwrite(save_path + "/" +str(denom) + "/images/"+str(running_count)+"_"+str(random_number)+".jpg", frame)
          running_count = running_count + 1
      else:
          cap.release() 