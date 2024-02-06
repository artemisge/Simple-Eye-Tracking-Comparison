import cv2
from matplotlib import pyplot as plt
import numpy as np

# Arrays to store selected x-coordinates
coordinates_1 = []
coordinates_2 = []
coordinates_1y = []
coordinates_2y = []
time_1 = []
time_2 = []

def click_event1(event, x, y, flags, params): 
    if event == cv2.EVENT_LBUTTONDOWN: 
        coordinates_1.append(x)
        coordinates_1y.append(y)
        print(x, ' ', y) 

def click_event2(event, x, y, flags, params): 
    if event == cv2.EVENT_LBUTTONDOWN: 
        coordinates_2.append(x)
        coordinates_2y.append(y)
        print(x, ' ', y) 

# Open the first video
video_path_1 = 'smooth_persuit (online-video-cutter.com).mp4'
cap_1 = cv2.VideoCapture(video_path_1)

# Open the second video
video_path_2 = 'reading (online-video-cutter.com).mp4'
cap_2 = cv2.VideoCapture(video_path_2)

# Create windows for displaying videos
cv2.namedWindow('Video 1')
cv2.namedWindow('Video 2')

# Set mouse callback function
cv2.setMouseCallback('Video 1', click_event1)
cv2.setMouseCallback('Video 2', click_event2)

# Variables for timing
frames_passed = 0

while True:
    # Read frames from the videos
    ret_1, frame_1 = cap_1.read()
    ret_2, frame_2 = cap_2.read()
    
    # Break the loop if any of the videos end
    if not ret_1 and not ret_2:
        break

    if frames_passed % 10 == 0:
        if ret_1:
            frame_1 = cv2.resize(frame_1, (1000, 700))
            cv2.imshow('Video 1', frame_1)
            time_1.append(cap_1.get(cv2.CAP_PROP_POS_MSEC))
       
        if ret_2:
            frame_2 = cv2.resize(frame_2, (1000, 700))
            cv2.imshow('Video 2', frame_2)
            time_2.append(cap_2.get(cv2.CAP_PROP_POS_MSEC))

        cv2.waitKey(0)

    frames_passed += 1

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture objects
cap_1.release()
cap_2.release()

# Destroy all OpenCV windows
cv2.destroyAllWindows()

# Print and save the selected coordinates
coordinates_1 = np.array(coordinates_1)
coordinates_2 = np.array(coordinates_2)
coordinates_1y = np.array(coordinates_1y)
coordinates_2y = np.array(coordinates_2y)

time_1 = np.array(time_1)
time_2 = np.array(time_2)

print("Selected coordinates for Video 1:", coordinates_1)
print("Selected coordinates for Video 2:", coordinates_2)

# Save the coordinates as numpy arrays
np.save('coordinates_1.npy', coordinates_1)
np.save('coordinates_2.npy', coordinates_2)
np.save('coordinates_1y.npy', coordinates_1y)
np.save('coordinates_2y.npy', coordinates_2y)
np.save('time_1.npy', time_1)
np.save('time_2.npy', time_2)