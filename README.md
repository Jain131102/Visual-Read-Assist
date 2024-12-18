# Visual Read Assist

Visual Read Assist is an innovative project designed to aid individuals with visual impairments. The device captures images, converts the text into machine-readable format using OCR (Optical Character Recognition), and reads the text aloud using text-to-speech technology. By leveraging the Raspberry Pi and other hardware components, this project aims to provide a low-cost and portable solution for visually impaired individuals to access and understand textual information independently.

---

## Features

- **Image Capture**: Utilizes the Raspberry Pi camera to capture high-quality images.
- **Optical Character Recognition (OCR)**: Converts captured images into machine-readable text using `tesseract`.
- **Text-to-Speech Conversion**: Reads out the extracted text in real-time using `espeak`.
- **Audio Feedback**: Provides audio cues for user interaction, such as `Clicking picture` and `Picture clicked`.
- **Portable and Low-Cost**: Designed to be affordable and easy to use.

---

## Components

### Hardware Requirements
- Raspberry Pi 4B+
- 5MP Pi Camera
- Speakers or Headphones
- Power Supply
- Push Button
- Raspberry Pi Case

### Software Requirements
- Python 3
- Raspbian OS
- Required Libraries:
  - `subprocess`
  - `pytesseract`
  - `aplay`
  - `PIL (Pillow)`
  - `espeak`
  - `libcamera-still`
  - `tesseract-ocr`

---

## Installation

### 1. Hardware Setup
- Attach the Pi Camera to the Raspberry Pi’s camera slot.
- Connect speakers or headphones for audio output.
- Ensure the Raspberry Pi is powered on and connected to the internet.

### 2. Software Installation
- Update and install the required packages:
  ```bash
  sudo apt-get update
  sudo apt-get install espeak tesseract-ocr libcamera-dev python3-pip
  pip install pytesseract pillow

- Verify the installation of Tesseract OCR:
  ```bash
  tesseract --version
Ensure it displays the installed version without errors.

## Usage

### Step 1: Capture an Image
Run the `click_image.py` script to capture an image:
 ```bash
    python3 click_image.py
```
- The program announces "Clicking picture" via audio.
- Captures an image using the Raspberry Pi camera and saves it as test_image.jpg.
- Announces "Picture clicked" once the image is saved.

### Step 2: Extract Text and Convert to Speech
Run the `image_to_text_speech.py` script to process the captured image:
 ```bash
    python3 image_to_text_speech.py
```
- The program reads the captured image (`test_image.jpg` by default).
- Extracts text using Tesseract OCR.
- Reads the extracted text aloud using `espeak`.
- Prints the text in the terminal for reference.

  ---
 
