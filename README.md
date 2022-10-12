How to install & use program

1. Create virtual enviroment

2. Run "pip install -r requirements.txt"

3. Run "python3 screenshots.py"

4. Set how many screenshot you want

5. Set time between screenshots

6. Images are saved in the ./screenshots folder

7. If you want to change the position of the screenshots you have to change the bbox coordinates (bbox=(0, 450, 1585, 1050)). If you want the fullscreen screenshots use ImageGrab.grab() instead of bbox.