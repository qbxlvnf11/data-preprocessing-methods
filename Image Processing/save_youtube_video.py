import subprocess
import json

def get_video_info(url):

    command = ["yt-dlp", "-j", url]
    
    print(f"'{url}' 영상 정보 가져오는 중...")
    
    try:
        result = subprocess.run(
            command,
            capture_output=True, 
            text=True,           
            encoding='utf-8',    
            check=True           
        )
        
        video_info = json.loads(result.stdout)

        video_title = video_info.get('title')
        video_id = video_info.get('id')
        uploader = video_info.get('uploader')
        duration_str = video_info.get('duration_string')

        print("영상 정보 가져오기 성공!")
        print(f"  - 제 목: {video_title}")
        print(f"  - 영상 ID: {video_id}")
        print(f"  - 채널명: {uploader}")
        print(f"  - 영상 길이: {duration_str}")
        print("="*40)

        return video_info
        
    except subprocess.CalledProcessError as e:
        print("영상 정보를 가져오는 중 오류가 발생했습니다.")
        print("오류 내용:", e.stderr)
        return None
    except FileNotFoundError:
        print("오류: 'yt-dlp'를 찾을 수 없습니다. 설치를 확인하세요.")
        return None
    except json.JSONDecodeError:
        print("오류: yt-dlp의 출력 결과를 JSON으로 변환하는 데 실패했습니다.")
        return None

def save_raw_youtube_video(video_url, save_path=None):
    
    command = [
        "yt-dlp",
        video_url
    ]
    
    if save_path is not None:
        command = [
            "yt-dlp",
            "-o", 
            save_path,
            video_url
        ]
    
    print(f"명령어 실행: {' '.join(command)}")
    print("-" * 30)

    try:
        subprocess.run(command, check=True)
        print("-" * 30)
        print(f"영상 저장: {save_path}")

    except FileNotFoundError:
        print("오류: 'yt-dlp'를 찾을 수 없습니다. 설치되었는지 확인하거나 환경 변수(PATH)를 확인하세요.")
    except subprocess.CalledProcessError as e:
        print("-" * 30)
        print(f"yt-dlp 실행 중 오류가 발생했습니다. (종료 코드: {e.returncode})")
