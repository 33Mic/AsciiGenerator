from PIL import Image
import clipboard

def pixelToGrayScale(pixels, j, i):
    red = pixels[j, i][0]
    green = pixels[j, i][1]
    blue = pixels[j, i][2]
    gray = (red + green + blue) // 3
    pixels[j, i] = (gray, gray, gray)

def pixelToAscii(pixels, j, i):
    ramp = " `.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"
    # test
    return ramp[int(pixels[j, i][0] * len(ramp) / 256)]

def detectSize(img: Image)->tuple[int, int]:
    MAX_SIZE = 128
    width, height = img.size
    if(width <= MAX_SIZE or height <= MAX_SIZE):
        print(f"Image is {width}x{height}.")
        return (width, height)
    else:
        print(f"Image is {width}x{height}.")
        print(f"Image is too large. Resizing to fit {MAX_SIZE}x{MAX_SIZE}.")
        if(width > height):
            return (MAX_SIZE, MAX_SIZE * height // width)
        else:
            return (MAX_SIZE * width // height, MAX_SIZE)
    
def main():
    try:
        img = Image.open(input("Enter image path: "))
    except:
        print("Invalid path")
        return
    
    img = img.resize(detectSize(img))
    pixels = img.load()

    # Convert to grayscale
    for i in range(img.height):
        for j in range(img.width):
            pixelToGrayScale(pixels, j, i)
    
    img.show()
    
    # Convert to ASCII
    text = ""
    for i in range(img.height):
        for j in range(img.width):
            text += pixelToAscii(pixels, j, i)
        text += "\n"
        
    clipboard.copy(text)
    print("ASCII copied to clipboard\n")

while True:
    main()