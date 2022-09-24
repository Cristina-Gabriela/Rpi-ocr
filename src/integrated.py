import os
from picamera import PiCamera
from time import sleep

camera = PiCamera()

def main():
    try:
        # take photo and save as latest.png
        camera.start_preview(alpha=200)
        sleep(1)
        camera.capture("latest.png")
        camera.stop_preview()
        os.system(f"aplay okay.wav")
    except:
        print("Error: Cannot capture image")
        os.system(f"aplay error.wav")
        return False
        
    try:
        # OCR on Tesseract
        # requires:
        # sudo apt install tesseract-ocr
        os.system(f"tesseract latest.png latest --psm 12 -l chi_tra+chi_sim+eng")
    except:
        print("Error: Cannot complete OCR")
        os.system(f"aplay error.wav")
        return False
    
    # print file content
    os.system(f"cat latest.txt")
    
    try:
        # TTS on Espeak-NG
        # requires:
        # sudo apt install espeak-ng
        os.system(f"espeak-ng -f latest.txt -s 175 -v yue -w latest.wav")
        os.system(f"espeak-ng -f latest.txt -s 145 -v yue -w latest-slow.wav")
        
        # play sound
        os.system(f"aplay latest.wav")
        print("Done")
    except:
        print("Error: Cannot complete TTS and play sound")
        os.system(f"aplay error.wav")
        return False
    
    return True
    

def replay(isSlow):
    if isSlow:
        os.system(f"aplay latest-slow.wav")
    else:
        os.system(f"aplay latest.wav")
