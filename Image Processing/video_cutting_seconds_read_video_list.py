from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import cv2
import argparse
import os

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('--video_path_list', required=True, \
		help='video path list (txt file), format: video_path \t start_seconds \t end_seconds \t save_path')
	
	args = parser.parse_args()

	return args

def mrlines(fname, sp='\n'):
    f = open(fname).read().split(sp)
    while f != [] and f[-1] == '':
        f = f[:-1]
    return f
	
args = parse_args()
 
lines = mrlines(args.video_path_list)
lines = [x.split('\t') for x in lines]

for vid, line in enumerate(lines):
	video_path = line[0]
	start_seconds = int(line[1])
	end_seconds = int(line[2])
	save_path = line[3]
	
	print()
	print(f' ==> {vid}')
	print(f'video_path: {video_path}')
	print(f'start_seconds: {start_seconds}, end_seconds: {end_seconds}')
	print(f'save_path: {save_path}')

	video = cv2.VideoCapture(video_path)

	# ffmpeg_extract_subclip(video_path, start_seconds, end_seconds, save_path)
	ffmpeg_extract_subclip(video_path, start_seconds, end_seconds, targetname=save_path)
