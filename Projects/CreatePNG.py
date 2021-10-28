from PIL import Image
from PIL import ImageDraw

def fill_pixles(startx, stopx ,starty,stopy, color):
    if image.width < stopx or image.height < stopy:
        raise ValueError("Invalid stop")
        return
    """
    Fills the given image with the given color.
    """
    for x in range(startx, stopx):
        for y in range(starty, stopy):
            image.putpixel((x, y), color)
    return image

def image_draw(image,width,color):
    """
    Draws a line on the given image.
    """
    draw = ImageDraw.Draw(image)
    draw.line((0,0,width,width),fill=color)
    return image
    
  
            

def draw_square(image, x, y, size, color):
    """
    Draws a square with the given size and color.
    """
    if image.width < x or image.height < y:
        raise ValueError("Invalid position")
        return
    """
    Draws a square with the given size and color.
    """
    for i in range(x, x + size):
        for j in range(y, y + size):
            image.putpixel((i, j), color)
    return image

def get_info(image):
    """
    Gets information about the given image.
    """
    print("Image size:", image.width, "x", image.height)
    print("Image mode:", image.mode)
    print("Image size in bytes:", image.size)
    print("Image format:", image.format)



def create_image(width, height):
    """
    Creates a new image with the given width and height.
    """
    return Image.new("RGBA", (width, height), color='rgb(255,255,255)')



def save_image(image, path):
    """
    Saves the given image to the given path.
    """
    image.save(path)
    
    
def create_checkerboard(image):
    """
    Creates a checkerboard image with the given width and height.
    """
    for x in range(image.width):
        for y in range(image.height):
            if (x + y) % 2 == 0:
                image.putpixel((x, y), (255, 255, 255))
            else:
                image.putpixel((x, y), (0, 0, 0))
    return image






def color_image(image):
    """
    Colors the given image.
    """
    for x in range(image.width):
        for y in range(image.height):
            image.putpixel((x, y), (x, y, x))
    return image

def set_colorspace(image, colorspace):
    """
    Sets the colorspace of the given image.
    """
    if colorspace not in ["RGB", "RGBA", "HSV", "HSB", "CMYK", "YCbCr"]:
        raise ValueError("Invalid colorspace")
        return
    """
    Changes the colorspace of the given image.
    """
    return image.convert(colorspace)

image = create_image(400, 400)



draw_square(image, 200, 0, 100, (255, 0, 0))


fill_pixles(startx=0, stopx=68, starty=0, stopy=400, color=(2555, 255, 0)) 


draw = ImageDraw.Draw(image)
draw.rectangle((0, 20, 20, 0), 25, (255, 0, 255))
image_draw(image,40,(0,0,0))

image.show()


def fill_image(image, color):
    """
    Fills the given image with the given color.
    """
    for x in range(image.width):
        for y in range(image.height):
            image.putpixel((x, y), color)
    return image


# get_info(image)
# 


