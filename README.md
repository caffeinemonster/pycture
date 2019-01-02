# pycture
pycture project - Realtime reddit picture frame / slideshow.


Description - Downloads top 25 post images from reddit urls stored in urls.txt then displays them as a slide show using feh, loops forever. Also checks file size in image header to avoid displaying 'This image is no longer available image' on imgur. I have this setup running on an rpi3 with the taskbar disabled and set to autorun when raspbian boots. Runs pretty flawlessly and have spent many hours working on this.

More detailed installation instructions coming soon.

Install feh (sudo apt-get install feh) (Image viewer / slide show application.)

Install pip (sudo apt-get install pip) (Python package manager)

Install python-requests package. (sudo pip install requests)

Copy to home directory urls.txt, pycture.py and pylogger.py.

Execute using /usr/bin/python ~/pycture.py

File description:

urls.txt (contains list of subreddits to grab data from.)

pycture.py (main program file)

pylogger.py (basic logging / error logging class.)
