import subprocess


def record_lecture(output_path="data/recordings/lecture.mp4"):
    try:
        cmd = [
            "ffmpeg", "-y", "-f", "avfoundation",  # For Mac, replace with appropriate device for your OS
            "-i", "0",  # Default camera
            "-r", "30", output_path
        ]
        subprocess.run(cmd)
    except Exception as e:
        print(f"Error during recording: {e}")