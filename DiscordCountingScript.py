import pyautogui
from time import sleep

nextnumber = 10
# here you must type next number on the channel

print("PL: Przygotuj sie, za 10 sekund program rozpocznie dzialanie!")
print("EN: Get ready, in 10 seconds the program will start!")
print("To end program you must close window!")
sleep(10)
for i in range(nextnumber,2147483647,1):
	sleep(2)
	pyautogui.write(str(i))
	pyautogui.press("enter")
