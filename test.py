import win32ui
import win32gui

class DesktopWindow(object):
    def __init__(self, *args, **kwargs):
        self.window_id = win32gui.GetDesktopWindow()
        self.window_dc = win32gui.GetWindowDC(self.window_id)
        pass
    def get_pixel_color(self, i_x, i_y):
        long_colour = win32gui.GetPixel(self.window_dc, i_x, i_y)
        print(long_colour)
        i_colour = int(long_colour)
        return (i_colour & 0xff, (i_colour >> 8) & 0xff,
                (i_colour >> 16) & 0xff)

limits = [
    [35, 395],
    [35 + 80 + 75, 395 + 80]
]

dtop = DesktopWindow()

while True:
    colour = dtop.get_pixel_color(limits[1][0], limits[0][1] + 40)
    print(colour)