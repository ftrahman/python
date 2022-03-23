#
# ps8pr4.py  (Problem Set 8, Problem 4)
#
# Images as 2-D lists  
#
# Computer Science 111
# 

from hmcpng import *

def create_uniform_image(height, width, pixel):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels have the RGB values
        given by pixel
        inputs: height and width are non-negative integers
                pixel is a 1-D list of RBG values of the form [R,G,B],
                     where each element is an integer between 0 and 255.
    """
    pixels = []
    
    for r in range(height):
        row = [pixel] * width
        pixels += [row]

    return pixels


def blank_image(height, width):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns by calling the create_uniform_image function
        inputs: height and width are non-negative integers
    """
    new_pixels = create_uniform_image(height, width, [0, 255, 0])
    return new_pixels



    
def flip_horiz(pixels):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels have been flipped
        inputs: the 2-D list of pixels
    """

    height = len(pixels)
    width = len(pixels[0])
    blank_img = blank_image(height, width)
    x = width - 1

    for r in range(height):
        for c in range(width):
            blank_img[r][c] = pixels[r][x-c]


    return blank_img
            


def extract(pixels, rmin, rmax, cmin, cmax):
    """ creates and returns a 2-D list of pixels with height of rmax-rmin
        an width of cmax-cmin to create an extraction of an image
        inputs: the 2-D list of pixels, a maximum and minimum row value
        and a max and min column value
    """

    height = rmax-rmin
    width = cmax-cmin
    blank_img = blank_image(height, width)
    r_new = rmin
    c_new = cmin

    for r in range(height):
        r_new += 1
        for c in range(width):
            c_new += 1
            if c_new < cmax:
                blank_img[r][c] = pixels[r_new][c_new]
            else:
                c_new = cmin

    return blank_img

                
def transpose(pixels):
    ''' takes the 2-D list pixels containing pixels for an image,
        and that creates and returns a new 2-D list that is the
        transpose of pixels
        inputs: 2-D list of pixels
    '''
    height = len(pixels)
    width = len(pixels[0])
    blank_img = blank_image(width, height)
    
    for r in range(height):
        for c in range(width):
            blank_img[c][r] = pixels[r][c]

    return blank_img
            

def rotate_counterclockwise(pixels):
    ''' takes the 2-D list pixels containing pixels for an image,
        and rotates it counterclockwise
        inputs: 2-D list of pixels
    '''
    new = flip_horiz(pixels)
    new = transpose(new)

    return new


def rotate_clockwise(pixels):
    ''' takes the 2-D list pixels containing pixels for an image,
        and rotates it clockwise
        inputs: 2-D list of pixels
    '''
    new = transpose(pixels)
    new = flip_horiz(new)

    return new



    
