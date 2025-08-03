import cv2
import os
import glob

image_folder = 'images'
video_name = 'output_video.mp4'
fps = 1
image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp']

images = []
for ext in image_extensions:
    images.extend(glob.glob(os.path.join(image_folder, ext)))

images.sort()

if not images:
    print(f"오류: '{image_folder}' 폴더에서 이미지를 찾을 수 없습니다. 경로를 확인해주세요.")
else:
    frame = cv2.imread(images[0])
    if frame is None:
        print(f"오류: 첫 번째 이미지 파일 '{images[0]}'을 읽을 수 없습니다.")
    else:
        height, width, layers = frame.shape
        size = (width, height)

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(video_name, fourcc, fps, size)

        print(f"총 {len(images)}개의 이미지를 비디오로 변환합니다...")

        for i, filename in enumerate(images):
            img = cv2.imread(filename)
            if img is not None:
                if (img.shape[1], img.shape[0]) != size:
                    img = cv2.resize(img, size)
                out.write(img)
                print(f" ({i+1}/{len(images)}) {filename} 처리 완료")
            else:
                print(f"경고: '{filename}' 파일을 읽을 수 없어 건너뜁니다.")

        out.release()

        print(f"\n성공: '{video_name}' 파일이 성공적으로 생성되었습니다.")
        print(f" - 해상도: {width}x{height}")
        print(f" - 프레임률: {fps} FPS")
