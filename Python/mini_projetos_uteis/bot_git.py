import pyautogui

pyautogui.PAUSE = 1
pyautogui.keyDown('ctrl')
pyautogui.keyDown('alt')
pyautogui.press('t')
pyautogui.keyUp('alt')
pyautogui.keyUp('ctrl')
pyautogui.write('terminal')
pyautogui.press('backspace')
pyautogui.PAUSE = 2
pyautogui.press('enter')
pyautogui.write('ls')
pyautogui.PAUSE = 0
pyautogui.write('cd Programacao')
pyautogui.press('enter')
pyautogui.write('cd Estudos')
pyautogui.press('enter')
