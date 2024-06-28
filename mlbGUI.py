import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore
from tkinter import *
from PIL import Image, ImageTk # type: ignore
import sys
import os

teamNames = {'redsox': 'aleast', 'padres': 'nlwest', 'dodgers': 'nlwest',
            'braves': 'nleast' , 'bluejays': 'aleast', 'whitesox' : 'alcentral',
            'tigers': 'alcentral', 'guardians': 'alcentral', 'royals': 'alcentral',
            'twins': 'alcentral', 'orioles': 'aleast', 'yankees': 'aleast',
            'rays': 'aleast', 'astros': 'alwest', 'angels': 'alwest',
            'athletics': 'alwest', 'mariners': 'alwest', 'rangers': 'alwest',
            'cubs': 'nlcentral', 'reds': 'nlcentral', 'brewers': 'nlcentral',
            'pirates': 'nlcentral', 'cardinals': 'nlcentral', 'marlins': 'nleast',
            'mets': 'nleast', 'phillies': 'nleast', 'nationals': 'nleast',
            'diamondbacks': 'nlwest', 'rockies': 'nlwest', 'giants': 'nlwest'}

bgColor = 'light blue'
fontColor = 'black'

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), "images/" + relative_path)

class Team:

    def __init__(self, master):
        self.window = master
        self.geometry = self.window.geometry("700x700")
        self.title = self.window.title("MLB Stats")
        self.configure = self.window.configure(background = bgColor)
        self.playerLabels = []
        self.posLabels = []
        self.statLabels = []
        self.photoExist = False
        self.window.bind("<Key-q>", self.keyPressed)
        self.start()

    def start(self):
        self.getNameLabel = Label(self.window, text = "Enter a team name:",
                                bg = bgColor, fg = fontColor, font = 'none 20 bold')
        self.getTeamName = Entry(self.window, width = 20, bg = 'white', fg = fontColor)
        self.choosePathLabel = Label(self.window, text = "Sort by: ",
                                bg = bgColor, fg = fontColor, font = 'none 15 bold')
        self.hitsButton = Button(self.window, text = "Hits", width = 4,
                                command = self.hits, bg = 'white', activebackground = bgColor,
                                 highlightbackground = bgColor, fg = 'black')
        self.batAvgButton = Button(self.window, text = "Batting Average", width = 12,
                                command = self.batAvg, bg = 'white',
                                   highlightbackground = bgColor, fg = 'black')
        self.hrButton = Button(self.window, text = "Home Runs", width = 10,
                                command = self.homeruns, bg = 'white',
                               highlightbackground = bgColor, fg = 'black')

        self.getNameLabel.place(x = 120, y = 20)
        self.getTeamName.place(x = 320, y = 23)
        self.choosePathLabel.place(x = 140, y = 100)
        self.hitsButton.place(x = 210, y = 103)
        self.batAvgButton.place(x = 280, y = 103)
        self.hrButton.place(x = 422, y = 103)

    def keyPressed(self, e):
        self.window.destroy()

    def hits(self):
        self.teamName = self.getTeamName.get().lower().replace(' ', '')
        if self.teamName != '' and self.teamName in teamNames:
            self.getTeamName.delete(0, END)
            self.url = 'https://www.mlb.com/' + self.teamName + '/stats/hits/regular-season?playerPool=ALL'
            self.chart = {
                'Player': [],
                'Position': [],
                'Hits': []
            }
            self.choice = "Hits"
            self.statClass = 'selected-h6IPIIxg number-GoaicxKV align-right-TwjGe_gi is-table-pinned-lGP8KWTK'
            self.scrape()

    def batAvg(self):
        self.teamName = self.getTeamName.get().lower().replace(' ', '')
        if self.teamName != '' and self.teamName in teamNames:
            self.getTeamName.delete(0, END)
            self.url = 'https://www.mlb.com/' + self.teamName + '/stats/batting-average/regular-season?playerPool=ALL'
            self.chart = {
                'Player': [],
                'Position': [],
                'Bat Avg': []
            }
            self.choice = "Bat Avg"
            self.statClass = 'selected-h6IPIIxg col-group-start-Gn6clGbi number-GoaicxKV align-right-TwjGe_gi is-table-pinned-lGP8KWTK'
            self.scrape()

    def homeruns(self):
        self.teamName = self.getTeamName.get().lower().replace(' ', '')
        if self.teamName != '' and self.teamName in teamNames:
            self.getTeamName.delete(0, END)
            self.url = 'https://www.mlb.com/' + self.teamName + '/stats/regular-season?playerPool=ALL'
            self.chart = {
                'Player': [],
                'Position': [],
                'Homeruns': []
            }
            self.choice = "Homeruns"
            self.statClass = 'number-GoaicxKV align-right-TwjGe_gi is-table-pinned-lGP8KWTK'
            self.scrape()

    def scrape(self):
        if len(self.playerLabels) > 0:
            for i in range(len(self.playerLabels)):
                self.playerLabels[i].destroy()
                self.posLabels[i].destroy()
                self.statLabels[i].destroy()
            self.playerLabels = []
            self.posLabels = []
            self.statLabels = []
            self.header3.destroy()
        if self.photoExist:
            self.photoPlace.destroy()

        img = Image.open(resource_path(teamNames[self.teamName] + '.jpg'))
        img = img.resize((150, 150), Image.NEAREST)
        self.photo = ImageTk.PhotoImage(img)
        self.photoPlace = Label(self.window, image = self.photo)
        self.photoExist = True

        self.page = requests.get(self.url)
        soup = BeautifulSoup(self.page.content, 'html.parser')
        table = soup.find('div', class_="table-scroller-GsCM0EhI scroller")
        # self.stat = table.find_all('td', class_ = self.statClass)
        tbody = table.find('tbody')
        trs = tbody.find_all("tr")
        # self.rows = self.table.find_all('th', class_ = 'pinned-col-3lxtFnc col-group-start-sa9unvY0 number-aY5arzrB first-col-3aGPCzvr is-table-pinned-1WfPW2jT')
        self.header1 = Label(self.window, text = 'Player',
                            bg = bgColor, fg = fontColor, font = 'none 15 bold')
        self.header2 = Label(self.window, text = 'Position',
                            bg = bgColor, fg = fontColor, font = 'none 15 bold')
        self.header3 = Label(self.window, text = self.choice,
                            bg = bgColor, fg = fontColor, font = 'none 15 bold')

        self.photoPlace.place(x = 500, y = 300)
        self.header1.place(x = 130, y = 140)
        self.header2.place(x = 280, y = 140)
        self.header3.place(x = 380, y = 140)

        for index, tr in enumerate(trs):
            name = tr.find('a', class_='bui-link').attrs['aria-label']
            position = tr.find('div', class_='position-SAxuJGcx').text
            stat = tr.find('td', class_=self.statClass).text

            self.playerLabels.append(Label(self.window, text=name,
                                    bg = bgColor, fg = fontColor, font = 'none 12 bold'))
            self.posLabels.append(Label(self.window, text=position,
                                    bg = bgColor, fg = fontColor, font = 'none 12 bold'))
            self.statLabels.append(Label(self.window, text = stat,
                                    bg = bgColor, fg = fontColor, font = 'none 12 bold'))
            self.playerLabels[index].place(x = 130, y = 170 + (20 * index))
            self.posLabels[index].place(x = 300, y = 170 + (20 * index))
            self.statLabels[index].place(x = 380, y = 170 + (20 * index))

if __name__ == "__main__":
    root = Tk()
    app = Team(root)
    root.mainloop()
