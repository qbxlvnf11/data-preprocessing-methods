# from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy import VideoFileClip
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
  
# # path
# video_path = args.video_path
# save_path = args.save_path

# # Cut seconds
# start_seconds = args.start_seconds
# end_seconds = args.end_seconds

# # video = cv2.VideoCapture(video_path)

# # ffmpeg_extract_subclip(video_path, start_seconds, end_seconds, save_path)
# ffmpeg_extract_subclip(video_path, start_seconds, end_seconds, targetname=save_path)

def cut_video(video_path, save_path, start_seconds, end_seconds):

    print(f"  -> MoviePy로 영상 자르는 중: {os.path.basename(save_path)}")

    try:
        with VideoFileClip(video_path) as video:
            
            highlight_clip = video.subclipped(start_seconds, end_seconds)
            
            highlight_clip.write_videofile(
                save_path, 
                codec="libx264",        
                audio_codec="aac"       
            )
        
        print(f"  -> 저장 완료: {save_path}")

    except Exception as e:
        print(f"  -> MoviePy 작업 중 오류 발생: {e}")

cut_video(
    video_path=args.video_path, \
    save_path=args.save_path, \
    start_seconds=args.start_seconds, \
    end_seconds=args.end_seconds)
