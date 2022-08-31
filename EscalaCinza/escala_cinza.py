from PIL import Image


def grayscale(colored):
    w, h = colored.size
    img = Image.new("RGB", (w, h))

    for x in range(w):
        for y in range(h):
            pixel = colored.getpixel((x, y))

            lum = (pixel[0] + pixel[1] + pixel[2])//3
            img.putpixel((x, y), (lum, lum, lum))
    return img
