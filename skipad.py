import pyautogui
from random import randint

pyautogui.FAILSAFE = True

region_list = [(775, 560, 120, 10),
               (1735, 560, 120, 10),
               (1145, 726, 131, 21),
               (1785, 944, 131, 21)]

while True:
    for i in region_list:
        position = pyautogui.locateOnScreen('button{}.png'.format(randint(1, 2)),
                                            confidence=0.6,
                                            region=i,
                                            grayscale=True)

        if position is not None:
            pyautogui.click(position)


