import os
# FIX 1: In version 0.7, split_video_ffmpeg is imported directly from the top level!
from scenedetect import detect, ContentDetector, split_video_ffmpeg

def run_auto_cutter():
    # FIX 2: Changed to match your file name 'my_vid.mp4' perfectly!
    input_video = "Screen Recording 2026-02-28 213521.mp4" 
    output_directory = "cuts"

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print(f"📁 Created folder: {output_directory}")

    print(f"🎬 Scanning '{input_video}' for scene changes...")

    try:
        # Detect all the hard visual cuts
        scene_list = detect(
            input_video,
            ContentDetector(threshold=27.0)
        )

        print(f"🎯 Found {len(scene_list)} scenes.")

        if not scene_list:
            print("⚠️ No scene cuts detected.")
            return

        print("⚡ Splitting video...")

        # Splitting the raw file seamlessly into the cuts directory
        split_video_ffmpeg(
            input_video,
            scene_list,
            output_dir=output_directory
        )

        print(f"🔥 Done! Clips saved in '{output_directory}'")

    except Exception as e:
        print(f"⚠️ Error: {e}")
        print("💡 Make sure FFmpeg is installed and available in PATH.")

if __name__ == "__main__":
    run_auto_cutter()