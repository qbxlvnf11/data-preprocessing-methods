from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import cv2
import argparse
import os

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('--video_path', help='input video path', required=True)
	parser.add_argument('--save_path', help='video save path', required=True)
	parser.add_argument('--start_seconds', help='start seconds', type=int, required=True)
	parser.add_argument('--end_seconds', help='end seconds', type=int, required=True)
	
	args = parser.parse_args()

	return args

args = parse_args()
  
# path
video_path = args.video_path
save_path = args.save_path

# Cut seconds
start_seconds = args.start_seconds
end_seconds = args.end_seconds

video = cv2.VideoCapture(video_path)

# ffmpeg_extract_subclip(video_path, start_seconds, end_seconds, save_path)
ffmpeg_extract_subclip(video_path, start_seconds, end_seconds, targetname=save_path)
