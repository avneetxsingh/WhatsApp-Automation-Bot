import pyautogui
import webbrowser
import time
#print(pyautogui.position()) # Debugging Command
#""" # Debugging Command
name = input("Enter Whom to Bomb : ")
num = int(input("Enter How Many Times to Bomb : "))
a = input("Enter What Do You Wanna Bombard with : ")
print("A Few Moments of Silence for",name,", Lol XD")
webbrowser.open("https://web.whatsapp.com/")
time.sleep(15) # Loading WhatsApp Web Beta Takes Eternity :-/
pyautogui.click(333, 204)
time.sleep(1)
pyautogui.write(name)
time.sleep(1)
pyautogui.click(369, 383)
time.sleep(1)
pyautogui.click(836, 977)
for i in range(num) :
    pyautogui.write(a)
    pyautogui.press("Enter")
    time.sleep(0.5)
pyautogui.write("This was a *PYTHON* WhatsApp Bot 💀")
pyautogui.press("Enter")
#""" # Debugging Command