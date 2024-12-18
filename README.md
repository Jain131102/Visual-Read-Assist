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

 ## Project Workflow

 ### 1.Image Capture : 
- Captures an image using the Raspberry Pi camera.
- Provides audio feedback to indicate the image capture process.
### Text Extraction:
- Converts the captured image into text using OCR (Tesseract).
### Text-to-Speech Conversion:
- Synthesizes the extracted text into real-time audio feedback.

---

## File Structure
- `click_image.py`: Captures an image using the Raspberry Pi camera and provides audio cues during the process.
- `image_to_text_speech.py`: Processes the captured image to extract text and convert it to speech.
- `test_image.jpg`: The default filename for the captured image.
- Dependencies:
 - `pytesseract`: For OCR functionality.
 - `espeak`: For text-to-speech conversion.
 - `libcamera-still`: For image capture.

---

## Future Enhancements
- Add support for multiple languages and handwriting recognition in OCR.
- Enable users to select voices and adjust speech rates in text-to-speech.
- Integrate with wearable devices, such as smart glasses, for hands-free operation.
- Improve OCR performance using advanced AI and machine learning models.

  ---

## References

- [Raspberry Pi Documentation](https://www.raspberrypi.com/documentation/)
- [Tesseract OCR GitHub](https://github.com/tesseract-ocr/tesseract)
- [Espeak Documentation](https://espeak.sourceforge.net/)
- [ItsFOSS Raspberry Pi Projects](https://itsfoss.com/raspberry-pi-projects/)

---

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).
