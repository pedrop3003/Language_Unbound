import subprocess
import os
import sys
import os


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
os.chdir('/home/langunbound/Desktop/translate_project')
#this command runs it 60fps 720
command = "libcamera-vid --level 4.2 --framerate 25 width 1280 --height 720 -t 5000 -o my_video.h264"

#this is default
#command = "libcamera-vid -t 5000 -o my_video.h264"

process = subprocess.Popen(command, shell = True)
process.wait()

convert_command="mkvmerge -o my_video.mp4 my_video.h264"

convert_pro = subprocess.Popen(convert_command,shell=True)
convert_pro.wait()

user_input = input("Do you want to retake your video? (yes/no): ").lower()

if user_input == "yes" or user_input == "y":
        restart_program()
else:
        print("Exiting the program.")
