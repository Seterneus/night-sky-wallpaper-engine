import subprocess
import os
import sys

def build():
    print("Compiling real-time GPU GLSL wallpaper_app.exe with real Thunder sound assets...")
    
    audio_src = os.path.abspath(os.path.join("assets", "audio"))
    
    cmd = [
        sys.executable,
        "-m", "PyInstaller",
        "--noconfirm",
        "--onefile",
        "--windowed",
        "--name=wallpaper_app",
        "--distpath=.",
        "--workpath=build",
        "--specpath=build",
        "--collect-all=moderngl",
        "--collect-all=glcontext",
        f"--add-data={audio_src};assets/audio",
        "main.py"
    ]
    
    result = subprocess.run(cmd, cwd=os.path.abspath("."))
    if result.returncode == 0:
        print("\nSUCCESS: Real-time GPU wallpaper_app.exe compiled successfully.")
    else:
        print("\nERROR: Compilation failed.")

if __name__ == "__main__":
    build()
