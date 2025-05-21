# Image to ASCII Converter

A simple Python script that turns images into ASCII art and copies the result to your clipboard.

## How to Use

1. Run the script:
   `python AsciiArt.py`

2. Enter the path to an image file when prompted.

3. Enter the maximum image height

4. The image will be resized (and aspect ratio adjusted), converted to grayscale, and shown as a preview.

5. ASCII art is generated and automatically copied to your clipboard.

## Requirements

* Python 3
* `Pillow`
* `clipboard`

Install dependencies with:

```
pip install pillow clipboard
```

## Notes
* Best results on simple or high-contrast images.
