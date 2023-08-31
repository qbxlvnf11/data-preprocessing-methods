from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import cv2
import argparse
import os
import shutil

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('--video_path_list', required=True, \
		help='video path list (txt file), format: video_path \t start_seconds \t end_seconds \t save_folder_path \t save_video_name')
	
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

new_folder_path = set()
for vid, line in enumerate(lines):
	video_path = line[0]
	start_seconds = float(line[1])
	end_seconds = float(line[2])
	save_folder_path = line[3]
	save_video_name = line[4]
	
	print()
	print(f' ==> {vid}')
	print(f'video_path: {video_path}')
	print(f'start_seconds: {start_seconds}, end_seconds: {end_seconds}')
	print(f'save_folder_path: {save_folder_path}')
	print(f'save_video_name: {save_video_name}')
	
	if os.path.exists(save_folder_path):
		if save_folder_path not in new_folder_path:
			shutil.rmtree(save_folder_path)
	os.makedirs(save_folder_path, exist_ok=True)
	new_folder_path.add(save_folder_path)
    
	video = cv2.VideoCapture(video_path)
	save_path = os.path.join(save_folder_path, save_video_name)

	# ffmpeg_extract_subclip(video_path, start_seconds, end_seconds, save_path)
	ffmpeg_extract_subclip(video_path, start_seconds, end_seconds, targetname=save_path)
