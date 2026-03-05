import subprocess
import sys
import time
import os

# --- 1. DEPENDENCY CHECK FIRST ---
packages = ['pywinauto', 'pywin32', 'comtypes', 'pyautogui', 'Pillow']
print("Checking dependencies...")
try:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + packages)
    print("All dependencies installed.")
except subprocess.CalledProcessError as e:
    print(f"Error installing packages: {e}")
    sys.exit(1)

# --- 2. IMPORT AFTER INSTALLATION ---
import pyautogui

# --- CONFIG ---
CLICK_X, CLICK_Y = 1100, 725
WAIT_TIME = 30
SCREENSHOT_DIR = "screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def take_screenshot(name):
    path = os.path.join(SCREENSHOT_DIR, name)
    try:
        pyautogui.screenshot(path)
        print(f"Screenshot saved: {path}")
    except Exception as e:
        print(f"Error taking screenshot {name}: {e}")

# --- TEST SCREENSHOT ---
take_screenshot("01_after_install.png")

# --- LAUNCH INSTALLER ---
second_path = os.path.join(os.getcwd(), "install-3.exe")
print(f"Launching Second from: {second_path}")

if not os.path.exists(second_path):
    print(f"ERROR: {second_path} not found!")
    sys.exit(1)

subprocess.Popen(second_path, shell=True)
time.sleep(10)
take_screenshot("10_after_launching_second.png")

# --- AUTOMATION SEQUENCE ---
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('up')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('enter')
time.sleep(10)
take_screenshot("11a_after_finishing_second.png")

pyautogui.press('tab')
time.sleep(1)
pyautogui.press('space')
time.sleep(1)
pyautogui.press('enter')
time.sleep(10)

pyautogui.press('right')
take_screenshot("11b_after_finishing_second.png")
time.sleep(1)

pyautogui.press('right')
time.sleep(1)
take_screenshot("11c_after_finishing_second.png")

pyautogui.press('tab')
time.sleep(1)
take_screenshot("11d_after_finishing_second.png")

pyautogui.press('space')
time.sleep(1)
take_screenshot("11e_after_finishing_second.png")

pyautogui.press('tab')
time.sleep(1)
take_screenshot("11f_after_finishing_second.png")

pyautogui.write("LetterNews")
pyautogui.press('tab')
take_screenshot("11_after_finishing_second.png")

print("Automation completed successfully!")
