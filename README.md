# RPi-ocr

"Reading Pen for the Visually Impaired" was a Raspberry Pi student project. The product chains inputs from a camera source through OCR and TTS software to sound outputs.

## Materials Needed
* A Raspberry Pi computer, with peripherals (monitor, keyboard, mouse, and all the cables) to display and configure the Raspberry Pi
* A Raspberry Pi Camera Module
* A Button that does not have "rebounce issue" (the main cause for the program to mistake single-clicks with double-clicks)

## Installation
* (Required, for /src/main.py) Install tesseract espeak-ng (it is the same as ESpeak but with Cantonese support)
	* In terminal, run `sudo apt-get install tesseract-ocr`. This installs Tesseract, the OCR software.
	* In terminal, run `sudo apt install tesseract-ocr-all`. This installs all available language packs for Tesseract.
	* In terminal, run `sudo apt-get install espeak-ng`. This installs ESpeak NG, the TTS software.
* (Optional, for /ocr_test/ocr.py) Install pytesseract and cv2 for python
	* In terminal, run `pip install pytesseract`. This installs a Tesseract library for python.
	* In terminal, run `pip install opencv-python`. This installs OpenCV for image processing in python.

In addition, connect and test the camera and the button.

![Product Image](/demo.png)

## Project Description
The project is done using Python, for a large part using `os.system()` to run command line sequences.

The /src folder contains the project source. This is how the product works:

0. Run `main.py`. It should start listening to the button.
1. When a single-click on the button is received, the Raspberry Pi captures an image after 1 second. Image is stored as `latest.png`.
2. The image is then passed to Tesseract which performs OCR. The resulting text is stored as `latest.txt`.
3. The text is then passed to ESpeak which performs TTS. This creates two sound files `latest.wav` ("normal" speed) and `latest-slow.wav` ("slow" speed).
4. It then plays `latest.wav`.
5. When a double-click on the button is received, it replays the slow version `latest-slow.wav`. The replay speed will swap between "normal" and "slow" on each subsequent replay.

The /ocr-test folder contains a test script for OCR visualization. It can be used with the command line `python ocr.py --image image.jpg`.

## Limitations
* The ESpeak-NG Cantonese is quite bad. It sounds like robot.
* The camera capture quality is not great, making unusable output most of the time.

These are some software improvements that I did not have the time to figure out:
* To make the product usable without no monitor/keyboard/mouse, main.py should run ***on startup*** after the Raspberry Pi is powered.
* Image processing before passing to Tesseract might help. https://duckduckgo.com/?q=image+preprocessing+opencv+tesseract

## Useful Links
* PiCamera documentation - https://picamera.readthedocs.io/en/release-1.13/
* Tesseract documentation - https://tesseract-ocr.github.io/tessdoc/
* ESpeak documentation - https://espeak.sourceforge.net/docindex.html
* OpenCV image processing tutorial - https://docs.opencv.org/4.x/d2/d96/tutorial_py_table_of_contents_imgproc.html
* Detailed guide on using buttons on a Raspberry Pi: https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/