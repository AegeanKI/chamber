import cv2
import os
import gdown

def download_video(download_path="data/"):
    """
        download the calibration video
    """
    if os.path.exists("data/calibration.mp4"):
        print("calibration video already exists")
        return
    url = "https://drive.google.com/uc?id=1A884ErnhJZRgZMrbvH0dRS2FRX-WSyCm"
    output_path = os.path.join(download_path, "calibration.mp4")
    gdown.download(url, output_path, quiet=False)


def take_screen_shots(video_path="data/calibration.mp4", 
                      output_path="data/calibration_images", 
                      interval=1, 
                      start_second=0, 
                      end_second=30):
    """
        read video from file, take snapshot every interval seconds, and save as image
        in the same directory as the video
    """
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    else: 
        # clear the directory
        for file in os.listdir(output_path):
            file_path = os.path.join(output_path, file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(e)
                
    video = cv2.VideoCapture(video_path)
    frame_per_second = video.get(cv2.CAP_PROP_FPS) 
    current_frame = 0
    while True:
        ret, frame = video.read()
        current_seconds = current_frame / frame_per_second
        if not ret or current_seconds > end_second:
            break
        else:
            if current_seconds % interval == 0 and current_seconds > start_second:
                cv2.imwrite(os.path.join(output_path, "calibration_frame_{}.jpg".format(current_frame)), frame)
            current_frame += 1

        

if __name__ == "__main__":
    take_screen_shots()