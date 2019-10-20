import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')

import webbrowser
import cv2
import pyautogui
import numpy as np
import time
from selenium import webdriver

driver = webdriver.Chrome("/home/debjoy/chromedriver_linux64")
driver.get("https://www.google.com/search?q=play%20snake") 
elem = driver.find_element_by_class_name("XlTvtc")
elem.click()

time.sleep(2)
im0 = pyautogui.screenshot('my_screenshot.png')
img0 =cv2.imread('my_screenshot.png')
img1 = img0[200:725, 420:1000, :]


dict_snake={
	'blue_low':230,
	'blue_high':255,
	'green_low':28,
	'green_high':75,
	'red_low':95,
	'red_high':110
	}


dict_apple={
	'blue_low':0,
	'blue_high':0,
	'green_low':52,
	'green_high':52,
	'red_low':236,
	'red_high':236
	}
	
white_count=1	
red_count=1
x_white=0
y_white=0
x_red=0
y_red=0
for i in range(0,img1.shape[0]):
	for j in range(0,img1.shape[1]):
 	  if(img1[i][j][0]==255 and img1[i][j][1]==255 and img1[i][j][2]==255):
 	  	 x_white=(x_white*white_count+j)/(white_count+1)
 	  	 y_white=(y_white*white_count+i)/(white_count+1)
 	  	 white_count+=1
 	  if(img1[i][j][0]==0 and img1[i][j][1]==52 and img1[i][j][2]==236):
 	  	 x_red=(x_red*red_count+j)/(red_count+1)
 	  	 y_red=(y_red*red_count+i)/(red_count+1)
 	  	 red_count+=1

snake_mat=np.zeros((15,17),dtype='int')  

apple_col = int((x_red-11)/32)
apple_row = int((y_red-26)/32)
snake_mat[apple_row][apple_col] = 2

for m in range(15):
	for n in range(17):
		i=m*32+16+26
		j=n*32+11+16
		if(img1[i][j][0]<dict_snake["blue_high"] and img1[i][j][0]>dict_snake["blue_low"] and img1[i][j][1]<dict_snake["green_high"] and img1[i][j][1]>dict_snake["green_low"] and img1[i][j][2]<dict_snake["red_high"] and img1[i][j][2]>dict_snake["red_low"]):
			snake_mat[m][n] = 1


eye_col = int((x_white-11)/32)
eye_row = int((y_white-26)/32)
snake_mat[eye_row][eye_col] = 5

print(snake_mat)

#for pix in img1:
#	for pix1 in pix:
#		if pix1[0] != 78:
#			pix1[0] = 0
#			pix1[1] = 0
#			pix1[2] = 0


cv2.circle(img1,(int(x_white),int(y_white)), 16, (0,0,255), -1)
cv2.circle(img1,(int(x_red),int(y_red)), 16, (0,255,255), -1)

cv2.imshow("win.jpg", img1)
cv2.waitKey(0)

