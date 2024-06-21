# MLB Stat Scrapper in Python

This is a project I first made in the summer of 2021 after my first year of college. While revisiting it, the class tags and overall method to get these stats had to be updated since the website this is scraping (mlb.com) changed the HTML slightly, so that had to be fixed.

To get started, run these lines
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

If you want to make it an executable, you will first need to make an icon for the app and add it into the `mlbGUI.spec' file, but then run
```bash
pyinstaller mlbGUI.spec
```
and then go into the `dist` folder and find the executable there. If you don't make an icon, it will not be able to be saved in the menu bar like other applications.
