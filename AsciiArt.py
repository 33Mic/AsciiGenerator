from PIL import Image
import clipboard

def pixelToGrayScale(pixels: list[list], j: int, i: int)-> None:
    red = pixels[j, i][0]
    green = pixels[j, i][1]
    blue = pixels[j, i][2]
    gray = (red + green + blue) // 3
    pixels[j, i] = (gray, gray, gray)

def pixelToAscii(pixels: list[list], j: int, i: int)-> str:
    ramp = " `.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"
    return ramp[int(pixels[j, i][0] * len(ramp) / 256)] + "  "

def detectSize(img: Image, max_size: int)-> tuple[int, int]:
    width, height = img.size
    if(width <= max_size or height <= max_size):
        print(f"Image is {width}x{height}.")
        return (width, height)
    else:
        print(f"Image is {width}x{height}.")
        print(f"Image is too large. Resizing to fit {max_size}x{max_size} with respect to aspect ratio.")
        if(width > height):
            return (max_size, max_size * height // width)
        else:
            return (max_size * width // height, max_size)
    
def main():
    max_size = 0
    try:
        img = Image.open(input("Enter image path: "))
    except:
        print("Invalid path")
        return
    
    try:
        max_size = int(input("Please specify maximum image height (in pixels): "))
    except:
        print("Not a number.")
        return
    
    img = img.resize(detectSize(img, max_size))
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