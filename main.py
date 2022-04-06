# HW1 wet exercise anat

# imports for hw1
import numpy as np
import matplotlib.pyplot as plt
import cv2


def video_to_frames(vid_path: str, start_second, end_second):
    """
    Load a video and return its frames from the wanted time range.
    :param vid_path: video file path.
    :param start_second: time of first frame to be taken from the
    video in seconds.
    :param end_second: time of last frame to be taken from the
    video in seconds.
    :return:
    frame_set: a 4D uint8 np array of size [num_of_frames x H x W x C]
    containing the wanted video frames.
    """
    video_capture = cv2.VideoCapture(vid_path)
    if not video_capture.isOpened():
        print("Error opening the video file")

    else:
        fps = video_capture.get(cv2.CAP_PROP_FPS)
        h = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        w = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        first_frame = fps*start_second
        last_frame = fps*end_second
        frame_num = last_frame-first_frame
        frame_set = np.empty((frame_num, h, w, 3), np.dtype('unit8'))
        i, j, ret = 0, 0, True
        print("frame_set shape is: ", frame_set.shape)

        # emptying the frames starting frames that aren't needed
        while j < (first_frame - 1):
            video_capture.read()

        # extracting video frames
        while i < last_frame-first_frame and ret:
            ret, cur_frame = video_capture.read()
            if not ret:
                print("Error: cannot receive next frame")
                break
            frame_set[i] = cur_frame
            i += 1

    return frame_set


def main():
    song_path = r'C:\Users\tmassas\Desktop\semster 6\anat\wet_1\given_data\MilkyChance_StolenDance.mp4'
    print("2")
    return 0


