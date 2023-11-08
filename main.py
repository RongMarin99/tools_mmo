import os
from moviepy.editor import VideoFileClip

def cut_video_into_clips(input_file, output_prefix, clip_duration):
    # Load the video clip
    video_clip = VideoFileClip(input_file)

    # Calculate the number of clips
    num_clips = int(video_clip.duration / clip_duration)

    for i in range(num_clips):
        # Calculate start and end times for each clip
        start_time = i * clip_duration
        end_time = (i + 1) * clip_duration

        # Trim the clip to the specified duration without audio
        trimmed_clip = video_clip.subclip(start_time, end_time)

        # Create a new video file for each clip without audio
        output_file = f"{output_prefix}_clip_{i + 1}.mp4"
        trimmed_clip.write_videofile(output_file, codec="libx264", audio_codec="aac", fps=video_clip.fps, bitrate="5000k", threads=4, ffmpeg_params=["-crf", "18", "-preset", "slow", "-movflags", "faststart"])

    # Close the video clip
    video_clip.close()

# Function to process all video files in a folder
def process_videos_in_folder(input_folder, output_folder, clip_duration):
    # Ensure the output folder exists, create it if necessary
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all video files in the input folder
    video_files = [f for f in os.listdir(input_folder) if f.endswith(".mp4")]

    # Process each video file
    for video_file in video_files:
        input_path = os.path.join(input_folder, video_file)
        output_prefix = os.path.join(output_folder, os.path.splitext(video_file)[0])
        cut_video_into_clips(input_path, output_prefix, clip_duration)

# Example usage
input_folder = "input"  # Replace with your input folder path
output_folder = "output"  # Replace with your desired output folder path
clip_duration = 45  # Duration of each clip in seconds

process_videos_in_folder(input_folder, output_folder, clip_duration)
