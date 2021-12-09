import wx
import requests

# load file bitmap and return it as a bitmap object
# for use with the "image" object
def load_image(filename, size):
    if filename[-4:] == ".lnk":
        # we are dealing with an internet image now
        with open(filename, "r") as file:
            pass
    else:
        # file extension checking not required, because a failure mode is prepared
        temp = 0
        try:
            temp = wx.Bitmap(filename, wx.BITMAP_TYPE_ANY)
            temp = scale_bitmap(temp, size[0], size[1])
        except:
            temp = wx.Bitmap("resources/nofile.png", wx.BITMAP_TYPE_ANY)
            temp = scale_bitmap(temp, size[0], size[1])

        return temp


# scales bitmap, shouldnt need to be touched at all
def scale_bitmap(bitmap, width, height):
    image = wx.Bitmap.ConvertToImage(bitmap)
    image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
    result = wx.Bitmap(image)
    return result

def web_image(url, size):
    temp = requests.get(url, allow_redirects=True)
    filename = "images/" + url.split('/')[-1]
    with open(filename, 'wb') as file:
        file.write(temp.content)
    return load_image(filename, size)