#####
# Author: Anant Mishra
# Date: 2023-04-09
# Description: Cross platform gui for yt-dlp using Qt6; Supports Windows, Linux, and Mac
#              This is a work in progress; 
# Features:
#   - Download videos from youtube, vimeo, etc.
#   - Download playlists
#   - Multi-threaded downloads
#####

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QGridLayout, QWidget
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
from utils.YoutubeDL import YouTubeDL
    

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("yt-dlp GUI")
        self.initUI()


    def initUI(self):

        # Window widget
        self.window = QWidget()
        self.setCentralWidget(self.window)

        # Layout
        self.layout = QGridLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        self.window.setLayout(self.layout)

        # Textbox
        self.textbox = QLineEdit(self)
        self.textbox.setPlaceholderText("Enter URL")
        self.textbox.setText(self.getClipboardURL())
        self.layout.addWidget(self.textbox, 0, 0)

        # Button
        self.button = QPushButton("Download", self)
        self.button.clicked.connect(self.on_click)
        self.layout.addWidget(self.button, 0, 1)


    def getVideoInfo(self, url):
        ytdl = YouTubeDL(url)
        info = ytdl.getVideoInfo()
        return info
        

    def getClipboardURL(self):
        if QApplication.clipboard().mimeData().hasText():
            text = QApplication.clipboard().mimeData().text()
            if text.startswith("http"):
                return text
        return ""

    def on_click(self):
        print("Button Clicked")
        url = self.textbox.text()
        info = self.getVideoInfo(url)
        print(info.keys())
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
