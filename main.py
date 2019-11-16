import win32ui
import win32gui
import pyautogui as pag

colors = {
    'red': 2366701,
    'blue': 13387839
}

class DesktopWindow(object):
    def __init__(self, *args, **kwargs):
        self.window_id = win32gui.GetDesktopWindow()
        self.window_dc = win32gui.GetWindowDC(self.window_id)
        pass
    def get_pixel_color(self, i_x, i_y):
        long_colour = win32gui.GetPixel(self.window_dc, i_x, i_y)
        i_colour = int(long_colour)
        return (i_colour & 0xff, (i_colour >> 8) & 0xff,
                (i_colour >> 16) & 0xff)
    def set_pixel_color(self, i_x, i_y, color):
        win32gui.SetPixel(self.window_dc, i_x, i_y, color)

limits = {
    'cactus':   [ 35 + 80 + 75, 395 + 50],
    'birds':    [ 35 + 80 + 75, 395 - 10],
}

dtop = DesktopWindow()

jumping = False
holdingKey = False

minWhites = 7
whiteSpaces = 0

minHold = 7
holdKeyCont = 0


while True:
    pixelCactus = dtop.get_pixel_color(limits['cactus'][0], limits['cactus'][1])
    # pixelBirds = dtop.get_pixel_color(limits['birds'][0], limits['birds'][1])
    # dtop.set_pixel_color(limits['cactus'][0], limits['cactus'][1] + 1, colors['red'])
    # dtop.set_pixel_color(limits['birds'][0], limits['birds'][1] + 1, colors['blue'])
    
    if holdingKey:
        holdKeyCont += 1
    if holdKeyCont >= minHold:
        pag.keyUp('down')
        holdKeyCont = 0
        holdingKey = False

    if pixelCactus != (255, 255, 255):
        pag.press('up')
        jumping = True
        whiteSpaces = 0
        # print(pixelCactus)
    else:
        whiteSpaces += 1
        
        if jumping and whiteSpaces >= minWhites:
            # print('down')
            pag.keyDown('down')
            jumping = False
            holdingKey = True
    