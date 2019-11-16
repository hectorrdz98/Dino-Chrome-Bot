import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui as pag

def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    #processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    return processed_img

class Dino:
    def __init__(self):
        self.pos = (35, 395)
        self.size = (80, 80)
        self.head = (90, 410)
        self.eye = (83, 406)
        self.dA = [
            (35 + 80, 395), 
            (35 + 80 + 75, 395 + 80)
        ]
        self.dAC = (35 + 80 + 50, 395 + 40)

dino = Dino()
dinoFinalPos = tuple(map(sum, zip(dino.pos, dino.size)))

# last_time = time.time()
while True:
    screen = np.array(ImageGrab.grab(bbox=(0, 0, 640, 640)))
    
    # print('Loop took {} seconds'.format(time.time()-last_time))
    # last_time = time.time()

    """
    screen = cv2.rectangle(screen, dino.pos, 
        dinoFinalPos, (153, 153, 0), 2)

    screen = cv2.circle(screen, dino.head, 
        int(dino.size[0] / 4), (153, 153, 0), 2)
    """
    
    # print(screen[dino.dAC[0], dino.dAC[1]])

    imCrop = screen[
        dino.pos[1]:dinoFinalPos[1],
        dino.pos[0]:dino.dA[1][0]
    ]

    imCropGray = process_img(imCrop)
    
    close = False
    start = 40
    #for i in range(25, imCropGray.shape[0]-25):
    for j in range(60, 1, -1):
        pixel = imCropGray[start, imCropGray.shape[1]-j]
        # print(pixel, end=' ')
        if pixel != 255:
            pag.press('up')
            #print('jump')
            close = True
            break
        imCrop[start, imCrop.shape[1]-j] = [0, 0, 255]
    # print()
    # if close:
    #    break
    #for j in range(0,imCrop.shape[1]):
    #    pixel = imCrop[i, j]
    #    print(pixel)

    """
    screen = cv2.rectangle(screen, dino.dA[0], 
        dino.dA[1], (255, 102, 102), 2)
    """

    # screen[dino.eye[1], dino.eye[0]] = [0, 0, 255]

    # print(screen[dino.eye[1], dino.eye[0]])

    cv2.imshow('game', imCrop)

    # cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break