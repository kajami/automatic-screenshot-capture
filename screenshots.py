import time
import pyscreenshot as ImageGrab

from datetime import datetime

# number of screenshots & time between screenshots
try:
    screenshots = int(input("Set a number of screenshots you want: "))
    screenshot_interval = int(input("Set seconds between screenshots: "))
except ValueError:
    print("ERROR! Provided value need to be an integer.")
    raise

# take screenshots and save them in /screenshots folder
i=0
while(i<screenshots):
    print("Taking screenshot...")
    # if you want to take a fullscreen screenshot use im = ImageGrab.grab()

    # grab a spesific part of the screen
    # X1,Y1,X2,Y2
    im = ImageGrab.grab(bbox=(0, 450, 1585, 1050))

    image_name = f"screenshot-{str(datetime.now())}"

    # save image file
    filepathloc = f"./screenshots/{image_name}.png"
    im.save(filepathloc)

    i += 1
    time.sleep(screenshot_interval)
    print(f"Screenshot taken...({i}/{screenshots})")
    
    if(i == screenshots):
        print(f"Completed! Total of {screenshots} screenshots saved in the ./screenshots folder.")



