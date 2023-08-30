import cv2
import argparse
import os 

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('--video_path', help='input video path', required=True)
	parser.add_argument('--video_fps', type=int, help='video fps',
		default=-1)
	parser.add_argument('--save_interval', type=int, help='saving fps interval',
		default=1)
	parser.add_argument('--result_path', help='result save folder',
		default='./images')

	args = parser.parse_args()

	return args

args = parse_args()
  
# read the video from specified path 
video_path = args.video_path
video = cv2.VideoCapture(video_path) 

# video fps
if args.video_fps == -1:
	video_fps = video.get(cv2.CAP_PROP_FPS)
else:
	video_fps = args.video_fps
save_interval = args.save_interval
print('video fps:', video_fps)
print('save_interval:', save_interval)

# creating a folder
result_path = args.result_path
if not os.path.exists(result_path): 
	os.makedirs(result_path) 

# frame num
currentframe = 0
  
while(True): 
      
	# reading from frame 
	ret, frame = video.read() 

	# if video is still left continue creating images
	if ret:
		if currentframe % save_interval == 0:
			image_path = result_path + '/' + str(currentframe) + '.png'
			print('Creating...' + image_path) 

			# writing the extracted images 
			cv2.imwrite(image_path, frame) 

		currentframe += 1
	else: 
		break
