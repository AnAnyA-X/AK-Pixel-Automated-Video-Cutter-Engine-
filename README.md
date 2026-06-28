# 🎬AK PIXEL: Automated Video Cutter Engine         

Hey! This is a simple Python script I built to automatically scan any long video, detect where the scenes change, and cut them into clean individual clips. No manual editing needed!

---

## 🔥 What It Does
* **Smart Scanning:** It looks at the video frames and instantly catches where a camera cut happens.
* **Auto-Slicing:** Once it finds the scenes (for example, it found 7 scenes in my test!), it cuts them and saves them cleanly in a folder called `cuts`.

## 🛠️ The Troubleshooting Journey (Lessons Learned)
While building and running this project, I ran into two classic developer errors and fixed them:
1. **Moov Atom Error:** Caught a corrupted video file where the index was missing. Fixed by using a proper completed recording.
2. **FFmpeg Path Issue:** The script found the scenes but couldn't cut them because the system was missing the physical slicing tool. Fixed by installing `FFmpeg` via Windows Winget and resetting the environment.

## 🚀 How to Use It

1. Make sure you have **Python** and **FFmpeg** installed on your laptop.
2. Put your video file in the main folder.
3. Run the script using your terminal:
```bash
python main.py
