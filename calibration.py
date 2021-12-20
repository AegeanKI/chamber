import numpy as np
import cv2 as cv
import glob
import tqdm
from screenshot import take_screen_shots

# take screen shots from video and save as images
print("taking screen shots from video...")
take_screen_shots(video_path="data/calibration.mp4",
                  output_path="data/calibration_images",
                  interval=1,
                  start_second=0,
                  end_second=30)


# find chessboard corners
# The dimension of chessboard is 10x7
print("generateing chessboard images coordinates...")
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001) # termination criteria
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((7*10,3), np.float32)
objp[:,:2] = np.mgrid[0:10,0:7].T.reshape(-1,2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
images = glob.glob('data/calibration_images/*.jpg')
for fname in tqdm.tqdm(images):
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (10,7), None)
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners)
        # Draw and display the corners
        cv.drawChessboardCorners(img, (10,7), corners2, ret)

# calibrate camera
print("calibrating camera...")
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
# print camera matrix
print("Camera Intrinsic Matrix: ") 
print(mtx)